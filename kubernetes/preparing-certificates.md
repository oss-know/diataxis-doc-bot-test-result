# 准备证书

**声明：本文使用的证书为自签名，不能用于商用环境**

部署集群前，需要生成集群各组件之间通信所需的证书。本文使用开源 CFSSL 作为验证部署工具，以便用户了解证书的配置和集群组件之间证书的关联关系。用户可以根据实际情况选择合适的工具，例如 OpenSSL 。

## 配置go环境

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

## 编译安装 CFSSL

编译安装 CFSSL 的参考命令如下（需要互联网下载权限，需要配置代理的请先完成配置，需要配置 go语言环境）:

```bash
$ wget --no-check-certificate  https://github.com/cloudflare/cfssl/archive/v1.5.0.tar.gz
$ tar -zxf v1.5.0.tar.gz
$ cd cfssl-1.5.0/
$ make -j6
# cp bin/* /usr/local/bin/
```

## 生成根证书

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

生成 CA 证书和密钥：

```bash
$ cfssl gencert -initca ca-csr.json | cfssljson -bare ca
```

得到如下证书：

```bash
ca.csr  ca-key.pem  ca.pem
```

## 生成 admin 帐户证书

admin 是 K8S 用于系统管理的一个帐户，编写 admin 帐户的 CSR 配置，例如 admin-csr.json：

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

生成证书：

```bash
$ cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes admin-csr.json | cfssljson -bare admin
```

结果如下：

```bash
admin.csr  admin-key.pem  admin.pem
```

## 生成 service-account 帐户证书

编写 service-account 帐户的 CSR 配置文件，例如 service-account-csr.json：

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

生成证书：

```bash
$ cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -profile=kubernetes service-account-csr.json | cfssljson -bare service-account
```

结果如下：

```bash
service-account.csr  service-account-key.pem  service-account.pem
```

## 生成 kube-controller-manager 组件证书

编写 kube-controller-manager 的 CSR 配置：

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

生成证书：

```bash
$ cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -profile=kubernetes kube-controller-manager-csr.json | cfssljson -bare kube-controller-manager
```

结果如下：

```bash
kube-controller-manager.csr  kube-controller-manager-key.pem  kube-controller-manager.pem
```

## 生成 kube-proxy 证书

编写 kube-proxy 的 CSR 配置：

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

生成证书：

```bash
$ cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -profile=kubernetes kube-proxy-csr.json | cfssljson -bare kube-proxy
```

结果如下：

```bash
kube-proxy.csr  kube-proxy-key.pem  kube-proxy.pem
```

## 生成 kube-scheduler 证书

编写 kube-scheduler 的 CSR 配置：

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

生成证书：

```bash
$ cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -profile=kubernetes kube-scheduler-csr.json | cfssljson -bare kube-scheduler
```

结果如下：

```bash
kube-scheduler.csr  kube-scheduler-key.pem  kube-scheduler.pem
```

## 生成 kubelet 证书

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

说明：如果节点存在多个 IP 或者其他别名，-hostname 可以增加其他的 IP 或者 hostname

结果如下：

```bash
k8snode1.csr       k8snode1.pem       k8snode2-key.pem  k8snode3-csr.json
k8snode1-csr.json  k8snode2.csr       k8snode2.pem      k8snode3-key.pem
k8snode1-key.pem   k8snode2-csr.json  k8snode3.csr      k8snode3.pem
```

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

注意：由于每个 node 所属的帐户组为 `system:node`，因此 CSR 的 CN 字段都为 `system:node` 加上`hostname`。

## 生成 kube-apiserver 证书

编写 kube api server 的 CSR 配置文件：

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

生成证书和密钥：

```bash
cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -hostname=10.32.0.1,192.168.122.154,192.168.122.155,192.168.122.156,127.0.0.1,kubernetes,kubernetes.default,kubernetes.default.svc,kubernetes.default.svc.cluster,kubernetes.svc.cluster.local -profile=kubernetes kubernetes-csr.json | cfssljson -bare kubernetes
```

结果如下：

```bash
kubernetes.csr  kubernetes-key.pem  kubernetes.pem
```

*说明：10.32.0.1 是内部 services 使用的 IP 地址区间，可以设置为其他值，后面启动 apiserver 服务时，会设置该参数。*

## 生成 etcd 证书（可选）

部署 etcd 有两种方式：

- 在每个 api-server 对应的机器都启动一个 etcd 服务
- 独立部署一个 etcd 集群服务

如果是和 api-server 一起部署，那么直接使用上面生成的 `kubernetes-key.pem` 和  `kubernetes.pem`  证书即可。

如果是独立的etcd集群，那么需要创建证书如下：

编写 etcd 的 CSR 配置：

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

生成证书：

```bash
$ cfssl gencert -ca=../ca/ca.pem -ca-key=../ca/ca-key.pem -config=../ca/ca-config.json -hostname=192.168.122.154,192.168.122.155,192.168.122.156,127.0.0.1 -profile=kubernetes etcd-csr.json | cfssljson -bare etcd
```

*说明：假设 etcd 集群的 IP地址是 192.168.122.154,192.168.122.155,192.168.122.156*

结果如下：

```bash
etcd.csr  etcd-key.pem  etcd.pem
```
