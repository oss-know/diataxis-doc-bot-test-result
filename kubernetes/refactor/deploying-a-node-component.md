# 可拆分成的文档类型

指南、参考

# 修改理由和意见

1. 原文包含完整的操作步骤链（环境准备→组件部署→验证），符合How-to指南特征
2. 配置文件参数说明（kubelet_config.yaml/kube_proxy_config.yaml/Corefile）属于技术参考文档
3. 操作步骤与参数说明混杂，需要分离结构
4. 需要补充跨文档跳转链接提升可读性
5. 保持原有代码块完整性和操作顺序
6. 标题后存在多余空格需要清理

# 改进后的结果

## 指南（How-to guides）
# 部署 Node 节点组件

本章节仅以`k8snode1`节点为例。
------------------------------------------------------------------------------------------------------------------------------------
1  正确
## 环境准备

```bash
# 内网需要配置代理
$ dnf install -y docker iSulad conntrack-tools socat containernetworking-plugins
$ swapoff -a
$ mkdir -p /etc/kubernetes/pki/
$ mkdir -p /etc/cni/net.d
$ mkdir -p /opt/cni
# 删除默认kubeconfig
$ rm /etc/kubernetes/kubelet.kubeconfig
```
------------------------------------------------------------------------------------------------------------------------------------
2  正确
## 使用isulad作为运行时

```bash
# 配置iSulad
cat  /etc/isulad/daemon.json
{
        "registry-mirrors": [
                "docker.io"
        ],
        "insecure-registries": [
                "k8s.gcr.io",
                "quay.io"
        ],
        "pod-sandbox-image": "k8s.gcr.io/pause:3.2",# pause类型
        "network-plugin": "cni", # 置空表示禁用cni网络插件则下面两个路径失效， 安装插件后重启isulad即可
        "cni-bin-dir": "/usr/libexec/cni/",
        "cni-conf-dir": "/etc/cni/net.d",
}

# 在iSulad环境变量中添加代理，下载镜像
cat /usr/lib/systemd/system/isulad.service
[Service]
Type=notify
Environment="HTTP_PROXY=http://name:password@proxy:8080"
Environment="HTTPS_PROXY=http://name:password@proxy:8080"

# 重启iSulad并设置为开机自启
systemctl daemon-reload
systemctl restart isulad
```

