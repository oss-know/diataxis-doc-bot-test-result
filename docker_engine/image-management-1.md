# 镜像管理

- [镜像管理](#镜像管理)
    - [创建镜像](#创建镜像)
    - [查看镜像](#查看镜像)
    - [删除镜像](#删除镜像)

## 创建镜像

docker pull、docker build、docker commit、docker import、docker load都可以创建一个新的镜像，关于这些命令的使用详见命令行参考镜像管理。

### 注意事项

1. 避免并发docker load和docker rmi操作。 如果同时满足如下两个条件，可能导致并发性问题：

    - 某个镜像存在于系统中。
    - 同时对该镜像进行docker rmi和docker load操作。

    所以使用时应该避免这种场景（注：所有的镜像创建操作如tag，build，load和rmi并发都有可能会导致类似的错误，应该尽量避免这类操作与rmi的并发）。

2. 如果Docker操作镜像时系统掉电，可能导致镜像损坏，需要手动恢复。

    由于Docker在操作镜像（pull/load/rmi/build/combine/commit/import等）时,镜像数据的操作是异步的、镜像元数据是同步的。所以如果在镜像数据未全部刷到磁盘时掉电，可能导致镜像数据和元数据不一致。对用户的表现是镜像可以看到\(有可能是none 镜像\)，但是无法启动容器，或者启动后的容器有异常。这种情况下应该先使用docker rmi删除该镜像，然后重新进行之前的操作，系统可以恢复。

3. 生产环境节点应避免存留超大数量镜像，请及时清理不使用的镜像。

    镜像数目过多会导致docker image等命令执行过慢，从而导致docker build/docker commit等相关命令执行失败，并可能导致内存堆积。在生产环境中，请及时清理不再使用的镜像和中间过程镜像。

4. 使用\--no-parent参数build镜像时，如果有多个build操作同时进行，并且Dockerfile里 FROM的镜像相同，则可能会残留镜像，分为以下两种情况：
    - FROM的镜像不是完整镜像，则有可能会残留FROM的镜像运行时生成的镜像。残留的镜像名类似base\_v1.0.0-app\_v2.0.0，或者残留<none\>镜像。
    - 如果Dockerfile里的前几条指令相同，则有可能会残留<none\>镜像。

### 可能会产生none镜像场景

1. none镜像是指没有tag的最顶层镜像，比如ubuntu的imageID，只有一个tag是ubuntu，如果这个tag没了，但是imageID还在，那么这个imageID就变成了none镜像。
2. Save镜像的过程中因为要把镜像的数据导出来，所以对image进行保护，但是如果这个时候来一个删除操作，可能会untag成功，删除镜像ID失败，造成该镜像变成none镜像。
3. 执行docker pull时掉电，或者系统panic，可能出现none镜像，为保证镜像完整性，此时可通过docker rmi 删除镜像后重新拉取。
4. 执行docker save保存镜像时，如果指定的名字为镜像ID，则load后的镜像也没有tag，其镜像名为none。

### build镜像的同时删除该镜像，有极低概率导致镜像build失败

目前的build镜像的过程是通过引用计数来保护的，当build完一个镜像后，紧接着就给该镜像的引用计数加1（holdon操作），一旦holdon操作成功，该镜像就不会被删除了，但是在holdon之前，有极低的概率，还是可以删除成功，导致build镜像失败。

## 查看镜像

查看本地镜像列表：

```bash
docker images
```

## 删除镜像

删除镜像（image处为具体镜像名）：

```bash
docker rmi image
```

### 注意事项

禁止使用docker rmi -f XXX删除镜像。如果使用强制删除，docker rmi会忽略过程中的错误，可能导致容器或者镜像元数据残留。如果使用普通删除，如果删除过程出错，则会删除失败，不会导致元数据残留。
