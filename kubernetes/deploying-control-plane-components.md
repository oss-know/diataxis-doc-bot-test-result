# 部署控制面组件

## 准备所有组件的 kubeconfig

### kube-proxy

```bash
$ kubectl config set-cluster openeuler-k8s --certificate-authority=/etc/kubernetes/pki/ca.pem --embed-certs=true --server=https://192.168.122.154:6443 --kubeconfig=kube-proxy.kubeconfig
$ kubectl config set-credentials system:kube-proxy --client-certificate=/etc/kubernetes/pki/kube-proxy.pem --client-key=/etc/kubernetes/pki/kube-proxy-key.pem --embed-certs=true --kubeconfig=kube-proxy.kubeconfig
$ kubectl config set-context default --cluster=openeuler-k8s --user=system:kube-proxy --kubeconfig=kube-proxy.kubeconfig
$ kubectl config use-context default --kubeconfig=kube-proxy.kubeconfig
```

### kube-controller-manager

```bash
$ kubectl config set-cluster openeuler-k8s --certificate-authority=/etc/kubernetes/pki/ca.pem --embed-certs=true --server=https://127.0.0.1:6443 --kubeconfig=kube-controller-manager.kubeconfig
$ kubectl config set-credentials system:kube-controller-manager --client-certificate=/etc/kubernetes/pki/kube-controller-manager.pem --client-key=/etc/kubernetes/pki/kube-controller-manager-key.pem --embed-certs=true --kubeconfig=kube-controller-manager.kubeconfig
$ kubectl config set-context default --cluster=openeuler-k8s --user=system:kube-controller-manager --kubeconfig=kube-controller-manager.kubeconfig
$ kubectl config use-context default --kubeconfig=kube-controller-manager.kubeconfig
```

### kube-scheduler

```bash
$ kubectl config set-cluster openeuler-k8s --certificate-authority=/etc/kubernetes/pki/ca.pem --embed-certs=true --server=https://127.0.0.1:6443 --kubeconfig=kube-scheduler.kubeconfig
$ kubectl config set-credentials system:kube-scheduler --client-certificate=/etc/kubernetes/pki/kube-scheduler.pem --client-key=/etc/kubernetes/pki/kube-scheduler-key.pem --embed-certs=true --kubeconfig=kube-scheduler.kubeconfig
$ kubectl config set-context default  --cluster=openeuler-k8s --user=system:kube-scheduler --kubeconfig=kube-scheduler.kubeconfig
$ kubectl config use-context default --kubeconfig=kube-scheduler.kubeconfig
```

### admin

```bash
$ kubectl config set-cluster openeuler-k8s --certificate-authority=/etc/kubernetes/pki/ca.pem --embed-certs=true --server=https://127.0.0.1:6443 --kubeconfig=admin.kubeconfig
$ kubectl config set-credentials admin --client-certificate=/etc/kubernetes/pki/admin.pem --client-key=/etc/kubernetes/pki/admin-key.pem --embed-certs=true --kubeconfig=admin.kubeconfig
$ kubectl config set-context default --cluster=openeuler-k8s --user=admin --kubeconfig=admin.kubeconfig
$ kubectl config use-context default --kubeconfig=admin.kubeconfig
```

### 获得相关 kubeconfig 配置文件

```bash
admin.kubeconfig kube-proxy.kubeconfig  kube-controller-manager.kubeconfig  kube-scheduler.kubeconfig
```

## 生成密钥提供者的配置

api-server 启动时需要提供一个密钥对`--encryption-provider-config=/etc/kubernetes/pki/encryption-config.yaml`，本文通过 urandom 生成一个：

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

## 拷贝证书

本文把所有组件使用的证书、密钥以及配置统一放到`/etc/kubernetes/pki/`目录下。

```bash
# 准备证书目录
$ mkdir -p /etc/kubernetes/pki/
$ ls /etc/kubernetes/pki/
admin-key.pem  encryption-config.yaml              kube-proxy-key.pem     kubernetes.pem             service-account-key.pem
admin.pem      kube-controller-manager-key.pem     kube-proxy.kubeconfig  kube-scheduler-key.pem     service-account.pem
ca-key.pem     kube-controller-manager.kubeconfig  kube-proxy.pem         kube-scheduler.kubeconfig
ca.pem         kube-controller-manager.pem         kubernetes-key.pem     kube-scheduler.pem
```

## 部署 admin 角色的 RBAC

使能 admin role

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

# 使能admin role 
$ kubectl apply --kubeconfig admin.kubeconfig -f admin_cluster_role.yaml
```

绑定 admin role

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

# 绑定admin role
$ kubectl apply --kubeconfig admin.kubeconfig -f admin_cluster_rolebind.yaml
```

## 部署 api server 服务

修改 apiserver 的 etc 配置文件：

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

所有apiserver的配置都在`/etc/kubernetes/config`文件中定义，然后在后面的service文件中直接使用即可。

大部分配置都是比较固定的，部分需要注意：

- `--service-cluster-ip-range`该地址需要和后面的设置的`clusterDNS`需要一致；

### 编写 apiserver 的 systemd 配置

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
     $KUBE_KUBELET_CLIENT_KEY \
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

## 部署 controller-manager 服务

修改 controller-manager 配置文件：

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

### 编写 controller-manager 的 systemd 配置文件

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

## 部署 scheduler 服务

修改 scheduler 配置文件：

```bash
$ cat /etc/kubernetes/scheduler
KUBE_CONFIG="--kubeconfig=/etc/kubernetes/pki/kube-scheduler.kubeconfig"
KUBE_AUTHENTICATION_KUBE_CONF="--authentication-kubeconfig=/etc/kubernetes/pki/kube-scheduler.kubeconfig"
KUBE_AUTHORIZATION_KUBE_CONF="--authorization-kubeconfig=/etc/kubernetes/pki/kube-scheduler.kubeconfig"
KUBE_BIND_ADDR="--bind-address=127.0.0.1"
KUBE_LEADER_ELECT="--leader-elect=true"
KUBE_SCHEDULER_ARGS=""
```

### 编写 scheduler 的 systemd 配置文件

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

## 使能各组件

```bash
$ systemctl enable kube-controller-manager kube-scheduler kube-proxy
$ systemctl restart kube-controller-manager kube-scheduler kube-proxy
```

## 基本功能验证

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