[环境准备](#环境准备) → [使用isulad作为运行时](#使用isulad作为运行时) → [创建 kubeconfig 配置文件](#创建-kubeconfig-配置文件)
------------------------------------------------------------------------------------------------------------------------------------
3  错误
## 创建 kubeconfig 配置文件

对各节点依次如下操作创建配置文件：

```bash
$ kubectl config set-cluster openeuler-k8s \
    --certificate-authority=/etc/kubernetes/pki/ca.pem \
    --embed-certs=true \
    --server=https://192.168.122.154:6443 \
    --kubeconfig=k8snode1.kubeconfig

$ kubectl config set-credentials system:node:k8snode1 \
    --client-certificate=/etc/kubernetes/pki/k8snode1.pem \
    --client-key=/etc/kubernetes/pki/k8snode1-key.pem \
    --embed-certs=true \
    --kubeconfig=k8snode1.kubeconfig

$ kubectl config set-context default \
    --cluster=openeuler-k8s \
    --user=system:node:k8snode1 \
    --kubeconfig=k8snode1.kubeconfig

$ kubectl config use-context default --kubeconfig=k8snode1.kubeconfig
```

**注：修改k8snode1为对应节点名**

[创建 kubeconfig 配置文件](#创建-kubeconfig-配置文件) → [拷贝证书](#拷贝证书)
------------------------------------------------------------------------------------------------------------------------------------
4 正确
## 拷贝证书

和控制面一样，所有证书、密钥和相关配置都放到`/etc/kubernetes/pki/`目录。

```bash
$ ls /etc/kubernetes/pki/
ca.pem                 k8snode1.kubeconfig  kubelet_config.yaml     kube-proxy-key.pem     kube-proxy.pem
k8snode1-key.pem  k8snode1.pem         kube_proxy_config.yaml  kube-proxy.kubeconfig
```

[拷贝证书](#拷贝证书) → [CNI 网络配置](#cni-网络配置)
------------------------------------------------------------------------------------------------------------------------------------
5  错误
## CNI 网络配置

先通过 containernetworking-plugins 作为 kubelet 使用的 cni 插件，后续可以引入 calico，flannel 等插件，增强集群的网络能力。

```bash
# 桥网络配置
$ cat /etc/cni/net.d/10-bridge.conf
{
  "cniVersion": "0.3.1",
  "name": "bridge",
  "type": "bridge",
  "bridge": "cnio0",
  "isGateway": true,
  "ipMasq": true,
  "ipam": {
    "type": "host-local",
    "subnet": "10.244.0.0/16",
    "gateway": "10.244.0.1"
  },
  "dns": {
    "nameservers": [
      "10.244.0.1"
    ]
  }
}

# 回-loop网络配置
$ cat /etc/cni/net.d/99-loopback.conf
{
    "cniVersion": "0.3.1",
    "name": "lo",
    "type": "loopback"
}
```

[CNI 网络配置](#cni-网络配置) → [部署 kubelet 服务](#部署-kubelet-服务)
------------------------------------------------------------------------------------------------------------------------------------
6 正确
## 部署 kubelet 服务

### 编写 systemd 配置文件

```bash
$ cat /usr/lib/systemd/system/kubelet.service
[Unit]
Description=kubelet: The Kubernetes Node Agent
Documentation=https://kubernetes.io/docs/
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/bin/kubelet \
 --config=/etc/kubernetes/pki/kubelet_config.yaml \
 --network-plugin=cni \
 --pod-infra-container-image=k8s.gcr.io/pause:3.2 \
 --kubeconfig=/etc/kubernetes/pki/k8snode1.kubeconfig \
 --register-node=true \
 --hostname-override=k8snode1 \
 --cni-bin-dir="/usr/libexec/cni/" \
 --v=2

Restart=always
StartLimitInterval=0
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**注意：如果使用isulad作为runtime，需要增加如下配置**

```bash
--container-runtime=remote \
--container-runtime-endpoint=unix:///var/run/isulad.sock \
```

[kubelet 配置文件参考](#kubelet配置参数) → [部署 kube-proxy](#部署-kube-proxy)
------------------------------------------------------------------------------------------------------------------------------------
7 正确
## 部署 kube-proxy

### 编写 systemd 配置文件

```bash
$ cat /usr/lib/systemd/system/kube-proxy.service
[Unit]
Description=Kubernetes Kube-Proxy Server
Documentation=https://kubernetes.io/docs/reference/generated/kube-proxy/
After=network.target

[Service]
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/proxy
ExecStart=/usr/bin/kube-proxy \
     $KUBE_LOGTOSTDERR \
     $KUBE_LOG_LEVEL \
     --config=/etc/kubernetes/pki/kube_proxy_config.yaml \
     --hostname-override=k8snode1 \
     $KUBE_PROXY_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```
------------------------------------------------------------------------------------------------------------------------------------
8 正确
[kube-proxy 配置参数参考](#kube-proxy配置参数) → [启动组件服务](#启动组件服务)

## 启动组件服务

```bash
$ systemctl enable kubelet kube-proxy
$ systemctl start kubelet kube-proxy
```

其他节点依次部署即可。

[启动组件服务](#启动组件服务) → [验证集群状态](#验证集群状态)
------------------------------------------------------------------------------------------------------------------------------------
9 正确
## 验证集群状态

等待几分钟，使用如下命令查看node状态：

```bash
$ kubectl get nodes --kubeconfig /etc/kubernetes/pki/admin.kubeconfig
NAME            STATUS   ROLES    AGE   VERSION
k8snode1   Ready    <none>   17h   v1.20.2
k8snode2   Ready    <none>   19m   v1.20.2
k8snode3   Ready    <none>   12m   v1.20.2
```

[验证集群状态](#验证集群状态) → [部署 coredns](#部署-coredns)
------------------------------------------------------------------------------------------------------------------------------------
10 正确
## 部署 coredns

coredns可以部署到node节点或者master节点，本文这里部署到节点`k8snode1`。

### 准备 systemd 的 service 文件

```bash
cat /usr/lib/systemd/system/coredns.service
[Unit]
Description=Kubernetes Core DNS server
Documentation=https://github.com/coredns/coredns
After=network.target

[Service]
ExecStart=bash -c "KUBE_DNS_SERVICE_HOST=10.32.0.10 coredns -conf /etc/kubernetes/pki/dns/Corefile"

Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```
------------------------------------------------------------------------------------------------------------------------------------
11 正确
### 启动服务

```bash
$ systemctl enable coredns
$ systemctl start coredns
```

[CoreDNS配置参数参考](#coredns配置参数) → [创建 coredns 的 Service 对象]
------------------------------------------------------------------------------------------------------------------------------------
12 正确
### 创建 coredns 的 Service 对象

```bash
$ cat coredns_server.yaml
apiVersion: v1
kind: Service
metadata:
  name: kube-dns
  namespace: kube-system
  annotations:
    prometheus.io/port: "9153"
    prometheus.io/scrape: "true"
  labels:
    k8s-app: kube-dns
    kubernetes.io/cluster-service: "true"
    kubernetes.io/name: "CoreDNS"
spec:
  clusterIP: 10.32.0.10
  ports:
  - name: dns
    port: 53
    protocol: UDP
  - name: dns-tcp
    port: 53
    protocol: TCP
  - name: metrics
    port: 9153
    protocol: TCP
```

[创建 coredns 的 Service 对象](#创建-coredns-的服务对象) → [创建 coredns 的 endpoint 对象]
------------------------------------------------------------------------------------------------------------------------------------
13 正确
### 创建 coredns 的 endpoint 对象

```bash
$ cat coredns_ep.yaml
apiVersion: v1
kind: Endpoints
metadata:
  name: kube-dns
  namespace: kube-system
subsets:
  - addresses:
      - ip: 192.168.122.157
    ports:
      - name: dns-tcp
        port: 53
        protocol: TCP
      - name: dns
        port: 53
        protocol: UDP
      - name: metrics
        port: 9153
        protocol: TCP
```

[创建 coredns 的 endpoint 对象](#创建-coredns-的-endpoint对象) → [确认 coredns 服务]
------------------------------------------------------------------------------------------------------------------------------------
14 正确
### 确认 coredns 服务

```bash
# 查看service对象
$ kubectl get service -n kube-system kube-dns
NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
kube-dns   ClusterIP   10.32.0.10   <none>        53/UDP,53/TCP,9153/TCP   51m
# 查看endpoint对象
$ kubectl get endpoints -n kube-system kube-dns
NAME       ENDPOINTS                                                    AGE
kube-dns   192.168.122.157:53,192.168.122.157:53,192.168.122.157:9153   52m
```
------------------------------------------------------------------------------------------------------------------------------------

15 错误
## 参考（Reference）

# 配置参数参考

## kubelet配置参数

### kubelet 依赖的配置文件

```yaml
kind: KubeletConfiguration
apiVersion: kubelet.config.k8s.io/v1beta1
authentication:
  anonymous:
    enabled: false
  webhook:
    enabled: true
  x509:
    clientCAFile: /etc/kubernetes/pki/ca.pem
authorization:
  mode: Webhook
clusterDNS:
- 10.32.0.10
clusterDomain: cluster.local
runtimeRequestTimeout: "15m"
tlsCertFile: "/etc/kubernetes/pki/k8snode1.pem"
tlsPrivateKeyFile: "/etc/kubernetes/pki/k8snode1-key.pem"
```

**注意：clusterDNS 的地址为：10.32.0.10，必须和之前设置的 service-cluster-ip-range 一致**

## kube-proxy配置参数
------------------------------------------------------------------------------------------------------------------------------------
16 错误
### kube-proxy 依赖的配置文件

```yaml
kind: KubeProxyConfiguration
apiVersion: kubeproxy.config.k8s.io/v1alpha1
clientConnection:
  kubeconfig: /etc/kubernetes/pki/kube-proxy.kubeconfig
clusterCIDR: 10.244.0.0/16
mode: "iptables"
```
------------------------------------------------------------------------------------------------------------------------------------

17 正确
## CoreDNS配置参数

### CoreDNS 配置文件

```yaml
.:53 {
    errors
    health {
      lameduck 5s
    }
    ready
    kubernetes cluster.local in-addr.arpa ip6.arpa {
      pods insecure
      endpoint https://192.168.122.154:6443
      tls /etc/kubernetes/pki/ca.pem /etc/kubernetes/pki/admin-key.pem /etc/kubernetes/pki/admin.pem
      kubeconfig /etc/kubernetes/pki/admin.kubeconfig default
      fallthrough in-addr.arpa ip6.arpa
    }
    prometheus :9153
    forward . /etc/resolv.conf {
      max_concurrent 1000
    }
    cache 30
    loop
    reload
    loadbalance
}
```

说明：

- 监听53端口；
- 设置kubernetes插件配置：证书、kube api的URL；
------------------------------------------------------------------------------------------------------------------------------------