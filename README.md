# k8s 部署 rocketmq

两主两从,同步复制异步刷盘。

## 准备nfs 服务器

需nfs共享目录存在，脚本文件需要修改nfs地址和目录。

## 创建 nfs-client 动态 storage

```bash
kubectl apply -f nfs_storage/
```

## 创建rocketmq 使用的配置文件

```bash
kubectl apply -f conf/
```

## 启动 nameserv、broker、mq-console

```bash
kubectl apply -f pod/
```

这一步保险起见先单独执行pod里面的  **mq-nmserv.yaml**，运行成功后在集体跑上面的命令。

## 测试

```bash
#进入容器
kubectl exec -it broker-a-0 -n rocketmq -- /bin/bash
# 进行生产消息测试
sh tools.sh org.apache.rocketmq.example.quickstart.Producer
sh tools.sh org.apache.rocketmq.example.quickstart.Consumer # 消费消息
```

**浏览器访问console界面**

```bash
http://ip:30808
```

## nameserver地址

```bash
mq-ns.rocketmq.svc.cluster.local:9876
```