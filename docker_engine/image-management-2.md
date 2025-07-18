# 镜像管理

- [镜像管理](#镜像管理)
    - [build](#build)
    - [history](#history)
    - [images](#images)
    - [import](#import)
    - [load](#load)
    - [login](#login)
    - [logout](#logout)
    - [pull](#pull)
    - [push](#push)
    - [rmi](#rmi)
    - [save](#save)
    - [search](#search)
    - [tag](#tag)

## build

用法：**docker build \[OPTIONS\] PATH | URL | -**

功能：使用指定路径中的Dockerfile生成构建一个新的image

选项：常用选项参数如下，更多选项可以查看docker help build

**表 4**  参数说明

<a name="zh-cn_topic_0183243738_table14251918184"></a>
<table><thead align="left"><tr id="zh-cn_topic_0183243738_row172615113189"><th class="cellrowborder" id="mcps1.2.3.1.1" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p3263119181"><a name="zh-cn_topic_0183243738_p3263119181"></a><a name="zh-cn_topic_0183243738_p3263119181"></a>参数</p>
</th>
<th class="cellrowborder" id="mcps1.2.3.1.2" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p162691131813"><a name="zh-cn_topic_0183243738_p162691131813"></a><a name="zh-cn_topic_0183243738_p162691131813"></a>参数含义</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0183243738_row122619121815"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p1526614185"><a name="zh-cn_topic_0183243738_p1526614185"></a><a name="zh-cn_topic_0183243738_p1526614185"></a>--force-rm=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p9803426131816"><a name="zh-cn_topic_0183243738_p9803426131816"></a><a name="zh-cn_topic_0183243738_p9803426131816"></a>即使没有构建成功也删除构建过程中生成的容器</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243738_row660114322184"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p460219324184"><a name="zh-cn_topic_0183243738_p460219324184"></a><a name="zh-cn_topic_0183243738_p460219324184"></a>--no-cache=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p5602163216189"><a name="zh-cn_topic_0183243738_p5602163216189"></a><a name="zh-cn_topic_0183243738_p5602163216189"></a>构建image的过程中不使用缓存</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243738_row9354121121913"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p9354714196"><a name="zh-cn_topic_0183243738_p9354714196"></a><a name="zh-cn_topic_0183243738_p9354714196"></a>-q, --quiet=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p33544151914"><a name="zh-cn_topic_0183243738_p33544151914"></a><a name="zh-cn_topic_0183243738_p33544151914"></a>禁止构建过程中产生的冗余信息</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243738_row37811581916"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p177819158192"><a name="zh-cn_topic_0183243738_p177819158192"></a><a name="zh-cn_topic_0183243738_p177819158192"></a>--rm=true</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p1546216313191"><a name="zh-cn_topic_0183243738_p1546216313191"></a><a name="zh-cn_topic_0183243738_p1546216313191"></a>构建成功后删除过程中生成的容器</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243738_row136272022111912"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p862882217196"><a name="zh-cn_topic_0183243738_p862882217196"></a><a name="zh-cn_topic_0183243738_p862882217196"></a>-t, --tag=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p13391038161911"><a name="zh-cn_topic_0183243738_p13391038161911"></a><a name="zh-cn_topic_0183243738_p13391038161911"></a>指定构建生成的image的tag名</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243738_row7484172061913"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p4485320161916"><a name="zh-cn_topic_0183243738_p4485320161916"></a><a name="zh-cn_topic_0183243738_p4485320161916"></a>--build-arg=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p3485112061914"><a name="zh-cn_topic_0183243738_p3485112061914"></a><a name="zh-cn_topic_0183243738_p3485112061914"></a>设置构建参数</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243738_row3920817171919"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p19920121701910"><a name="zh-cn_topic_0183243738_p19920121701910"></a><a name="zh-cn_topic_0183243738_p19920121701910"></a>--label=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p777151152020"><a name="zh-cn_topic_0183243738_p777151152020"></a><a name="zh-cn_topic_0183243738_p777151152020"></a>镜像相关参数设置，各参数意义与create类似</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243738_row1993117602010"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p18931106112015"><a name="zh-cn_topic_0183243738_p18931106112015"></a><a name="zh-cn_topic_0183243738_p18931106112015"></a>--isolation</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p29312652012"><a name="zh-cn_topic_0183243738_p29312652012"></a><a name="zh-cn_topic_0183243738_p29312652012"></a>指定容器的隔离方法</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243738_row1325154192018"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p825184112011"><a name="zh-cn_topic_0183243738_p825184112011"></a><a name="zh-cn_topic_0183243738_p825184112011"></a>--pull</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="50%"><p id="zh-cn_topic_0183243738_p22517417207"><a name="zh-cn_topic_0183243738_p22517417207"></a><a name="zh-cn_topic_0183243738_p22517417207"></a>构建时总是尝试获取最新版本镜像</p>
</td>
</tr>
</tbody>
</table>

Dockerfile介绍：

Dockerfile是一个镜像的表示，可以通过Dockerfile来描述构建镜像的步骤，并自动构建一个容器，所有的 Dockerfile 命令格式都是：**INSTRUCTION arguments**

**FROM命令**

格式：FROM <image\>   或    FROM <image\>:<tag\>

功能：该命令指定基本镜像，是所有Dockerfile文件的第一个命令，如果没有指定基本镜像的tag，使用默认tag名latest。

**RUN命令**

格式：RUN <command\> \(the command is run in a shell - \`/bin/sh -c\`\) 或者

RUN \["executable", "param1", "param2" ... \]  \(exec form\)

功能：RUN命令会在上面FROM指定的镜像里执行指定的任何命令，然后提交\(commit\)结果，提交的镜像会在后面继续用到。RUN命令等价于:

docker run image command

docker commit container\_id

**注释**

使用\#注释

**MAINTAINER命令**

格式：MAINTAINER <name\>

功能：命令用来指定维护者的姓名和联系方式

**ENTRYPOINT命令**

格式：ENTRYPOINT cmd param1 param2 ...  或者ENTRYPOINT \["cmd", "param1", "param2"...\]

功能：设置在容器启动时执行命令

**USER命令**

格式：USER name

功能：指定 memcached 的运行用户

**EXPOSE命令**

格式：EXPOSE <port\> \[<port\>...\]

功能：开放镜像的一个或多个端口

**ENV命令**

格式：ENV <key\> <value\>

功能：设置环境变量，设置了后，后续的RUN命令都可以使用

**ADD命令**

格式：ADD <src\> <dst\>

功能：从src复制文件到container的dest路径，<src\> 是相对被构建的源目录的相对路径，可以是文件或目录的路径，也可以是一个远程的文件url，<dest\> 是container中的绝对路径

**VOLUME命令**

格式：VOLUME \["<mountpoint\>"\]

功能：创建一个挂载点用于共享目录

**WORKDIR命令**

格式：workdir <path\>

功能：配置RUN, CMD, ENTRYPOINT 命令设置当前工作路径可以设置多次，如果是相对路径，则相对前一个 WORKDIR 命令

**CMD命令**

格式：CMD \["executable","param1","param2"\] \(like an exec, preferred form\)

CMD \["param1","param2"\] \(as default parameters to ENTRYPOINT\)

CMD command param1 param2 \(as a shell\)

功能：一个Dockerfile里只能有一个CMD，如果有多个，只有最后一个生效

**ONBUILD命令**

格式：ONBUILD \[其他指令\]

功能：后面跟其他指令，比如 RUN、COPY 等，这些指令，在当前镜像构建时并不会被执行，只有当以当前镜像为基础镜像，去构建下一级镜像的时候才会被执行

下面是Dockerfile的一个完整例子，该Dockerfile将构建一个安装了sshd服务的image

```bash
FROM busybox
ENV  http_proxy http://192.168.0.226:3128
ENV  https_proxy https://192.168.0.226:3128
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd
EXPOSE 22
ENTRYPOINT /usr/sbin/sshd -D
```

示例：

1. 以上文的Dockerfile构建一个image

    ```bash
    $ sudo docker build -t busybox:latest
    ```

2. 通过以下命令可以看到这个生成的image：

    ```bash
    docker images | grep busybox
    ```

## history

用法：**docker history \[OPTIONS\] IMAGE**

功能：显示一个image的变化历史

选项：

-H, \--human=true

\--no-trunc=false     不对输出进行删减

-q, \--quiet=false     只显示ID

示例：

```bash
$ sudo docker history busybox:test
IMAGE               CREATED             CREATED BY          SIZE                COMMENT
be4672959e8b        15 minutes ago      bash                23B
21970dfada48        4 weeks ago                             128MB               Imported from -
```

## images

用法：**docker images \[OPTIONS\] \[NAME\]**

功能：列出存在的image，不加选项时不显示中间的image

选项：

-a, \--all=false      显示所有的镜像，

-f, \--filter=\[\]       指定一个过滤值\(i.e. 'dangling=true'\)

\--no-trunc=false    不对输出进行删减

-q, \--quiet=false    只显示ID

示例：

```bash
$ sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
busybox             latest              e02e811dd08f        2 years ago         1.09MB
```

## import

用法：**docker import URL|- \[REPOSITORY\[:TAG\]\]**

功能：把包含了一个rootfs的tar包导入为镜像。与docker export相对应。

选项：无

示例：

从上文介绍的docker export命令时导出的busybox.tar用docker import命令生成一个新的image

```bash
$ sudo docker import busybox.tar busybox:test
sha256:a79d8ae1240388fd3f6c49697733c8bac4d87283920defc51fb0fe4469e30a4f
$ sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
busybox             test                a79d8ae12403        2 seconds ago       1.3MB
```

## load

用法：**docker load \[OPTIONS\]**

功能：把docker save出来的tar包重新加载一个镜像。与docker save相对应。

选项：

-i, \--input=""

示例：

```bash
$ sudo docker load -i busybox.tar
Loaded image ID: sha256:e02e811dd08fd49e7f6032625495118e63f597eb150403d02e3238af1df240ba
$ sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
busybox             latest              e02e811dd08f        2 years ago         1.09MB
```

## login

用法：**docker login \[OPTIONS\] \[SERVER\]**

功能：登录到一个镜像服务库，没有指定server时，默认登录到<https://index.docker.io/v1/>

选项：

-e, \--email=""       Email

-p, \--password=""    密码

-u, \--username=""    用户名

示例：

```bash
$ sudo docker login
```

## logout

用法：**docker logout \[SERVER\]**

功能：从一个镜像服务器中登出，没有指定server时，默认登出<https://index.docker.io/v1/>

选项：无

示例：

```bash
$ sudo docker logout
```

## pull

用法：**docker pull \[OPTIONS\] NAME\[:TAG\]**

功能：从一个镜像库（官方的或私有的）中拉取一个镜像

选项：

-a, \--all-tags=false    下载一个镜像仓库的所有镜像（一个镜像仓库可以被打多个标签，比如一个busybox镜像库，可能有多个标签如busybox:14.04,busybox:13.10,busybox:latest等，使用-a选项后，将所有标签的busybox镜像拉取下来）

示例：

1. 从官方镜像库中拉取nginx镜像

    ```bash
    $ sudo docker pull nginx
    Using default tag: latest
    latest: Pulling from official/nginx
    94ed0c431eb5: Pull complete
    9406c100a1c3: Pull complete
    aa74daafd50c: Pull complete
    Digest: sha256:788fa27763db6d69ad3444e8ba72f947df9e7e163bad7c1f5614f8fd27a311c3
    Status: Downloaded newer image for nginx:latest
    ```

    拉取镜像时会检测所依赖的层是否存在，如果存在就用本地的层。

2. 从私有镜像库中拉取镜像

    从私有镜像库中拉取Fedora镜像，比如所使用的私有镜像库的地址是192.168.1.110:5000：

    ```bash
    $ sudo docker pull 192.168.1.110:5000/fedora
    ```

## push

用法：**docker push NAME\[:TAG\]**

功能：将一个image推送到镜像库中

选项：无

示例：

1. 将一个image推送到私有镜像库192.168.1.110:5000中
2. 将要推送的镜像打标签（docker tag命令将在下文介绍），本例中要推送的镜像为busybox:sshd

    ```bash
    $ sudo docker tag ubuntu:sshd 192.168.1.110:5000/busybox:sshd
    ```

3. 将打好标签的镜像推送到私有镜像库中

    ```bash
    $ sudo docker push 192.168.1.110:5000/busybox:sshd
    ```

    推送的时候会自动检测所依赖的层在镜像库中是否已存在，如果以存在，跳过该层。

## rmi

用法：**docker rmi \[OPTIONS\] IMAGE \[IMAGE...\]**

功能：删除一个或多个镜像，如果一个镜像在镜像库中有多个标签，删除镜像的时候只是进行untag操作，当删除的是只有一个标签的镜像时，将依次删除所依赖的层。

选项：

-f, \--force=false    强制删除image

\--no-prune=false    不删除没有标签的父镜像

示例：

```bash
$ sudo docker rmi 192.168.1.110:5000/busybox:sshd
```

## save

用法：**docker save \[OPTIONS\] IMAGE \[IMAGE...\]**

功能：保存一个image到一个tar包，输出默认是到STDOUT

选项：

-o, \--output=""   输出到文件中而不是STDOUT

示例：

```bash
$ sudo docker save -o nginx.tar nginx:latest
$ ls
nginx.tar
```

## search

用法：**docker search \[OPTIONS\] TERM**

功能：在镜像库中查找特定的镜像

选项：

\--automated=false    显示自动构建的image

\--no-trunc=false      不对输出进行删减

-s, \--stars=0         只显示特定星级以上的image

示例：

1. 在官方镜像库中搜寻nginx

    ```bash
    $ sudo docker search nginx
    NAME                              DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
    nginx                             Official build of Nginx.                        11873               [OK]
    jwilder/nginx-proxy               Automated Nginx reverse proxy for docker con…   1645                                    [OK]
    richarvey/nginx-php-fpm           Container running Nginx + PHP-FPM capable of…   739                                     [OK]
    linuxserver/nginx                 An Nginx container, brought to you by LinuxS…   74
    bitnami/nginx                     Bitnami nginx Docker Image                      70                                      [OK]
    tiangolo/nginx-rtmp               Docker image with Nginx using the nginx-rtmp…   51                                      [OK]
    ```

2. 在私有镜像库中搜寻busybox，在私有镜像库中搜寻时要加上私有镜像库的地址

    ```bash
    $ sudo docker search 192.168.1.110:5000/busybox
    ```

## tag

用法：**docker tag \[OPTIONS\] IMAGE\[:TAG\] \[REGISTRYHOST/\]\[USERNAME/\]NAME\[:TAG\]**

功能：将一个镜像打标签到一个库中

选项：

-f, \--force=false    如果存在相同的tag名将强制替换原来的image

示例：

```bash
$ sudo docker tag busybox:latest busybox:test
```
