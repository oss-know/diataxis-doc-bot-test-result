# 安装配置

本章节主要介绍和开源容器Docker安装相关的重要配置。

## 注意事项

- Docker容器的安装需要使用root权限。
- docker-engine rpm包与containerd rpm包、runc rpm包、podman rpm包不能同时安装。因为docker-engine rpm包中已经包含Docker运行所需的所有组件，其中包括containerd、runc、docker二进制，且containerd、runc和podman rpm包也分别提供了对应的二进制，所以重复安装时会出现软件包冲突。

## 基本安装配置

### 配置daemon参数

可以通过在/etc/docker/daemon.json文件中添加配置项自定义配置参数，相关配置项以及如何使用可以通过dockerd --help查看。配置示例如下：

```sh
cat /etc/docker/daemon.json 
{        
    "debug": true,        
    "storage-driver": "overlay2",        
    "storage-opts": ["overlay2.override_kernel_check=true"] 
}
```

### daemon运行目录配置

用户需要明白重新指定各种运行目录和文件（包括--graph、--exec-root等），可能会存在目录冲突，或文件属性变换，对应用的正常使用造成影响。

> [!TIP]须知
>
> 用户指定的目录或文件应为docker专用，避免冲突导致的文件属性变化带来安全问题。  

- 以--graph为例，当我们使用/new/path/作为daemon新的Root Dir时，如果/new/path/下已经存在文件，且目录或文件名与docker需要使用的目录或文件名冲突（例如： containers、hooks、tmp等目录）时，docker可能会更新原有目录或文件的属性，包括属主、权限等为自己的属主和权限。

> [!TIP]须知
>
> 从docker-17.05开始，--graph参数被标记为Deprecated，用新的参数--data-root替代。  

### daemon自带网络配置

- Docker daemon使用--bip参数指定docker0网桥的网段之后，如果在下一次重启的时候去掉--bip参数，docker0网桥会沿用上一次的--bip配置，即使重启之前已经删除docker0网桥。原因是docker会保存网络配置并在下一次重启的时候默认恢复上一次配置。
- Docker network create 并发创建网络的时候，可以创建具有相同名字的两个网络。原因是docker network是通过id来区分的，name只是个便于识别的别名而已，不保证唯一性。
- Docker在桥接bridge网络模式下，Docker容器是通过宿主机上的NAT模式，建立与宿主机之外世界的通信。Docker Daemon在启动一个容器时，每在宿主机上映射一个端口都会启动一个docker-proxy进程来实现访问代理。建议用户在使用这种userland-proxy时，只映射必须的端口，减少docker-proxy进行端口映射所消耗的资源。

### daemon-umask配置

容器主进程和exec进程的默认umask为0022，为了满足安全性需求，避免容器受到攻击，修改runc的实现，将默认umask修改为0027。修改后others群组将无法访问新建文件或目录。

docker启动容器时的默认umask值为0027，可以在dockerd启动时，使用--exec-opt native.umask=normal参数将容器启动时的umask修改为0022。

> [!TIP]须知
>
> 如果docker create/run也配置了native.umask参数，则以docker create/run中的配置为准。  

