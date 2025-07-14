# 可拆分成的文档类型

指南（How-to guides）、参考（Reference）

# 修改理由和意见

1. 原文档混合了操作步骤和配置参数说明，不符合Diátaxis架构规范
2. 操作流程应归类为指南（How-to guides），参数说明应归类为参考（Reference）
3. 注意事项中的参数说明需要与配置参数合并形成完整的参考文档
4. 服务文件中的参数列表需要表格化处理以符合参考文档规范
5. 需要建立指南与参考之间的双向跳转链接

# 改进后的结果

## 指南（How-to guides）
------------------------------------------------------------------------------------------------------------------------------------
1、 正确
# 安装 etcd

## 准备环境

使能 etcd 使用的端口：

```bash
firewall-cmd --zone=public --add-port=2379/tcp
firewall-cmd --zone=public --add-port=2380/tcp
```
------------------------------------------------------------------------------------------------------------------------------------
2、 正确
## 安装 etcd 二进制

当前是通过 rpm 包安装 

```bash
rpm -ivh etcd*.rpm
```

准备目录

```bash
mkdir -p /etc/etcd /var/lib/etcd
cp ca.pem /etc/etcd/
cp kubernetes-key.pem /etc/etcd/
cp kubernetes.pem /etc/etcd/
# 关闭selinux
setenforce 0
# 禁用/etc/etcd/etcd.conf文件的默认配置
# 注释掉即可，例如：ETCD_LISTEN_CLIENT_URLS="http://localhost:2379"
```
------------------------------------------------------------------------------------------------------------------------------------
3、 正确
## 编写 etcd.service 文件

以 `k8smaster0`机器为例：

```bash
$ cat /usr/lib/systemd/system/etcd.service
[Unit]
Description=Etcd Server
After=network.target
After=network-online.target
Wants=network-online.target

[Service]
Type=notify
WorkingDirectory=/var/lib/etcd/
EnvironmentFile=-/etc/etcd/etcd.conf
# set GOMAXPROCS to number of processors
ExecStart=/bin/bash -c "ETCD_UNSUPPORTED_ARCH=arm64 /usr/bin/etcd --name=k8smaster0 --cert-file=/etc/etcd/kubernetes.pem --key-file=/etc/etcd/kubernetes-key.pem --peer-cert-file=/etc/etcd/kubernetes.pem --peer-key-file=/etc/etcd/kubernetes-key.pem --trusted-ca-file=/etc/etcd/ca.pem --peer-trusted-ca-file=/etc/etcd/ca.pem --peer-client-cert-auth --client-cert-auth --initial-advertise-peer-urls https://192.168.122.154:2380 --listen-peer-urls https://192.168.122.154:2380 --listen-client-urls https://192.168.122.154:2379,https://127.0.0.1:2379 --advertise-client-urls https://192.168.122.154:2379 --initial-cluster-token etcd-cluster-0 --initial-cluster k8smaster0=https://192.168.122.154:2380,k8smaster1=https://192.168.122.155:2380,k8smaster2=https://192.168.122.156:2380 --initial-cluster-state new --data-dir /var/lib/etcd"

Restart=always
RestartSec=10s
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

**注意:** arm64上面需要增加启动设置`ETCD_UNSUPPORTED_ARCH=arm64`；[环境变量说明](#环境变量)

启动服务

```bash
$ systemctl enable etcd
$ systemctl start etcd
```

然后，依次部署其他机器即可。
------------------------------------------------------------------------------------------------------------------------------------
4、 正确
## 验证基本功能

```bash
$  ETCDCTL_API=3 etcdctl -w table endpoint status --endpoints=https://192.168.122.155:2379,https://192.168.122.156:2379,https://192.168.122.154:2379   --cacert=/etc/etcd/ca.pem   --cert=/etc/etcd/kubernetes.pem   --key=/etc/etcd/kubernetes-key.pem
+------------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|           ENDPOINT           |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFTAPPLIED INDEX | ERRORS |
+------------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
| https://192.168.122.155:2379 | b50ec873e253ebaa |  3.4.14 |  262 kB |     false |      false |       819 |         21 |           21 |        |
| https://192.168.122.156:2379 | e2b0d126774c6d02 |  3.4.14 |  262 kB |      true |      false |       819 |         21 |           21 |        |
| https://192.168.122.154:2379 | f93b3808e944c379 |  3.4.14 |  328 kB |     false |      false |       819 |         21 |           21 |        |
+------------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
```
------------------------------------------------------------------------------------------------------------------------------------
5、错误
## 参考（Reference）

# etcd 配置参考

## 配置参数说明

### etcd.service 配置项

| 配置项 | 说明 |
|--------|------|
| Description | 服务描述 |
| After | 服务启动依赖 |
| Wants | 服务依赖关系 |
| Type | 服务类型 |
| WorkingDirectory | 工作目录 |
| EnvironmentFile | 环境变量配置文件 |
| ExecStart | 启动命令 |
| Restart | 重启策略 |
| RestartSec | 重启间隔时间 |
| LimitNOFILE | 文件描述符限制 |

### etcd 启动参数

| 参数 | 说明 |
|------|------|
| --name | 节点名称 |
| --cert-file | 证书文件路径 |
| --key-file | 私钥文件路径 |
| --peer-cert-file | 对等节点证书路径 |
| --peer-key-file | 对等节点私钥路径 |
| --trusted-ca-file | 受信任CA证书路径 |
| --peer-trusted-ca-file | 对等节点CA证书路径 |
| --peer-client-cert-auth | 对等客户端证书认证 |
| --client-cert-auth | 客户端证书认证 |
| --initial-advertise-peer-urls | 初始对等节点广告URL |
| --listen-peer-urls | 监听对等节点URL |
| --listen-client-urls | 监听客户端URL |
| --advertise-client-urls | 广告客户端URL |
| --initial-cluster-token | 初始集群令牌 |
| --initial-cluster | 初始集群配置 |
| --initial-cluster-state | 初始集群状态 |
| --data-dir | 数据存储目录 |
------------------------------------------------------------------------------------------------------------------------------------
6、正确
## 环境变量

### ETCD_UNSUPPORTED_ARCH
用于指定不受支持的架构类型，如arm64：
```bash
ETCD_UNSUPPORTED_ARCH=arm64
```
------------------------------------------------------------------------------------------------------------------------------------
7、正确
## 证书说明

| 证书文件 | 用途 |
|----------|------|
| ca.pem | 根CA证书 |
| kubernetes-key.pem | Kubernetes私钥证书 |
| kubernetes.pem | Kubernetes客户端证书 |

## 注意事项说明

1. **证书复用**：当etcd与k8s control部署在同一机器时，可复用Kubernetes证书
2. **CA证书管理**：建议使用独立CA签发etcd证书，需在apiserver中配置对应信任关系
3. **集群配置**：`initial-cluster`参数需包含所有etcd节点配置
4. **存储优化**：建议使用SSD硬盘作为数据存储目录