# 可拆分成的文档类型

参考（Reference）、解释（Explanations）、指南（How-to guides）

# 修改理由和意见

1. 原文档混合了多种内容类型，需按Diátaxis分离：
   - 参数表格和命令基础信息属于参考文档（Reference）
   - Dockerfile语法说明属于解释文档（Explanations）
   - 命令使用示例属于指南文档（How-to guides）
2. 重构时需注意：
   - 保持原文内容完整，仅调整结构
   - 为相关部分添加锚点跳转链接
   - 分离不同命令的参考信息和指南示例
   - 保留完整的参数表格和代码示例

# 改进后的结果

## 教程（Tutorials）

无教程内容

## 指南（How-to guides）

### 如何构建镜像
示例：
1. 使用Dockerfile构建镜像：
   ```bash
   $ sudo docker build -t busybox:latest
   ```
2. 查看生成的镜像：
   ```bash
   docker images | grep busybox
   ```

### 如何查看镜像历史
示例：
```bash
$ sudo docker history busybox:test
```

### 如何列出镜像
示例：
```bash
$ sudo docker images
```

### 如何导入镜像
示例：
```bash
$ sudo docker import busybox.tar busybox:test
$ sudo docker images
```

### 如何加载镜像
示例：
```bash
$ sudo docker load -i busybox.tar
$ sudo docker images
```

### 如何登录镜像仓库
示例：
```bash
$ sudo docker login
```

### 如何拉取镜像
示例：
1. 从官方仓库拉取：
   ```bash
   $ sudo docker pull nginx
   ```
2. 从私有仓库拉取：
   ```bash
   $ sudo docker pull 192.168.1.110:5000/fedora
   ```

### 如何推送镜像
示例：
1. 打标签：
   ```bash
   $ sudo docker tag ubuntu:sshd 192.168.1.110:5000/busybox:sshd
   ```
2. 推送镜像：
   ```bash
   $ sudo docker push 192.168.1.110:5000/busybox:sshd
   ```

### 如何保存镜像
示例：
```bash
$ sudo docker save -o nginx.tar nginx:latest
```

## 参考（Reference）

### build命令
用法：**docker build [OPTIONS] PATH | URL | -**
功能：使用指定路径中的Dockerfile生成构建一个新的image

#### 参数说明
<a name="build_options"></a>
表4 参数说明：
| 参数 | 参数含义 |
|------|----------|
| --force-rm=false | 即使没有构建成功也删除构建过程中生成的容器 |
| --no-cache=false | 构建image的过程中不使用缓存 |
| -q, --quiet=false | 禁止构建过程中产生的冗余信息 |
| --rm=true | 构建成功后删除过程中生成的容器 |
| -t, --tag="" | 指定构建生成的image的tag名 |
| --build-arg=[] | 设置构建参数 |
| --label=[] | 镜像相关参数设置，各参数意义与create类似 |
| --isolation | 指定容器的隔离方法 |
| --pull | 构建时总是尝试获取最新版本镜像 |

### history命令
用法：**docker history [OPTIONS] IMAGE**
功能：显示一个image的变化历史

#### 选项参数
- -H, --human=true
- --no-trunc=false
- -q, --quiet=false

### images命令
用法：**docker images [OPTIONS] [NAME]**
功能：列出存在的image，不加选项时不显示中间的image

#### 选项参数
- -a, --all=false
- -f, --filter=[]
- --no-trunc=false
- -q, --quiet=false

（其他命令参数说明按相同方式归类）

## 解释（Explanations）

### Dockerfile详解

Dockerfile是一个镜像的表示，可以通过Dockerfile来描述构建镜像的步骤，并自动构建一个容器，所有的 Dockerfile 命令格式都是：**INSTRUCTION arguments**

#### 基本指令说明

**FROM命令**
格式：FROM <image> 或 FROM <image>:<tag>
功能：指定基本镜像，是所有Dockerfile文件的第一个命令

**RUN命令**
格式：RUN <command> 或 RUN ["executable", "param1", "param2" ... ]
功能：在镜像中执行命令并提交结果

**注释**
使用#注释

**MAINTAINER命令**
格式：MAINTAINER <name>
功能：指定维护者信息

**ENTRYPOINT命令**
格式：ENTRYPOINT cmd param1 param2 ... 或 ENTRYPOINT ["cmd", "param1", "param2"...]
功能：设置容器启动时执行命令

**USER命令**
格式：USER name
功能：指定运行用户

**EXPOSE命令**
格式：EXPOSE <port> [<port>...]
功能：开放端口

**ENV命令**
格式：ENV <key> <value>
功能：设置环境变量

**ADD命令**
格式：ADD <src> <dst>
功能：复制文件到容器

**VOLUME命令**
格式：VOLUME ["<mountpoint>"]
功能：创建挂载点

**WORKDIR命令**
格式：workdir <path>
功能：设置工作路径

**CMD命令**
格式：CMD ["executable","param1","param2"] 等
功能：指定容器启动默认命令

**ONBUILD命令**
格式：ONBUILD [其他指令]
功能：延迟执行的构建指令

#### 示例Dockerfile
```bash
FROM busybox
ENV  http_proxy http://192.168.0.226:3128
ENV  https_proxy https://192.168.0.226:3128
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd
EXPOSE 22
ENTRYPOINT /usr/sbin/sshd -D
```