详细的配置见[docker create](./容器管理-4.md#create)和[docker run](./容器管理-4.md#run)章节的参数说明。

### daemon启动时间

Docker服务由systemd管理，systemd对各个服务的启动时间有限制，如果指定时间内docker服务未能成功启动，则可能由以下原因导致：

- 如果使用devicemapper且为第一次启动，docker daemon需要对该设备做文件系统初始化操作，而该操作会进行大量磁盘IO操作，在磁盘性能不佳或存在大量IO竞争时，很可能会导致docker daemon启动超时。devicemapper设备只需要初始化一次，后续docker daemon启动时不再需要重复初始化。
- 如果当前系统资源占用太高，导致系统卡顿，系统所有的操作都会变慢，也可能会出现docker服务启动超时的情况。
- daemon重启过程中，需要遍历并读取docker工作目录下每一个容器的配置文件、容器init层和可写层的配置，如果当前系统存在过多容器（包含created和exited的容器），并且磁盘读写性能受限，也会出现daemon遍历文件过久导致docker服务启动超时的情况。

出现服务启动超时情况，建议对以下两种情况进行排查调整：

- 容器编排层定期清理不需要的容器，尤其是exited的容器。
- 结合解决方案的性能要求场景，调整编排层的清理周期和docker服务的启动时间。

### 关联组件journald

重启systemd-journald后需要重启docker daemon。journald通过pipe获取docker daemon的日志，如果journald服务重启，会导致该pipe被关闭，docker的日志写入操作便会触发SIGPIPE信号，该错误信号会导致docker daemon crash。由于忽略该信号影响严重，可能导致后续docker daemon的日志无法记录，因此建议用户在重启journald服务或者journald 异常后主动去重启docker daemon，保证docker日志能够被正常记录，避免daemon crash导致的状态异常。

### 关联组件firewalld

需要在重启或拉起firewalld之后重启docker服务，保证docker服务在firewalld之后启动。

- firewalld服务启动会清空当前系统的iptables规则，所以在启动docker daemon过程中，重启firewalld可能会导致docker服务插入iptables规则失败，从而导致docker服务启动失败。
- docker服务启动后重启firewalld服务，或者状态发生了变化（从启动到停止，或者从停止到启动），会导致docker的iptables规则被删除，创建带端口映射的容器失败。

### 关联组件iptables

docker使用--icc=false选项时，可以限制容器之间互通，但若os自带某些规则，可以造成限制容器之间互通失效，例如：

```text
Chain FORWARD (policy ACCEPT 0 packets, 0 bytes) 
... 
0     0 ACCEPT     icmp --  *      *       0.0.0.0/0            0.0.0.0/0 
... 
0     0 DROP       all  --  docker0 docker0  0.0.0.0/0            0.0.0.0/0
...
```

在Chain FORWARD中，DROP上面多出了一条ACCEPT icmp的规则，造成加了--icc=false后，容器之间也能ping通，但容器之间如果使用udp/tcp协议，对端仍然是不可达的。

因此，在容器os中使用docker，如果需要使用--icc=false选项时，建议先在host上清理一下iptables相关的规则。

### 关联组件audit

docker支持配置audit，但不是强制的。例如：

```text
-w /var/lib/docker -k docker 
-w /etc/docker -k docker 
-w /usr/lib/systemd/system/docker.service -k docker 
-w /usr/lib/systemd/system/docker.socket -k docker 
-w /etc/sysconfig/docker -k docker 
-w /usr/bin/docker-containerd -k docker 
-w /usr/bin/docker-runc -k docker 
-w /etc/docker/daemon.json -k docker
```

配置docker的audit，好处在于可以记录更多信息便于审计，但从安全角度来看，它对防攻击并没有实质性的作用。另一方面，audit配置会导致严重的效率问题，可能导致系统卡顿，生产环境中请谨慎使用。

下面以“-w /var/lib/docker -k docker”为例，演示docker audit的配置：

```sh
[root@localhost signal]# cat /etc/audit/rules.d/audit.rules | grep docker -w /var/lib/docker/  -k docker 
[root@localhost signal]# auditctl -R /etc/audit/rules.d/audit.rules | grep docker 
[root@localhost signal]# auditctl -l | grep docker -w /var/lib/docker/ -p rwxa -k docker
```

> [!NOTE]说明
>
> -p \[r|w|x|a\] 和-w一起使用，观察用户对这个目录的读、写、执行或者属性变化（如时间戳变化）。这样的话，在/var/lib/docker目录下的任何文件、目录操作，都会打印日志到audit.log中，从而会有太多的日志往audit.log中记录，会严重地影响auditd， 比如内存、cpu占用等，进而影响os的运行。例如：每次执行"ls /var/lib/docker/containers"都会有类似如下日志记录到/var/log/audit/audit.log中。  

```text
type=SYSCALL msg=audit(1517656451.457:8097): arch=c000003e syscall=257 success=yes exit=3 a0=ffffffffffffff9c a1=1b955b0 a2=90800 a3=0 items=1 ppid=17821 pid=1925 auid=0 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=pts6 ses=4 comm="ls" exe="/usr/bin/ls" subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key="docker"type=CWD msg=audit(1517656451.457:8097):  cwd="/root"type=PATH msg=audit(1517656451.457:8097): item=0 name="/var/lib/docker/containers" inode=1049112 dev=fd:00 mode=040700 ouid=0 ogid=0 rdev=00:00 obj=unconfined_u:object_r:container_var_lib_t:s0 objtype=NORMAL 
```

### 安全配置seccomp

在做容器网络性能测试时发现，Docker相对于原生内核namespace性能有所下降，经分析开启seccomp后，系统调用（如：sendto）不会通过system\_call\_fastpath进行，而是调用tracesys，这会带来性能大幅下降。因此，建议在有高性能要求的业务的容器场景下关闭seccomp，示例如下：

```sh
docker run -itd --security-opt seccomp=unconfined busybox:latest
```

### 禁止修改docker-daemon的私有目录

不允许对Docker用的根目录（默认/var/lib/docker）和运行时目录（默认/run/docker）以及其文件作任何修改，包括在该目录下删除文件，添加文件，对目录或者文件做软/硬链接，修改文件的属性/权限，修改文件的内容等，如果确实需要做修改，后果自负。

### 普通用户大量部署容器场景下的配置注意事项

普通用户在OS主机上能创建的进程数的上限，例如：可以在系统中创建配置文件“/etc/security/limits.d/20-nproc.conf”限制；类似的，普通用户在容器里也能创建的进程数的上限，由容器镜像中“/etc/security/limits.d/20-nproc.conf”文件对应的值决定，如下所示：

```sh
cat /etc/security/limits.conf 
*       soft    nproc   4096
```

当普通用户大量部署容器，导致容器内进程过多资源不够出现报错时，需要把容器镜像“/etc/security/limits.d/20-nproc.conf”文件中如上所示的4096配置值加大。

可配置的最大值请参考内核的最大能力，如下：

```sh
[root@localhost ~]# sysctl -a | grep pid_max 
kernel.pid_max = 32768
```

## 存储驱动配置

本发行版docker支持overlay2和devicemapper两种存储驱动。由于overlay2较devicemapper而言，拥有更好的性能，建议用户在生产环境中优先考虑。

### 配置overlay2存储驱动

#### 配置方法

docker默认为使用overlay2存储驱动，也可以通过如下两种方式显式指定。

- 编辑/etc/docker/daemon.json，通过storage-driver字段显式指定。

    ```sh
    cat /etc/docker/daemon.json
    {
        "storage-driver": "overlay2"
    }
    ```

- 编辑/etc/sysconfig/docker-storage，通过docker daemon启动参数显式指定。

    ```sh
    cat /etc/sysconfig/docker-storage 
    DOCKER_STORAGE_OPTIONS="--storage-driver=overlay2"
    ```

#### 注意事项

- 部分容器生命周期管理的操作会报找不到相应的rootfs或者相关的可执行文件。
- 如果容器的健康检查配置的是执行容器内的可执行文件，也会报错，导致容器的健康检查失败。

- 如果将overlay2作为graphdriver，在容器中第一次修改镜像中的文件时，若该文件的大小大于系统剩余的空间，修改将会失败。因为即使修改很小，也要把这个文件完整的拷贝到上层，剩余空间不足导致失败。
- overlay2文件系统相比普通文件系统天然存在一些行为差异，归纳如下：
    - 内核版本

        overlay2只兼容原生4.0以上内核，建议配合使用ext4文件系统。

    - Copy-UP性能问题

        修改lower层文件会触发文件复制到upper层，其中数据块复制和fsync比较耗时。

    - rename目录问题
        - 只有源路径和目标路径都在merged层时，才允许rename系统调用，否则rename系统调用会报错-EXDEV。
        - 内核4.10引入了redirect dir特性来修复rename问题，对应内核选项为CONFIG\_OVERLAY\_FS\_REDIRECT\_DIR。

            在使用overlay2场景下，对文件系统目录进行重命名时，如果系统配置文件/sys/module/overlay/parameters/redirect\_dir中配置的特性开关为关闭状态，则会导致使用失败；如果用户要使用相关特性，需要用户手动设置/sys/module/overlay/parameters/redirect\_dir为“Y”。

    - Hard link break问题
        - 当lower层目录中有多个硬链接，在merged层写入数据会触发Copy-UP，导致硬链接断开。
        - 内核4.13引入了index feature来修复这个问题，对应内核选项为 CONFIG\_OVERLAY\_FS\_INDEX。注意这个选项没有前向兼容性，不支持热升级。

    - st\_dev和st\_ino变化

        触发Copy-UP之后，用户只能看到merged层中的新文件，inode会变化。虽然attr和xattr可以复制，但st\_dev和st\_ino具有唯一性，不可复制。这会导致stat和ls查看 到相应的变化。

    - fd变化

        Copy-UP之前，以只读模式打开文件得到描述符fd1，Copy-UP之后，打开同名文件得到文件描述符fd2， 二者实际指向不同的文件。向fd2写入的数据不会在fd1中体现。

#### 异常场景

容器使用配置了overlay2存储驱动的过程中，可能出现挂载点被覆盖的异常情况。例如

#### 异常场景-挂载点被覆盖

挂载关系：在问题容器的挂载点的下面，存在一个/var/lib/docker/overlay2的挂载点：

```sh
[root@localhost ~]# mount -l | grep overlay 
overlay on /var/lib/docker/overlay2/844fd3bca8e616572935808061f009d106a8748dfd29a0a4025645457fa21785/merged type overlay (rw,relatime,seclabel,lowerdir=/var/lib/docker/overlay2/l/JL5PZQLNDCIBU3ZOG3LPPDBHIJ:/var/lib/docker/overlay2/l/ELRPYU4JJG4FDPRLZJCZZE4UO6,upperdir=/var/lib/docker/overlay2/844fd3bca8e616572935808061f009d106a8748dfd29a0a4025645457fa21785/diff,workdir=/var/lib/docker/overlay2/844fd3bca8e616572935808061f009d106a8748dfd29a0a4025645457fa21785/work) 
/dev/mapper/dm-root on /var/lib/docker/overlay2 type ext4 (rw,relatime,seclabel,data=ordered)
```

执行部分docker命令会遇到错误，比如：

```sh
[root@localhost ~]# docker rm 1348136d32
docker rm: Error response from daemon: driver "overlay2" failed to remove root filesystem for 1348136d32: error while removing /var/lib/docker/overlay2/844fd3bca8e616572935808061f009d106a8748dfd29a0a4025645457fa21785: invalid argument
```

此时，在主机侧可以发现对应容器的rootfs找不到，但这并不意味着rootfs丢失，只是被/var/lib/docker/overlay2挂载点覆盖，业务仍然可以正常运行，不受影响。修复方案可以参考如下：

- 修复方案一
    1. 确定当前docker所使用graphdriver：

        ```sh
        docker info | grep "Storage Driver"
        ```

    2. 查询当前的挂载点：

        ```text
        Devicemapper: mount -l | grep devicemapper 
        Overlay2: mount -l | grep overlay2
        ```

        输出格式为： A on B type C \(D\)

        其中，A：块设备名称或overlay，B：挂载点，C：文件系统类型，D：挂载属性。

    3. 从下往上逐一umount这些挂载点B。
    4. 然后全部docker restart这些容器，或者删除所有容器。
    5. 重启docker。

        ```sh
        systemctl restart docker
        ```

- 修复方案二
    1. 业务迁移
    2. 节点重启

### 配置devicemapper存储驱动

用户如果需要使用devicemapper存储驱动，可以通过如下两种方式显式指定。

- 编辑/etc/docker/daemon.json，通过storage-driver字段显式指定。

    ```sh
    cat /etc/docker/daemon.json
    {
        "storage-driver": "devicemapper"
    }
    ```

- 编辑/etc/sysconfig/docker-storage，通过docker daemon启动参数显式指定。

    ```sh
    cat /etc/sysconfig/docker-storage 
    DOCKER_STORAGE_OPTIONS="--storage-driver=devicemapper"
    ```

#### 注意事项

- 使用devicemapper必须使用devicemapper+direct-lvm的方式，配置的方法可以参考<http://docs.docker.com/engine/storage/drivers/device-mapper-driver#configure-direct-lvm-mode-for-production>
- 配置devicemapper时，如果系统上没有足够的空间给thinpool做自动扩容，请禁止自动扩容功能。
- 禁止把/etc/lvm/profile/docker-thinpool.profile中如下两个值都改成100。

    ```text
    activation {   
      thin_pool_autoextend_threshold=80   
      thin_pool_autoextend_percent=20 
    }
    ```

- 使用devicemapper时推荐加上--storage-opt dm.use\_deferred\_deletion=true --storage-opt dm.use\_deferred\_removal=true。
- 使用devicemapper时，容器文件系统推荐使用ext4，需要在docker daemon的配置参数中加 上--storage-opt dm.fs=ext4。
- 当graphdriver为devicemapper时，如果metadata文件损坏且不可恢复，需要人工介入恢复。禁止直接操作或篡改daemon存储devicemapper的元数据。
- 使用devicemapper lvm时，异常掉电导致的devicemapper thinpool损坏，无法保证thinpool损坏后可以修复，也不能保证数据的完整性，需重建thinpool。

docker daemon开启了user namespace特性，切换devicemapper存储池时的**注意事项**

- 一般启动容器时，deviceset-metadata文件为：/var/lib/docker/devicemapper/metadata/deviceset-metadata。
- 使用了user namespace场景下，deviceset-metadata文件使用的是：/var/lib/docker/\{userNSUID.GID\}/devicemapper/metadata/deviceset-metadata。
- 使用devicemapper存储驱动，容器在user namespace场景和普通场景之间切换时，需要将对应deviceset-metadata文件中的BaseDeviceUUID内容清空；针对thinpool扩容或者重建的场景下，也同样的需要将对应deviceset-metadata文件中的BaseDeviceUUID内容清空，否则docker服务会重启失败。

## 强制退出docker相关后台进程的影响

### 信号量残留

使用devicemapper作为graphdriver时，强制退出强制退出可能导致信号量残留。docker在操作dm的过程中会创建信号量，如果在释放信号量前，daemon被强制退出，可能导致该信号量无法释放，一次强制退出最多泄露一个信号量，泄露概率低。而linux系统有信号量上限限制，当信号量泄露次数达到上限值时将无法创建新的信号量，进而导致docker daemon启动失败。排查方法如下：

1. 首先查看系统上残留的信号量

    ```sh
    $ ipcs 
    ------ Message Queues -------- 
    key        msqid      owner      perms      used-bytes   messages 
    ------ Shared Memory Segments -------- 
    key        shmid      owner      perms      bytes      nattch     status 
    ------ Semaphore Arrays -------- 
    key        semid      owner      perms      nsems 
    0x0d4d3358 238977024  root       600        1 
    0x0d4d0ec9 270172161  root       600        1 
    0x0d4dc02e 281640962  root       600        1
    ```

2. 接着用dmsetup查看devicemapper创建的信号量，该信号量集合是上一步中查看到的系统信号量的子集

    ```sh
    dmsetup udevcookies 
    ```

3. 最后查看内核信号量设置上限，第四个值就是当前系统的信号量使用上限

    ```sh
    # cat /proc/sys/kernel/sem 
    250     32000   32      128
    ```

    如果步骤1中残留的信号量数量与步骤3中看到的信号量上限相等，则是达到上限，此时docker daemon无法正常启动。可以使用下述命令增加信号量使用上限值来让docker恢复启动

    ```sh
    echo 250 32000  32  1024 > /proc/sys/kernel/sem
    ```

    也可以手动清理devicemapper残留的信号量（下面是清理一分钟以前申请的dm相关信号量）

    ```sh
    # dmsetup udevcomplete_all 1 
    This operation will destroy all semaphores older than 1 minutes with keys that have a prefix 3405 (0xd4d). 
    Do you really want to continue? [y/n]: y 
    0 semaphores with keys prefixed by 3405 (0xd4d) destroyed. 0 skipped.
    ```

### 网卡残留

使用bridge模式启动容器的过程中，强制退出daemon可能导致网卡残留。使用bridge网络模式，当docker创建容器时，会先在host上创建一对veth，然后再把该网卡信息存到数据库中，如果在创建完成，存到docker的数据库之前，daemon被强制退出，那么该网卡无法被docker关联，下次启动也无法删除（docker本身会清理自己数据库中不用的网卡），从而造成网卡残留。

### 重启容器失败

容器hook耗时较长，且启动阶段遇到containerd被强制退出，再次执行容器start操作可能失败。容器启动阶段遇到containerd被强制退出，docker start操作直接返回错误；containerd被重新拉起后，上次启动可能仍处于runc create执行阶段（执行用户自定义hook，可能耗时较长），此时再次下发docker start命令启动该容器，可能提示以下错误：

```text
Error response from daemon: oci runtime error: container with id exists: xxxxxx
```

该错误是由runc create一个已经存在（创建中）的容器导致，等第一次start对应的runc操作结束后再次执行docker start便可以成功。

由于hook的执行不受docker控制，这种场景下尝试回收该容器有可能导致containerd进程启动卡死（执行未知hook程序），且问题的风险可控（短期影响当前容器的创建）：

- 问题出现后等待第一次操作结束可以再次成功启动该容器。
- 一般是在容器启动失败后创建新的容器，不复用已经失败的容器。

综上，该问题暂时作为场景约束。

### 服务无法正常重启

短时间内频繁重启docker服务导致该服务无法正常重启。docker系统服务由systemd负责监控，如果docker服务在10s内重启次数超过5次，systemd服务就会监控到该异常行为，因此会禁止docker服务启动。只有等到下一个10s周期开始后，docker服务才能响应重启命令正常重启。

## 系统掉电影响

主机意外掉电或系统panic等场景下，由于docker daemon的状态无法及时刷新到磁盘，导致重启后docker daemon状态不正常，可能出现的问题有（包括但不限于）：

- 掉电前创建的容器，重启后docker ps -a看不到，该问题是因为该容器的状态文件没有刷新到磁盘，从而导致重启后daemon无法获取到该容器的状态（镜像、卷、网络等也可能会有类似问题）。
- 掉电前某个文件正处于写入状态，尚未完全写入，重启后daemon重新加载该文件发现文件格式不正常或内容不完整，导致重启加载出错。
- 针对掉电时会破坏docker DB的情况，在重启节点时会清理data-root下面的db文件。因此重启前创建的如下信息在重启后会被删除：
    - network，用docker network创建的资源会在重启后清除。
    - volume，用 docker volume创建的资源会在重启后删除。
    - 构建缓存，构建缓存信息会在重启后删除。
    - containerd保存的元数据，由于启动容器会重建containerd元数据，重启节点会清理containerd中保存的元数据。

        > [!NOTE]说明   
        >
        > 用户若选择采用手动清理恢复环境的方式，可通过配置环境变量“DISABLE\_CRASH\_FILES\_DELETE=true”屏蔽daemon掉电重启时db文件清理功能。  
