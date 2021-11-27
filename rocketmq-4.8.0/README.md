# 部署rocketmq 集群 环境

## docker 部署
[docker](./docker/)


## k8s 部署
[kubernetes](./k8s/)


## 快速部署 nfs
```bash
python3 k8s/init_nfs.py
```

## 镜像构建

### rocketmq 镜像

[rocketmq-image](./image-build/build-rocketmq)

### rocketmq-dashboard 镜像

[rocketmq-dashboard](./image-build/build-dashboard)