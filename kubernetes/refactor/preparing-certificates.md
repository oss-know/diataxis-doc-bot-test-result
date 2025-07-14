# 可拆分成的文档类型

指南（How-to guides）

# 修改理由和意见

原文属于典型的操作指南类文档，但存在以下结构问题：
1. 多个独立操作步骤混合在一个文档中，缺乏明确的步骤分隔
2. 没有建立有效的导航链接体系
3. 重复出现的生成证书流程没有统一说明
4. 脚本类操作分散在文档各处
5. 缺乏统一的前置条件说明
重构后将：
1. 按证书类型拆分为独立操作单元
2. 建立统一的步骤模板
3. 添加前置条件和环境准备说明
4. 集中展示通用流程
5. 增加内部跳转链接提升可读性

# 改进后的结果

## 指南（How-to guides）

# 证书生成指南

## 环境准备

[生成根证书](#生成根证书) | [生成组件证书](#生成组件证书) | [生成节点证书](#生成kubelet证书) | [生成API Server证书](#生成kube-apiserver证书)

### 配置go环境

1. 下载go

    ```bash
    wget https://go.dev/dl/go1.22.3.linux-amd64.tar.gz
    ```

2. 移除旧版本并安装

    ```bash
    $ rm -rf /usr/local/go && tar -C /usr/local -xzf go1.22.3.linux-amd64.tar.gz
    ```

3. 添加环境变量

    ```bash
    export PATH=$PATH:/usr/local/go/bin
    ```

4. 检查是否安装成功

    ```bash
    go version
    ```

### 编译安装 CFSSL

编译安装 CFSSL 的参考命令如下（需要互联网下载权限，需要配置代理的请先完成配置，需要配置 go语言环境）:

```bash
$ wget --no-check-certificate  https://github.com/cloudflare/cfssl/archive/v1.5.0.tar.gz
$ tar -zxf v1.5.0.tar.gz
$ cd cfssl-1.5.0/
$ make -j6
# cp bin/* /usr/local/bin/
```

## 通用证书生成流程

所有证书生成均遵循以下流程：

1. 创建 CSR 配置文件
2. 使用 cfssl 生成证书
3. 验证生成结果

## 生成根证书

### 配置文件

编写 CA 配置文件，例如 ca-config.json：

```bash
$ cat ca-config.json | jq
{
  "signing": {
    "default": {
      "expiry": "8760h"
    },
    "profiles": {
      "kubernetes": {
        "usages": [
          "signing",
          "key encipherment",
          "server auth",
          "client auth"
        ],
        "expiry": "8760h"
      }
    }
  }
}
```

编写 CA CSR 文件，例如 ca-csr.json：

```bash
$ cat ca-csr.json  | jq
{
  "CN": "Kubernetes",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "L": "HangZhou",
      "O": "openEuler",
      "OU": "WWW",
      "ST": "BinJiang"
    }
  ]
}
```

### 生成证书

```bash
$ cfssl gencert -initca ca-csr.json | cfssljson -bare ca
```

### 生成结果

```bash
ca.csr  ca-key.pem  ca.pem
```

## 生成组件证书

[生成 admin 帐户证书](#生成-admin-帐户证书) | [生成 service-account 证书](#生成-service-account-帐户证书) | [生成 kube-controller-manager 证书](#生成-kube-controller-manager-组件证书) | [生成 kube-proxy 证书](#生成-kube-proxy-证书) | [生成 kube-scheduler 证书](#生成-kube-scheduler-证书)

### 生成 admin 帐户证书

#### CSR 配置

```bash
cat admin-csr.json | jq
{
  "CN": "admin",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "L": "HangZhou",
      "O": "system:masters",
      "OU": "Containerum",
      "ST": "BinJiang"
    }
  ]
}
```

#### 生成证书

```bash
$ cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes admin-csr.json | cfssljson -bare admin
```

#### 生成结果

```bash
admin.csr  admin-key.pem  admin.pem
```

### 生成 service-account 帐户证书

#### CSR 配置

```bash
cat service-account-csr.json | jq
{
  "CN": "service-accounts",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "L": "HangZhou",
      "O": "Kubernetes",
      "OU": "openEuler k8s install",
      "ST": "BinJiang"
    }
  ]
}
```

#### 生成证书

```bash
$ cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -profile=kubernetes service-account-csr.json | cfssljson -bare service-account
```

#### 生成结果

```bash
service-account.csr  service-account-key.pem  service-account.pem
```

### 生成 kube-controller-manager 组件证书

#### CSR 配置

```bash
{
  "CN": "system:kube-controller-manager",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "L": "HangZhou",
      "O": "system:kube-controller-manager",
      "OU": "openEuler k8s kcm",
      "ST": "BinJiang"
    }
  ]
}
```

#### 生成证书

```bash
$ cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -profile=kubernetes kube-controller-manager-csr.json | cfssljson -bare kube-controller-manager
```

#### 生成结果

```bash
kube-controller-manager.csr  kube-controller-manager-key.pem  kube-controller-manager.pem
```

### 生成 kube-proxy 证书

#### CSR 配置

```bash
{
  "CN": "system:kube-proxy",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "L": "HangZhou",
      "O": "system:node-proxier",
      "OU": "openEuler k8s kube proxy",
      "ST": "BinJiang"
    }
  ]
}
```

#### 生成证书

```bash
$ cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -profile=kubernetes kube-proxy-csr.json | cfssljson -bare kube-proxy
```

#### 生成结果

```bash
kube-proxy.csr  kube-proxy-key.pem  kube-proxy.pem
```

### 生成 kube-scheduler 证书

#### CSR 配置

```bash
{
  "CN": "system:kube-scheduler",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "L": "HangZhou",
      "O": "system:kube-scheduler",
      "OU": "openEuler k8s kube scheduler",
      "ST": "BinJiang"
    }
  ]
}
```

#### 生成证书

```bash
$ cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -profile=kubernetes kube-scheduler-csr.json | cfssljson -bare kube-scheduler
```

#### 生成结果

```bash
kube-scheduler.csr  kube-scheduler-key.pem  kube-scheduler.pem
```

## 生成 kubelet 证书

### 批量生成脚本

由于证书涉及到 kubelet 所在机器的 hostname 和 IP 地址信息，因此每个 node 节点配置不尽相同，所以编写脚本完成，生成脚本如下：

```bash
$ cat node_csr_gen.bash

#!/bin/bash

nodes=(k8snode1 k8snode2 k8snode3)
IPs=("192.168.122.157" "192.168.122.158" "192.168.122.159")

for i in "${!nodes[@]}"; do

cat > "${nodes[$i]}-csr.json" <<EOF
{
  "CN": "system:node:${nodes[$i]}",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "L": "HangZhou",
      "O": "system:nodes",
      "OU": "openEuler k8s kubelet",
      "ST": "BinJiang"
    }
  ]
}
EOF

 # generate ca
 echo "generate: ${nodes[$i]} ${IPs[$i]}"
 cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -hostname=${nodes[$i]},${IPs[$i]} -profile=kubernetes ${nodes[$i]}-csr.json | cfssljson -bare ${nodes[$i]}
done
```

### 生成结果

```bash
k8snode1.csr       k8snode1.pem       k8snode2-key.pem  k8snode3-csr.json
k8snode1-csr.json  k8snode2.csr       k8snode2.pem      k8snode3-key.pem
k8snode1-key.pem   k8snode2-csr.json  k8snode3.csr      k8snode3.pem
```

### 示例配置

CSR 配置信息，以 k8snode1 为例如下：

```bash
$ cat k8snode1-csr.json
{
  "CN": "system:node:k8snode1",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "L": "HangZhou",
      "O": "system:nodes",
      "OU": "openEuler k8s kubelet",
      "ST": "BinJiang"
    }
  ]
}
```

> 注意：由于每个 node 所属的帐户组为 `system:node`，因此 CSR 的 CN 字段都为 `system:node` 加上`hostname`。

## 生成 kube-apiserver 证书

### CSR 配置

```bash
$ cat kubernetes-csr.json | jq
{
  "CN": "kubernetes",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "L": "HangZhou",
      "O": "Kubernetes",
      "OU": "openEuler k8s kube api server",
      "ST": "BinJiang"
    }
  ]
}
```

### 生成证书

```bash
cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -hostname=10.32.0.1,192.168.122.154,192.168.122.155,192.168.122.156,127.0.0.1,kubernetes,kubernetes.default,kubernetes.default.svc,kubernetes.default.svc.cluster,kubernetes.svc.cluster.local -profile=kubernetes kubernetes-csr.json | cfssljson -bare kubernetes
```

### 生成结果

```bash
kubernetes.csr  kubernetes-key.pem  kubernetes.pem
```

> *说明：10.32.0.1 是内部 services 使用的 IP 地址区间，可以设置为其他值，后面启动 apiserver 服务时，会设置该参数。*

## 生成 etcd 证书（可选）

### 部署方式说明

部署 etcd 有两种方式：

- 在每个 api-server 对应的机器都启动一个 etcd 服务
- 独立部署一个 etcd 集群服务

如果是和 api-server 一起部署，那么直接使用上面生成的 `kubernetes-key.pem` 和  `kubernetes.pem`  证书即可。

### 独立集群证书

#### CSR 配置

```bash
cat etcd-csr.json | jq
{
  "CN": "ETCD",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "L": "HangZhou",
      "O": "ETCD",
      "OU": "openEuler k8s etcd",
      "ST": "BinJiang"
    }
  ]
}
```

#### 生成证书

```bash
$ cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -hostname=192.168.122.154,192.168.122.155,192.168.122.156,127.0.0.1 -profile=kubernetes etcd-csr.json | cfssljson -bare etcd
```

> *说明：假设 etcd 集群的 IP地址是 192.168.122.154,192.168.122.155,192.168.122.156*

#### 生成结果

```bash
etcd.csr  etcd-key.pem  etcd.pem
```