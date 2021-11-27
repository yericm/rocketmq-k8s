#! /usr/bin/env python3
import platform
import os
import stat

def init_nfs():
    '''
    :param nfs_str: nfs 中共享挂载路径参数
    '''
    nfs_str="/data/demo   *(rw,sync,no_root_squash,no_subtree_check)"
    with open('/etc/exports','w',encoding='utf8') as n:
        n.write(nfs_str)

    if not os.path.exists('/data/demo'):
        '''
        :param exisk_ok: 如果为真执行 -p 操作
        '''
        os.makedirs('/data/demo',exist_ok=True)    # 如果指定的路径不存在，新建

    # 授权，相当于执行 --> chmod 777 /data/demo
    os.chmod('/data/demo',stat.S_IRWXU+stat.S_IRWXG+stat.S_IRWXO)

def main():
    '''
    :param system_type: 操作系统类型 例: ubuntu | centos 
    '''
    system_type=platform.uname().version.lower()
    if 'ubuntu' in system_type:
        #安装nfs
        os.system('apt install -y nfs-kernel-server rpcbind')
        init_nfs()
        # 启动&开机自启
        os.system('systemctl start rpcbind && systemctl start nfs-kernel-server.service')
        # 检查 是否启动成功
        if os.system('exportfs -rv') != 0:
            os.system(' /etc/init.d/nfs-kernel-server restart')
        os.system('systemctl enable rpcbind && systemctl enable nfs-kernel-server.service')
    elif 'centos' in system_type:
        #安装nfs
        os.system('yum install -y nfs-utils rpcbind')
        init_nfs()
        # 启动&开机自启
        os.system('systemctl start rpcbind && systemctl start nfs-server')
        os.system('systemctl enable rpcbind && systemctl enable nfs-server')

if __name__=='__main__':
    main()
