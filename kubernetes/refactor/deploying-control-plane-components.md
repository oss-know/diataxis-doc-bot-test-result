# 可拆分成的文档类型

指南（How-to guides）、参考（Reference）

# 修改理由和意见

1. 原文档混合了操作步骤和配置参数说明，不符合Diátaxis分层结构要求
2. 操作步骤（生成kubeconfig、部署服务等）应归类为指南
3. 配置参数列表（环境变量定义）和systemd服务单元文件应归类为参考
4. 代码块内容完整保留，仅通过标题层级重构结构
5. 添加跨章节跳转链接保持操作连贯性

# 改进后的结果

## 指南（How-to guides）

### 准备所有组件的 kubeconfig
------------------------------------------------------------------------------------------------------------------------------------
1 正确
#### kube-proxy
[生成 kube-proxy 的 kubeconfig](#kube-proxy)
```bash
$ kubectl config set-cluster openeuler-k8s --certificate-authority=/etc/kubernetes/pki/ca.pem --embed-certs=true --server=https://192.168.122.154:6443 --kubeconfig=kube-proxy.kubeconfig
$ kubectl config set-credentials system:kube-proxy --client-certificate=/etc/kubernetes/pki/kube-proxy.pem --client-key=/etc/kubernetes/pki/kube-proxy-key.pem --embed-certs=true --kubeconfig=kube-proxy.kubeconfig
$ kubectl config set-context default --cluster=openeuler-k8s --user=system:kube-proxy --kubeconfig=kube-proxy.kubeconfig
$ kubectl config use-context default --kubeconfig=kube-proxy.kubeconfig
```
------------------------------------------------------------------------------------------------------------------------------------
2 正确
#### kube-controller-manager
[生成 controller-manager 的 kubeconfig](#kube-controller-manager)
```bash
$ kubectl config set-cluster openeuler-k8s --certificate-authority=/etc/kubernetes/pki/ca.pem --embed-certs=true --server=https://127.0.0.1:6443 --kubeconfig=kube-controller-manager.kubeconfig
$ kubectl config set-credentials system:kube-controller-manager --client-certificate=/etc/kubernetes/pki/kube-controller-manager.pem --client-key=/etc/kubernetes/pki/kube-controller-manager-key.pem --embed-certs=true --kubeconfig=kube-controller-manager.kubeconfig
$ kubectl config set-context default --cluster=openeuler-k8s --user=system:kube-controller-manager --kubeconfig=kube-controller-manager.kubeconfig
$ kubectl config use-context default --kubeconfig=kube-controller-manager.kubeconfig
```
------------------------------------------------------------------------------------------------------------------------------------
3 正确
#### kube-scheduler
[生成 scheduler 的 kubeconfig](#kube-scheduler)
```bash
$ kubectl config set-cluster openeuler-k8s --certificate-authority=/etc/kubernetes/pki/ca.pem --embed-certs=true --server=https://127.0.0.1:6443 --kubeconfig=kube-scheduler.kubeconfig
$ kubectl config set-credentials system:kube-scheduler --client-certificate=/etc/kubernetes/pki/kube-scheduler.pem --client-key=/etc/kubernetes/pki/kube-scheduler-key.pem --embed-certs=true --kubeconfig=kube-scheduler.kubeconfig
$ kubectl config set-context default  --cluster=openeuler-k8s --user=system:kube-scheduler --kubeconfig=kube-scheduler.kubeconfig
$ kubectl config use-context default --kubeconfig=kube-scheduler.kubeconfig
```
------------------------------------------------------------------------------------------------------------------------------------
4 正确
#### admin
[生成 admin 的 kubeconfig](#admin)
```bash
$ kubectl config set-cluster openeuler-k8s --certificate-authority=/etc/kubernetes/pki/ca.pem --embed-certs=true --server=https://127.0.0.1:6443 --kubeconfig=admin.kubeconfig
$ kubectl config set-credentials admin --client-certificate=/etc/kubernetes/pki/admin.pem --client-key=/etc/kubernetes/pki/admin-key.pem --embed-certs=true --kubeconfig=admin.kubeconfig
$ kubectl config set-context default --cluster=openeuler-k8s --user=admin --kubeconfig=admin.kubeconfig
$ kubectl config use-context default --kubeconfig=admin.kubeconfig
```
------------------------------------------------------------------------------------------------------------------------------------
5 错误
#### 获得相关 kubeconfig 配置文件
```bash
admin.kubeconfig kube-proxy.kubeconfig  kube-controller-manager.kubeconfig  kube-scheduler.kubeconfig
```
------------------------------------------------------------------------------------------------------------------------------------
6 正确
### 生成密钥提供者的配置
[生成加密配置](#生成密钥提供者的配置)
```bash
$ cat generate.bash
#!/bin/bash

ENCRYPTION_KEY=$(head -c 32 /dev/urandom | base64)

cat > encryption-config.yaml <<EOF
kind: EncryptionConfig
apiVersion: v1
resources:
  - resources:
      - secrets
    providers:
      - aescbc:
          keys:
            - name: key1
              secret: ${ENCRYPTION_KEY}
      - identity: {}
EOF
# api-server启动配置 --encryption-provider-config=/etc/kubernetes/pki/encryption-config.yaml
```
------------------------------------------------------------------------------------------------------------------------------------
7 正确
### 拷贝证书
[准备证书目录](#拷贝证书)
```bash
# 准备证书目录
$ mkdir -p /etc/kubernetes/pki/
$ ls /etc/kubernetes/pki/
admin-key.pem  encryption-config.yaml              kube-proxy-key.pem     kubernetes.pem             service-account-key.pem
admin.pem      kube-controller-manager-key.pem     kube-proxy.kubeconfig  kube-scheduler-key.pem     service-account.pem
ca-key.pem     kube-controller-manager.kubeconfig  kube-proxy.pem         kube-scheduler.kubeconfig
ca.pem         kube-controller-manager.pem         kubernetes-key.pem     kube-scheduler.pem
```
------------------------------------------------------------------------------------------------------------------------------------
8 正确
### 部署 admin 角色的 RBAC
[创建和绑定 admin role](#部署-admin-角色的-rbac)
```bash
$ cat admin_cluster_role.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: system:kube-apiserver-to-kubelet
rules:
  - apiGroups:
      - ""
    resources:
      - nodes/proxy
      - nodes/stats
      - nodes/log
      - nodes/spec
      - nodes/metrics
    verbs:
      - "*"

$ kubectl apply --kubeconfig admin.kubeconfig -f admin_cluster_role.yaml
```

```bash
$ cat admin_cluster_rolebind.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: system:kube-apiserver
  namespace: ""
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:kube-apiserver-to-kubelet
subjects:
  - apiGroup: rbac.authorization.k8s.io
    kind: User
    name: kubernetes

$ kubectl apply --kubeconfig admin.kubeconfig -f admin_cluster_rolebind.yaml
```
------------------------------------------------------------------------------------------------------------------------------------
9 正确
### 部署 api server 服务
[修改 apiserver 配置](#apiserver-配置参数) | [编写 systemd 配置](#apiserver-systemd配置)
```bash
$ systemctl enable kube-controller-manager kube-scheduler kube-proxy
$ systemctl restart kube-controller-manager kube-scheduler kube-proxy
```
------------------------------------------------------------------------------------------------------------------------------------
10 错误
### 基本功能验证
[验证部署](#基本功能验证)
```bash
$ curl --cacert /etc/kubernetes/pki/ca.pem https://192.168.122.154:6443/version
{
  "major": "1",
  "minor": "20",
  "gitVersion": "v1.20.2",
  "gitCommit": "faecb196815e248d3ecfb03c680a4507229c2a56",
  "gitTreeState": "archive",
  "buildDate": "2021-03-02T07:26:14Z",
  "goVersion": "go1.15.7",
  "compiler": "gc",
  "platform": "linux/arm64"
}
```
------------------------------------------------------------------------------------------------------------------------------------
11 正确
## 参考（Reference）

### apiserver 配置参数
[配置参数位置](#部署-api-server-服务)
```bash
$ cat /etc/kubernetes/apiserver
KUBE_ADVERTIS_ADDRESS="--advertise-address=192.168.122.154"
KUBE_ALLOW_PRIVILEGED="--allow-privileged=true"
KUBE_AUTHORIZATION_MODE="--authorization-mode=Node,RBAC"
KUBE_ENABLE_ADMISSION_PLUGINS="--enable-admission-plugins=NamespaceLifecycle,NodeRestriction,LimitRanger,ServiceAccount,DefaultStorageClass,ResourceQuota"
KUBE_SECURE_PORT="--secure-port=6443"
KUBE_ENABLE_BOOTSTRAP_TOKEN_AUTH="--enable-bootstrap-token-auth=true"
KUBE_ETCD_CAFILE="--etcd-cafile=/etc/kubernetes/pki/ca.pem"
KUBE_ETCD_CERTFILE="--etcd-certfile=/etc/kubernetes/pki/kubernetes.pem"
KUBE_ETCD_KEYFILE="--etcd-keyfile=/etc/kubernetes/pki/kubernetes-key.pem"
KUBE_ETCD_SERVERS="--etcd-servers=https://192.168.122.154:2379,https://192.168.122.155:2379,https://192.168.122.156:2379"
KUBE_CLIENT_CA_FILE="--client-ca-file=/etc/kubernetes/pki/ca.pem"
KUBE_KUBELET_CERT_AUTH="--kubelet-certificate-authority=/etc/kubernetes/pki/ca.pem"
KUBE_KUBELET_CLIENT_CERT="--kubelet-client-certificate=/etc/kubernetes/pki/kubernetes.pem"
KUBE_KUBELET_CLIENT_KEY="--kubelet-client-key=/etc/kubernetes/pki/kubernetes-key.pem"
KUBE_KUBELET_HTTPS="--kubelet-https=true"
KUBE_PROXY_CLIENT_CERT_FILE="--proxy-client-cert-file=/etc/kubernetes/pki/kube-proxy.pem"
KUBE_PROXY_CLIENT_KEY_FILE="--proxy-client-key-file=/etc/kubernetes/pki/kube-proxy-key.pem"
KUBE_TLS_CERT_FILE="--tls-cert-file=/etc/kubernetes/pki/kubernetes.pem"
KUBE_TLS_PRIVATE_KEY_FILE="--tls-private-key-file=/etc/kubernetes/pki/kubernetes-key.pem"
KUBE_SERVICE_CLUSTER_IP_RANGE="--service-cluster-ip-range=10.32.0.0/16"
KUBE_SERVICE_ACCOUNT_ISSUER="--service-account-issuer=https://kubernetes.default.svc.cluster.local"
KUBE_SERVICE_ACCOUNT_KEY_FILE="--service-account-key-file=/etc/kubernetes/pki/service-account.pem"
KUBE_SERVICE_ACCOUNT_SIGN_KEY_FILE="--service-account-signing-key-file=/etc/kubernetes/pki/service-account-key.pem"
KUBE_SERVICE_NODE_PORT_RANGE="--service-node-port-range=30000-32767"
KUB_ENCRYPTION_PROVIDER_CONF="--encryption-provider-config=/etc/kubernetes/pki/encryption-config.yaml"
KUBE_REQUEST_HEADER_ALLOWED_NAME="--requestheader-allowed-names=front-proxy-client"
KUBE_REQUEST_HEADER_EXTRA_HEADER_PREF="--requestheader-extra-headers-prefix=X-Remote-Extra-"
KUBE_REQUEST_HEADER_GROUP_HEADER="--requestheader-group-headers=X-Remote-Group"
KUBE_REQUEST_HEADER_USERNAME_HEADER="--requestheader-username-headers=X-Remote-User"
KUBE_API_ARGS=""
```

### apiserver systemd配置
[服务配置详情](#编写-apiserver-的-systemd-配置)
```bash
cat /usr/lib/systemd/system/kube-apiserver.service
[Unit]
Description=Kubernetes API Server
Documentation=https://kubernetes.io/docs/reference/generated/kube-apiserver/
After=network.target
After=etcd.service

[Service]
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/apiserver
ExecStart=/usr/bin/kube-apiserver \
     $KUBE_ADVERTIS_ADDRESS \
     $KUBE_ALLOW_PRIVILEGED \
     $KUBE_AUTHORIZATION_MODE \
     $KUBE_ENABLE_ADMISSION_PLUGINS \
      $KUBE_SECURE_PORT \
     $KUBE_ENABLE_BOOTSTRAP_TOKEN_AUTH \
     $KUBE_ETCD_CAFILE \
     $KUBE_ETCD_CERTFILE \
     $KUBE_ETCD_KEYFILE \
     $KUBE_ETCD_SERVERS \
     $KUBE_CLIENT_CA_FILE \
     $KUBE_KUBELET_CERT_AUTH \
     $KUBE_KUBELET_CLIENT_CERT \
     $KUBE_PROXY_CLIENT_CERT_FILE \
     $KUBE_PROXY_CLIENT_KEY_FILE \
     $KUBE_TLS_CERT_FILE \
     $KUBE_TLS_PRIVATE_KEY_FILE \
     $KUBE_SERVICE_CLUSTER_IP_RANGE \
     $KUBE_SERVICE_ACCOUNT_ISSUER \
     $KUBE_SERVICE_ACCOUNT_KEY_FILE \
     $KUBE_SERVICE_ACCOUNT_SIGN_KEY_FILE \
     $KUBE_SERVICE_NODE_PORT_RANGE \
     $KUBE_LOGTOSTDERR \
     $KUBE_LOG_LEVEL \
     $KUBE_API_PORT \
     $KUBELET_PORT \
     $KUBE_ALLOW_PRIV \
     $KUBE_SERVICE_ADDRESSES \
     $KUBE_ADMISSION_CONTROL \
     $KUB_ENCRYPTION_PROVIDER_CONF \
     $KUBE_REQUEST_HEADER_ALLOWED_NAME \
     $KUBE_REQUEST_HEADER_EXTRA_HEADER_PREF \
     $KUBE_REQUEST_HEADER_GROUP_HEADER \
     $KUBE_REQUEST_HEADER_USERNAME_HEADER \
     $KUBE_API_ARGS
Restart=on-failure
Type=notify
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

### controller-manager 配置参数
[配置参数详情](#部署-controller-manager-服务)
```bash
$ cat /etc/kubernetes/controller-manager
KUBE_BIND_ADDRESS="--bind-address=127.0.0.1"
KUBE_CLUSTER_CIDR="--cluster-cidr=10.200.0.0/16"
KUBE_CLUSTER_NAME="--cluster-name=kubernetes"
KUBE_CLUSTER_SIGNING_CERT_FILE="--cluster-signing-cert-file=/etc/kubernetes/pki/ca.pem"
KUBE_CLUSTER_SIGNING_KEY_FILE="--cluster-signing-key-file=/etc/kubernetes/pki/ca-key.pem"
KUBE_KUBECONFIG="--kubeconfig=/etc/kubernetes/pki/kube-controller-manager.kubeconfig"
KUBE_LEADER_ELECT="--leader-elect=true"
KUBE_ROOT_CA_FILE="--root-ca-file=/etc/kubernetes/pki/ca.pem"
KUBE_SERVICE_ACCOUNT_PRIVATE_KEY_FILE="--service-account-private-key-file=/etc/kubernetes/pki/service-account-key.pem"
KUBE_SERVICE_CLUSTER_IP_RANGE="--service-cluster-ip-range=10.32.0.0/24"
KUBE_USE_SERVICE_ACCOUNT_CRED="--use-service-account-credentials=true"
KUBE_CONTROLLER_MANAGER_ARGS="--v=2"
```

### controller-manager systemd配置
[服务配置详情](#编写-controller-manager-的-systemd-配置文件)
```bash
$ cat /usr/lib/systemd/system/kube-controller-manager.service
[Unit]
Description=Kubernetes Controller Manager
Documentation=https://kubernetes.io/docs/reference/generated/kube-controller-manager/

[Service]
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/controller-manager
ExecStart=/usr/bin/kube-controller-manager \
     $KUBE_BIND_ADDRESS \
     $KUBE_LOGTOSTDERR \
     $KUBE_LOG_LEVEL \
     $KUBE_CLUSTER_CIDR \
     $KUBE_CLUSTER_NAME \
     $KUBE_CLUSTER_SIGNING_CERT_FILE \
     $KUBE_CLUSTER_SIGNING_KEY_FILE \
     $KUBE_KUBECONFIG \
     $KUBE_LEADER_ELECT \
     $KUBE_ROOT_CA_FILE \
     $KUBE_SERVICE_ACCOUNT_PRIVATE_KEY_FILE \
     $KUBE_SERVICE_CLUSTER_IP_RANGE \
     $KUBE_USE_SERVICE_ACCOUNT_CRED \
     $KUBE_CONTROLLER_MANAGER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

### scheduler 配置参数
[配置参数详情](#部署-scheduler-服务)
```bash
$ cat /etc/kubernetes/scheduler
KUBE_CONFIG="--kubeconfig=/etc/kubernetes/pki/kube-scheduler.kubeconfig"
KUBE_AUTHENTICATION_KUBE_CONF="--authentication-kubeconfig=/etc/kubernetes/pki/kube-scheduler.kubeconfig"
KUBE_AUTHORIZATION_KUBE_CONF="--authorization-kubeconfig=/etc/kubernetes/pki/kube-scheduler.kubeconfig"
KUBE_BIND_ADDR="--bind-address=127.0.0.1"
KUBE_LEADER_ELECT="--leader-elect=true"
KUBE_SCHEDULER_ARGS=""
```

### scheduler systemd配置
[服务配置详情](#编写-scheduler-的-systemd-配置文件)
```bash
$ cat /usr/lib/systemd/system/kube-scheduler.service
[Unit]
Description=Kubernetes Scheduler Plugin
Documentation=https://kubernetes.io/docs/reference/generated/kube-scheduler/

[Service]
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/scheduler
ExecStart=/usr/bin/kube-scheduler \
     $KUBE_LOGTOSTDERR \
     $KUBE_LOG_LEVEL \
     $KUBE_CONFIG \
     $KUBE_AUTHENTICATION_KUBE_CONF \
     $KUBE_AUTHORIZATION_KUBE_CONF \
     $KUBE_BIND_ADDR \
     $KUBE_LEADER_ELECT \
     $KUBE_SCHEDULER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

------------------------------------------------------------------------------------------------------------------------------------