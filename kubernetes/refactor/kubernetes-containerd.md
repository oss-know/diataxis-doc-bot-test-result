# 可拆分成的文档类型
指南、解释、参考

# 修改理由和意见
1. 原文档属于典型的How-to Guides，但混杂了解释性内容和版本参考信息
2. 需要拆分出：
   - 操作步骤归入指南
   - SELinux/SWAP影响说明归入解释
   - 软件版本信息归入参考
3. 重构时需：
   - 保持代码块和图片引用完整
   - 为指南步骤添加解释锚点跳转
   - 将版本信息转为参考表格
   - 清理标题多余空格

# 改进后的结果

## 指南（How-to guides）

### [环境配置](#环境配置)
------------------------------------------------------------------------------------------------------------------------------------
1 正确
#### 1. 设置主机名
```bash
$ hostnamectl set-hostname nodeName
```
------------------------------------------------------------------------------------------------------------------------------------
2 正确
#### 2. 配置防火墙
**方法一：**
开放etcd和API Server端口：

```bash
$ firewall-cmd --zone=public --add-port=2379/tcp --permanent
$ firewall-cmd --zone=public --add-port=2380/tcp --permanent
$ firewall-cmd --zone=public --add-port=6443/tcp --permanent
```
使规则生效：
```bash
$ firewall-cmd --reload
```
> ![](public_sys-resources/icon-note.gif)**说明**  
> 防火墙配置可能导致镜像无法使用，需根据镜像开放相应端口

**方法二：**
禁用防火墙：

```bash
$ systemctl stop firewalld
$ systemctl disable firewalld
```
------------------------------------------------------------------------------------------------------------------------------------
3 正确
#### 3. 禁用SELinux
[SELinux的影响](#selinux的影响)
```bash
$ setenforce 0
$ sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config
```
------------------------------------------------------------------------------------------------------------------------------------
4 正确
#### 4. 禁用swap
[swap的影响](#swap的影响)

```bash
$ swapoff -a
$ sed -ri 's/.*swap.*/#&/' /etc/fstab
```
------------------------------------------------------------------------------------------------------------------------------------
5 正确
#### 5. 网络配置
```bash
$ cat > /etc/sysctl.d/k8s.conf << EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
vm.swappiness=0
EOF
$ modprobe br_netfilter
$ sysctl -p /etc/sysctl.d/k8s.conf
```

------------------------------------------------------------------------------------------------------------------------------------
6 正确
### [配置containerd](#配置containerd)
生成默认配置：
```bash
$ containerd_conf="/etc/containerd/config.toml"
$ mkdir -p /etc/containerd
$ containerd config default > "${containerd_conf}"
```

配置pause_image：
```bash
$ pause_img=$(kubeadm config images list | grep pause | tail -1)
$ sed -i "/sandbox_image/s#\".*\"#\"${pause_img}\"#" "${containerd_conf}" 
```

设置cgroup驱动：
```bash
$ sed -i "/SystemdCgroup/s/=.*/= true/" "${containerd_conf}"
```

关闭证书验证：
```bash
$ sed -i '/plugins."io.containerd.grpc.v1.cri".registry.configs/a\[plugins."io.containerd.grpc.v1.cri".registry.configs."registry.k8s.io".tls]\n  insecure_skip_verify = true' /etc/containerd/config.toml
```

配置代理：
```bash
$ server_path="/etc/systemd/system/containerd.service.d"
$ mkdir -p "${server_path}"
$ cat > "${server_path}"/http-proxy.conf << EOF
[Service]
Environment="HTTP_PROXY=***"
Environment="HTTPS_PROXY=***"
Environment="NO_PROXY=***"
EOF
```
重启服务：
```bash
$ systemctl daemon-reload
$ systemctl restart containerd
```

### [集群部署](#集群部署)
------------------------------------------------------------------------------------------------------------------------------------
7 正确
#### 初始化集群
```bash
$ kubeadm init --config kubeletConfig.yaml
```

配置kubectl：
```bash
$ mkdir -p "$HOME"/.kube
$ cp -i /etc/kubernetes/admin.conf "$HOME"/.kube/config
$ chown "$(id -u)":"$(id -g)" "$HOME"/.kube/config
$ export KUBECONFIG=/etc/kubernetes/admin.conf
```
------------------------------------------------------------------------------------------------------------------------------------
8 错误 原文内容丢失
#### 部署flannel
```bash
$ kubectl apply -f kube-flannel.yml
```
------------------------------------------------------------------------------------------------------------------------------------
9 正确
#### 工作节点加入
```bash
$ unset http_proxy https_proxy
$ kubeadm join <br/>:</hash> --token <br/> --discovery-token-ca-cert-hash sha256:</hash>
```

获取token：
```bash
$ kubeadm token create
$ openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
```

## 解释（Explanations）
------------------------------------------------------------------------------------------------------------------------------------
10 正确
### SELinux的影响
SELinux的安全策略可能会阻止容器内的某些操作，比如写入特定目录、访问网络资源、或执行具有特权的操作。这会导致 CoreDNS 等关键服务无法正常运行，并表现为CrashLoopBackOff或 Error状态。

------------------------------------------------------------------------------------------------------------------------------------
11 正确
### swap的影响
Kubernetes的资源调度器根据节点的可用内存和CPU资源来决定Pod分配。如果启用swap，实际可用物理内存和逻辑内存可能不一致，会影响调度器决策，导致节点过载或调度错误。

## 参考（Reference）

------------------------------------------------------------------------------------------------------------------------------------

12 错误 增加原文没有的内容

### 软件版本

| 组件         | 架构   | 版本           |
|--------------|--------|----------------|
| containerd   | x86_64 | 1.6.22-15      |
| kubernetes   | x86_64 | 1.29.1-4       |
| cri-tools    | x86_64 | 1.29.0-3       |

------------------------------------------------------------------------------------------------------------------------------------

13 错误 增加原文没有的内容

### 端口说明

- etcd端口：2379/tcp, 2380/tcp
- API Server端口：6443/tcp