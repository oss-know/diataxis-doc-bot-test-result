# 可拆分成的文档类型

指南（How-to guides）

# 修改理由和意见

1. 原文档属于典型的操作指南类型，符合How-to guides特征：以完成特定任务为目标、包含可执行命令序列、有明确结果验证方式
2. 结构不合理之处：
   - 标题层级不够清晰
   - 操作步骤缺少上下文说明
   - 代码块与文字描述的逻辑关系需要强化
3. 重构方式：
   - 增加顶层操作目标说明
   - 将配置文件创建作为第一步
   - 将部署执行作为第二步
   - 保持原有代码块完整性和输出结果原样展示
   - 添加步骤间的逻辑跳转链接

# 改进后的结果

## 指南（How-to guides）

------------------------------------------------------------------------------------------------------------------------------------
1 正确
# 如何运行测试Pod

本指南演示如何通过Kubernetes部署运行一个测试用的Nginx Pod。

## 步骤1：创建Deployment配置文件

[步骤2：启动Pod](#步骤2-启动pod)

创建名为nginx.yaml的配置文件，内容如下：

```bash
$ cat nginx.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

------------------------------------------------------------------------------------------------------------------------------------
2 正确
## 步骤2：启动Pod

[步骤1：创建Deployment配置文件](#步骤1-创建deployment配置文件)

使用kubectl命令应用配置并验证部署结果：

```bash
$ kubectl apply -f nginx.yaml
deployment.apps/nginx-deployment created
$ kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-66b6c48dd5-6rnwz   1/1     Running   0          33s
nginx-deployment-66b6c48dd5-9pq49   1/1     Running   0          33s
nginx-deployment-66b6c48dd5-lvmng   1/1     Running   0          34s
```