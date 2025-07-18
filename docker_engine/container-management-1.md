# 容器管理

- [容器管理](#容器管理)
    - [创建容器](#创建容器)
    - [创建容器使用hook-spec](#创建容器使用hook-spec)
    - [创建容器配置健康检查](#创建容器配置健康检查)
    - [停止与删除容器](#停止与删除容器)
    - [容器信息查询](#容器信息查询)
    - [修改操作](#修改操作)

## 创建容器

### 下载镜像

运行docker命令需要root权限，当你使用普通用户登录时，需要用sudo权限执行docker命令。

```bash
[root@localhost ~]# docker pull busybox
```

该命令行将在docker官方的镜像库中下载busybox:latest（命令行中没指定TAG，所以使用默认的TAG名latest），镜像在下载过程中将检测所依赖的层本地是否存在，如果存在就跳过。从私有镜像库下载镜像时，请带上registry描述，例如：假如建立了一个私有镜像库，地址为192.168.1.110:5000，里面有一些常用镜像。使用下面命令行从私有镜像库中下载镜像。

```bash
[root@localhost ~]# docker pull 192.168.1.110:5000/busybox
```

从私有镜像库中下载下来的image名字带有镜像库地址的信息名字比较长，可以用docker tag命令生成一个名字简单点的image。

```bash
[root@localhost ~]# docker tag 192.168.1.110:5000/busybox busybox
```

可以通过docker images命令查看本地镜像列表。

### 运行一个简单的应用

```bash
[root@localhost ~]# docker run busybox /bin/echo "Hello world"
Hello world
```

该命令行使用busybox:latest（命令行中没有指定tag，所以使用默认的tag名latest）镜像创建了一个容器，在容器内执行了echo "Hello world"。使用下面命令行可以查看刚才创建的这个容器。

```bash
[root@localhost ~]# docker ps -l
CONTAINER ID        IMAGE               COMMAND                   CREATED             STATUS                     PORTS               NAMES
d8c0a3315bc0        busybox "/bin/echo 'Hello wo…"   5 seconds ago       Exited (0) 3 seconds ago                       practical_franklin
```

### 创建一个交互式的容器

```bash
[root@localhost ~]# docker run -it busybox /bin/bash
root@bf22919af2cf:/# ls 
bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var 
root@bf22919af2cf:/# pwd 
/
```

-ti选项分配一个伪终端给容器并可以使用STDIN进行交互，可以看到这时可以在容器内执行一些命令。这时的容器看起来完全是一个独立的linux虚拟机。使用exit命令退出容器。

### 后台运行容器

执行下面命令行，-d指示这个容器在后台运行，\--name=container1 指定容器的名字为container1。

```bash
[root@localhost ~]# docker run -d --name=container1 busybox /bin/sh -c "while true;do echo hello world;sleep 1;done"
7804d3e16d69b41aac5f9bf20d5f263e2da081b1de50044105b1e3f536b6db1c
```

命令行的执行结果是返回了这个容器的ID，没有返回命令的执行结果hello world，此时容器在后台运行，可以用docker ps命令查看正在运行的容器:

```bash
[root@localhost ~]# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
7804d3e16d69        busybox "/bin/sh -c 'while tr"   11 seconds ago      Up 10 seconds                           container1
```

用docker logs查看容器运行的输出：

```bash
[root@localhost ~]# docker logs container1
hello world
hello world
hello world
...
```

### 容器网络连接

默认情况下，容器可以访问外部网络，而外部网络访问容器时需要通过端口映射，下面以在docker中运行私有镜像库服务registry为例。下面的命令行中-P使registry镜像中开放的端口暴露给主机。

```bash
[root@localhost ~]# docker run --name=container_registry -d -P registry 
cb883f6216c2b08a8c439b3957fb396c847a99079448ca741cc90724de4e4731 
```

container\_registry这个容器已经启动了，但是并不知道容器中的服务映射到主机的哪个端口，通过docker port查看端口映射。

```bash
[root@localhost ~]# docker port container_registry 
5000/tcp -> 0.0.0.0:49155 
```

从输出可以看出，容器内的5000端口映射到了主机的49155端口。通过主机IP:49155就可以访问registry服务了，在浏览器中输入<http://localhost:49155>就可以返回registry的版本信息。

在运行registry镜像的时候还可以直接指定端口映射如：

```bash
docker run --name=container_registry -d -p 5000:5000 registry 
```

通过-p 5000:5000指定容器的5000端口映射到主机的5000端口。

### 注意事项

- **启动容器不能单独加-a stdin**

    启动容器时，不能单独加-a stdin，必须要同时加上-a stdout或者-a stderr，否则会导致终端即使在容器退出后也会卡住。

- **避免使用已有容器的长id、短id作为新容器的name**

    创建容器时，避免使用已有容器A的长id或短id作为新容器B的name。若使用容器A的长id作为容器B的name，当使用容器B的name作为指定容器进行操作时，docker匹配到的是容器A。若使用容器A的短id作为容器B的name，当使用容器A的短id作为指定容器进行相关操作时，docker匹配到的是容器B。这是因为，docker在匹配容器时，先精确匹配所有容器的长id。若未匹配成功，再根据container\_name进行精确匹配；若还未匹配成功，直接对容器id进行模糊匹配。

- **使用sh/bash等依赖标准输入输出的容器应该使用\`-ti\`参数，避免出现异常**

    正常情况：不用\`-ti\`参数启动sh/bash等进程容器，容器会马上退出。

    出现这种问题的原因在于，docker会先创建一个匹配用于容器内业务的stdin，在不设置-ti等交互式参数时，docker会在容器启动后关闭该pipe，而业务容器进程sh/bash在检测到stdin被关闭后会直接退出。

    异常情况：如果在上述过程中的特定阶段（关闭该pipe之前）强制杀死docker daemon，会导致该pipe的daemon端没有被及时关闭，这样即使不带\`-ti\`的sh/bash进程也不会退出，导致异常场景，这种容器就需要手动清理。

    Daemon重启后会接管原有的容器stream，而不带\`-ti\`参数的容器可能就无法处理（因为正常情况下这些容器不存在stream需要接管）；真实业务下几乎不存在这种使用方式\(不带 \`-ti\`的sh/bash没有任何作用\)，为了避免这类问题发生，限制交互类容器应该使用 \`-ti\`参数。

- **容器存储卷**

    启动容器时如果通过\`-v\`参数将主机上的文件挂载到容器中，在主机或容器中使用vi或sed命令修改文件可能会使文件inode发生改变，从而导致主机和容器内的文件不同步。容器中挂载文件时应该尽量避免使用这种文件挂载的方式（或不与vi和sed同时使用），也可以通过挂载文件上层目录来避免该问题。在docker挂载卷时“nocopy”选项可以避免将容器内挂载点目录下原有的文件拷贝到主机源目录下，但是这个选项只能在挂载匿名卷时使用，不能在bind mount的场景下使用。

- **避免使用可能会对host造成影响的选项**

    \--privileged 选项会让容器获得所有权限，容器可以做挂载操作和修改/proc、/sys等目录，可能会对host造成影响，普通容器需要避免使用该选项。

    共享host的namespace，比如\--pid host/\--ipc host/\--net host等选项可以让容器跟host共享命名空间，同样会导致容器影响host的结果，需要避免使用。

- **kernel memory cgroup不稳定，禁止使用**

    kernel memory cgroup在小于4.0版本的Linux内核上仍属于实验阶段，运行起来不稳定，虽然Docker的Warning说是小于4.0就可以，但是我们评估认为，kmemcg在高版本内核仍然不稳定，所以不管是低版本还是高版本，均禁止使用。

    当docker run \--kernel-memory时，会产生如下告警：

    ```text
    WARNING: You specified a kernel memory limit on a kernel older than 4.0. Kernel memory limits are experimental on older kernels, it won't work as expected as expected and can cause your system to be unstable.
    ```

- **blkio-weight参数在支持blkio精确控制的内核下不可用**

    \--blkio-weight-device 可以实现容器内更为精确的blkio控制，该控制需要指定磁盘设备，可以通过docker \--blkio-weight-device参数实现。同时在这种内核下docker不再提供\--blkio-weight方式限制容器blkio，使用该参数创建容器将会报错:

    ```text
    docker: Error response from daemon: oci runtime error: container_linux.go:247: starting container process caused "process_linux.go:398: container init caused \"process_linux.go:369: setting cgroup config for ready process caused \\\"blkio.weight not supported, use weight_device instead\\\"\""
    ```

- **使用\--blkio-weight-device需要磁盘支持CFQ调度策略**

    \--blkio-weight-device参数需要磁盘工作于完全公平队列调度（CFQ：Completely Fair Queuing）的策略时才能工作。

    通过查看磁盘scheduler文件（‘/sys/block/\<磁盘>/queue/scheduler’）可以获知磁盘支持的策略以及当前所采用的策略，如查看sda：

    ```bash
    # cat /sys/block/sda/queue/scheduler noop [deadline] cfq 
    ```

    当前sda支持三种调度策略：noop, deadline, cfq，并且正在使用deadline策略。通过echo修改策略为cfq：

    ```bash
    # echo cfq > /sys/block/sda/queue/scheduler
    ```

- **容器基础镜像中systemd使用限制**

    通过基础镜像创建的容器在使用过程中，容器基础镜像中的systemd仅用于系统容器，普通容器不支持使用。

### 并发性能

- docker内部的消息缓冲有一个上限，超过这个上限就会将消息丢弃，因此在并发执行命令时建议不要超过1000条命令，否则有可能会造成docker内部消息丢失，从而造成容器无法启动等严重问题。
- 并发创建容器并对容器执行restart时会偶现“oci runtime error: container init still running”报错，这是因为containerd对事件等待队列进行了性能优化，容器stop过程中执行runc delete，尝试在1s内kill掉容器的init进程，如果1s内init进程还没有被kill掉的话runc会返回该错误。由于containerd的GC（垃圾回收机制）每隔10s会回收之前runc delete的残留资源， 所以并不影响下次对容器的操作，一般出现上述报错的话等待4\~5s之后再次启动容器即可。

### 安全特性解读

1. docker默认的权能配置分析

    原生的docker默认配置如下，默认进程携带的Cap如下:

    ```conf
    "CAP_CHOWN", 
    "CAP_DAC_OVERRIDE", 
    "CAP_FSETID", 
    "CAP_FOWNER", 
    "CAP_MKNOD", 
    "CAP_NET_RAW", 
    "CAP_SETGID", 
    "CAP_SETUID", 
    "CAP_SETFCAP", 
    "CAP_SETPCAP", 
    "CAP_NET_BIND_SERVICE", 
    "CAP_SYS_CHROOT", 
    "CAP_KILL", 
    "CAP_AUDIT_WRITE",
    ```

    默认的seccomp配置是白名单，不在白名单的syscall默认会返回SCMP\_ACT\_ERRNO，根据给docker不同的Cap开放不同的系统调用，不在上面的权限，默认docker都不会给到容器。

2. CAP\_SYS\_MODULE

    CAP\_SYS\_MODULE这个Cap是让容器可以插入或移除ko，增加该Cap可以让容器逃逸，甚至破坏内核。因为容器最大的隔离是Namespace，在ko中只要把他的Namespace指向init\_nsproxy即可。

3. CAP\_SYS\_ADMIN

    sys\_admin权限给容器带来的能力有：

    - 文件系统（mount，umount，quotactl）
    - namespace设置相关的（setns，unshare，clone new namespace）
    - driver ioctl
    - 对pci的控制，pciconfig\_read, pciconfig\_write, pciconfig\_iobase
    - sethostname

4. CAP\_NET\_ADMIN

    容器中有访问网络接口的和sniff网络流量的权限，容器可以获取到所有容器包括host的网络流量，对网络隔离破坏极大。

5. CAP\_DAC\_READ\_SEARCH

    该权限开放了open\_by\_handle\_at和name\_to\_handle\_at两个系统调用，如果host上没有selinux保护，容器中可通过暴力搜索file\_handle结构的inode号，进而可以打开host上的任意文件，影响文件系统的隔离性。

6. CAP\_SYS\_RAWIO

    容器中可对host写入io端口，可造成host内核崩溃。

7. CAP\_SYS\_PTRACE

    容器中有ptrace权限，可对容器的进程进行ptrace调试。现runc已经修补该漏洞，但有些工具比如nsenter和docker-enter并没有改保护，容器中可对这些工具执行的进程进行调试，获取这些工具带入的资源信息（Namespace、fd等），另外， ptrace可以绕过seccomp，极大增加内核攻击面。

8. Docker Cap接口 \--cap-add all

    --cap-add all表示赋予容器所有的权能，包括本节提到的比较危险的权能，使得容器可以逃逸。

9. 不要禁用docker的seccomp特性

    默认的docker有一个seccomp的配置，配置中使用的是白名单，不在配置的sys\_call会被seccomp禁掉，使用接口--security-opt 'seccomp:unconfined'可以禁止使用seccomp特性。如果禁用seccomp或使用自定义seccomp配置但过滤名单不全，都会增加容器对内核的攻击面。

10. 不要配置/sys和/proc目录可写

    /sys和/proc目录包含了linux维护内核参数、设备管理的接口，容器中配置该目录可写可能会导致容器逃逸。

11. Docker开放Cap  \--CAP\_AUDIT\_CONTROL

    容器可以通过控制系统audit系统，并且通过AUDIT\_TTY\_GET/AUDIT\_TTY\_SET等命令可以获取审计系统中记录的tty执行输入记录，包括root密码。

12. CAP\_BLOCK\_SUSPEND和CAP\_WAKE\_ALARM

    容器可拥有阻塞系统挂起\(epoll\)的能力。

13. CAP\_IPC\_LOCK

    容器拥有该权限后，可以突破ulimit中的max locked memory限制，任意mlock超大内存块，造成一定意义的DoS攻击。

14. CAP\_SYS\_LOG

    容器拥有该权限后，可以dmesg读取系统内核日志，突破内核kaslr防护。

15. CAP\_SYS\_NICE

    容器拥有该权限后，可以改变进程的调度策略和优先级，造成一定意义的DoS攻击。

16. CAP\_SYS\_RESOURCE

    容器可以绕过对其的一些资源限制，比如磁盘空间资源限制、keymaps数量限制、pipe-size-max限制等，造成一定意义的DoS攻击。

17. CAP\_SYS\_TIME

    容器可以改变host上的时间。

18. Docker默认Cap风险分析

    Docker默认的Cap，包含了CAP\_SETUID和CAP\_FSETID，如host和容器共享目录，容器可对共享目录的二进制文件进行+s设置，host上的普通用户可使用其进行提权CAP\_AUDIT\_WRITE，容器可以对host写入，容器可以对host写入日志，host需配置日志防爆措施。

19. Docker和host共享namespace参数，比如 \--pid，\--ipc, \--uts

    该参数为容器和host共享namespace空间，容器和host的namespace隔离没有了，容器可对host进行攻击。比如，使用\--pid 和host共享pid namespace，容器中可以看到host上的进程pid号，可以随意杀死host的进程。

20. \--device 把host的敏感目录或者设备，映射到容器中

    Docker管理面有接口可以把host上的目录或者设备映射到容器中，比如\--device，-v等参数，不要把host上的敏感目录或者设备映射到容器中。

## 创建容器使用hook-spec

### 原理及使用场景

docker支持hook的扩展特性，hook应用与底层runc的执行过程中，遵循OCI标准：[https://github.com/opencontainers/runtime-spec/blob/main/config.md\#hooks](#https://github.com/opencontainers/runtime-spec/blob/main/config.md#hooks)  。

hook主要有三种类型：prestart，poststart，poststop。分别作用于容器内用户应用程序启动之前，容器应用程序启动之后，容器应用程序停止之后。

### 接口参考

当前为docker run和create命令增加了参数“--hook-spec”，后面接spec文件的绝对路径，可以指定容器启动时的需要添加的hook，这些hook会自动附加在docker自己动态创建的hook后面（当前docker只有一个libnetwork的prestart hook），随容器的启动/销毁过程执行用户指定的程序。

spec的结构体定义为：

```conf
// Hook specifies a command that is run at a particular event in the lifecycle of a container
type Hook struct{       
               Path    string   `json:"path"`    
               Args    []string `json:"args,omitempty"`    
               Env     []string `json:"env,omitempty"`      
               Timeout *int     `json:"timeout,omitempty"`
}
// Hooks for container setup and teardown
type  Hooks struct{
               // Prestart is a list of hooks to be run before the container process is executed.
               // On Linux, they are run after the container namespaces are created.         
               Prestart []Hook `json:"prestart,omitempty"`
               // Poststart is a list of hooks to be run after the container process is started.         
               Poststart []Hook `json:"poststart,omitempty"`
               // Poststop is a list of hooks to be run after the container process exits.         
               Poststop []Hook `json:"poststop,omitempty"`
}
```

- Spec文件的path、args、env 都是必填信息；
- Timeout选填\(建议配置\)，参数类型为int，不接受浮点数，范围为\[1, 120\]。
- Spec内容应该是json格式的，格式不对会报错，示例参考前面。
- 使用的时候既可以\`docker run \--hook-spec /tmp/hookspec.json xxx\`, 也可以 \`docker create \--hook-spec /tmp/hookspec.json xxx && docker start xxx\`。

### 为容器定制特有的hook

以启动过程中添加一个网卡的过程来说明。下面是相应的hook spec文件内容：

```conf
{
    "prestart": [
         {
             "path": "/var/lib/docker/hooks/network-hook",             
             "args": ["network-hook", "tap0", "myTap"],             
             "env": [],
             "timeout": 5
         }
     ],
     "poststart":[],     
     "poststop":[]
}
```

指定prestart hook增加一个网络hook的执行。路径是/var/lib/docker/hooks/network-hook，args代表程序的参数，第一个参数一般是程序名字，第二个是程序接受的参数。对于network-hook这个hook程序，需要两个参数，第一个是主机上的网卡名字，第二个是在容器内的网卡重命名。

- 注意事项
    1. hook path必须为docker的graph目录（\--graph）下的hooks文件夹下，默认一般为 /var/lib/docker/hooks，可以通过docker info命令查看root路径。

        ```bash
        [root@localhost ~]# docker info 
        ... 
        Docker Root Dir: /var/lib/docker 
        ...
        ```

        这个路径可能会跟随用户手动配置，以及user namespace的使用（daemon --userns-remap）而变化。 path进行软链接解析后，必须以Docker Root Dir/hooks开头（如本例中使用 /var/lib/docker/hooks开头），否则会直接报错。

    2. hooks path必须指定绝对路径，因为这个是由daemon处理，相对路径对daemon无意义。同时绝对路径也更满足安全要求。
    3. hook程序打印到stderr的输出会打印给客户端并对容器的声明周期产生影响（比如启动失败），而输出到stdout的打印信息会被直接忽略。
    4. 严禁在hook里反向调用docker的指令。
    5. 配置的hook执行文件必须要有可执行权限，否则hook执行会报错。
    6. 使用hook时，执行时间应尽量短。如果hook中的prestart时间过长（超过2分钟），则会导致容器启动超时失败，如果hook中的poststop时间过长（超过2分钟），也会导致容器异常。

        目前已知的异常如下：执行docker stop命令停止容器时，2分钟超时执行清理时，由于hook还没执行结束，因此会等待hook执行结束（该过程持有锁），从而导致和该容器相关的操作都会卡住，需要等到hook执行结束才能恢复。另外，由于docker stop命令的2分钟超时处理是异步的过程，因此即使docker stop命令返回了成功，容器的状态也依然是up状态，需要等到hook执行完后状态才会修改为exited。

- 使用建议
    1. 建议配置hook的Timeout超时时间阈值，超时时间最好在5s以内。
    2. 建议不要配置过多hook，每个容器建议prestart、poststart、poststop这三个hook都只配置一个，过多hook会导致启动时间长。
    3. 建议用户识别多个hook之间的依赖关系，如果存在依赖关系，在组合hook配置文件时要根据依赖关系灵活调整顺序，hook的执行顺序是按照配置的spec文件上的先后顺序。

### 多个hook-spec

当有多个hook配置文件，要运行多个hook时，用户必须自己手工将多个hook配置文件组合成一个配置文件，使用\--hook-spec参数指定此合并后的配置文件，方可生效所有的hook；如果配置多个\--hook-spec参数，则只有最后一个生效。

配置举例：

hook1.json内容如下：

```bash
# cat /var/lib/docker/hooks/hookspec.json 
{
    "prestart": [
        {
            "path": "/var/lib/docker/hooks/lxcfs-hook",             
            "args": ["lxcfs-hook", "--log", "/var/log/lxcfs-hook.log"],             
            "env": []
        }
     ],     
     "poststart":[],     
     "poststop":[]
}
```

hook2.json内容如下：

```bash
# cat /etc/isulad-tools/hookspec.json 
{
      "prestart": [
         {
               "path": "/docker-root/hooks/docker-hooks",             
               "args": ["docker-hooks", "--state", "prestart"],             
               "env": []
         }
       ],     
       "poststart":[],     
       "poststop":[
          {
               "path": "/docker-root/hooks/docker-hooks",             
               "args": ["docker-hooks", "--state", "poststop"],             
               "env": []
          }
        ]
}
```

手工合并后的json内容如下：

```conf
{
       "prestart":[
          {
                "path": "/var/lib/docker/hooks/lxcfs-hook",             
                "args": ["lxcfs-hook", "--log", "/var/log/lxcfs-hook.log"],             
                "env": []
           },         
           {
                "path": "/docker-root/hooks/docker-hooks",             
                "args": ["docker-hooks", "--state", "prestart"],             
                "env": []
           }
        ],     
        "poststart":[],     
        "poststop":[
            {
                "path": "/docker-root/hooks/docker-hooks",             
                "args": ["docker-hooks", "--state", "poststop"],             
                "env": []
            }
         ]
}
```

需要注意的是，docker daemon会按照数组顺序依次读取hook配置文件中prestart等action中的hook二进制，进行执行动作。用户需要识别多个hook之间的依赖关系，如果有依赖关系，在组合hook配置文件时要根据依赖关系灵活调整顺序。

### 为所有容器定制默认的hook

Docker daemon同样可以接收--hook-spec的参数，--hook-spec的语义与docker create/run的--hook-spec参数相同，这里不再复述。也可以在/etc/docker/daemon.json里添加hook配置：

```conf
{
     "hook-spec": "/tmp/hookspec.json"
}
```

容器在运行时，会首先执行daemon定义的--hook-spec中指定的hooks，然后再执行每个容器单独定制的hooks。

## 创建容器配置健康检查

Docker提供了用户定义的对容器进行健康检查的功能。在Dockerfile中配置HEALTHCHECK CMD选项，或在容器创建时配置\--health-cmd选项，在容器内部周期性地执行命令，通过命令的返回值来监测容器的健康状态。

### 配置方法

- 在Dockerfile中添加配置，如：

    ```conf
    HEALTHCHECK --interval=5m --timeout=3s --health-exit-on-unhealthy=true \
       CMD curl -f http://localhost/ || exit 1
    ```

    可配置的选项：

    1. --interval=DURATION，默认 30s，相邻两次命令执行的间隔时间。另外，容器启动后，经过interval时间进行第一次检查。
    2. --timeout=DURATION，默认 30s，单次检查命令执行的时间上限，超时则任务命令执行失败。
    3. --start-period=DURATION，默认 0s，容器初始化时间。初始化期间也会执行健康检查，健康检查失败不会计入最大重试次数。但是，如果在初始化期间运行状况检查成功，则认为容器已启动。之后所有连续的检查失败都将计入最大重试次数。
    4. --retries=N，默认 3，健康检查失败最大的重试次数。
    5. --health-exit-on-unhealthy=BOOLEAN，默认false，检测到容器非健康时是否杀死容器
    6. CMD，必选，在容器内执行的命令。返回值为0表示成功，非0表示失败。

        在配置了HEALTHCHECK后创建镜像，HEALTHCHECK相关配置会被写入镜像的配置中。通过docker inspect可以看到。如：

        ```conf
        "Healthcheck": {
            "Test": [
                "CMD-SHELL",
                "/test.sh"
            ]
        },
        ```

- 在容器创建时的配置：

    ```bash
    docker run -itd --health-cmd "curl -f http://localhost/ || exit 1" --health-interval 5m --health-timeout 3s --health-exit-on-unhealthy centos bash
    ```

    可配置的选项：

    1. \--health-cmd，必选，在容器内执行的命令。返回值为0表示成功，非0表示失败。
    2. \--health-interval，默认 30s，最大为int64上限（纳秒）相邻两次命令执行的间隔时间。
    3. \--health-timeout，默认 30s，最大为int64上限（纳秒），单次检查命令执行的时间上限，超时则任务命令执行失败。
    4. \--health-start-period，默认 0s，最大为int64上限（纳秒），容器初始化时间。
    5. \--health-retries，默认 3，最大为int32上限，健康检查失败最大的重试次数。
    6. \--health-exit-on-unhealthy，默认false，检测到容器非健康时是否杀死容器。

        容器启动后，HEALTHCHECK相关配置会被写入容器的配置中。通过docker inspect可以看到。如：

        ```conf
        "Healthcheck": {
            "Test": [
                "CMD-SHELL",
                "/test.sh"
            ]
        },
        ```

### 检查规则

1. 容器启动后，容器状态中显示health:starting。
2. 经过start-period时间后开始，以interval为间隔周期性在容器中执行CMD。即：当一次命令执行完毕后，经过interval时间，执行下一次命令。
3. 若CMD命令在timeout限制的时间内执行完毕，并且返回值为0，则视为一次检查成功，否则视为一次检查失败。检查成功后，容器状态变为health:healthy。
4. 若CMD命令连续retries次检查失败，则容器状态变为health:unhealthy。失败后容器也会继续进行健康检查。
5. 容器状态为health:unhealthy时，任意一次检查成功会使得容器状态变为health:healthy。
6. 设置--health-exit-on-unhealthy的情况下，如果容器因为非被杀死退出（退出返回值137）后，健康检查只有容器在重新启动后才会继续生效。
7. CMD执行完毕或超时时，docker daemon会将这次检查的起始时间、返回值和标准输出记录到容器的配置文件中。最多记录最新的5条数据。此外，容器的配置文件中还存储着健康检查的相关参数。

通过docker ps可以看到容器状态。

```bash
[root@bac shm]# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                         PORTS               NAMES
7de2228674a2        testimg             "bash"              About an hour ago   Up About an hour (unhealthy)                       cocky_davinci
```

运行中的容器的健康检查状态也会被写入容器配置中。通过docker inspect可以看到。

```conf
"Health": {
    "Status": "healthy",
    "FailingStreak": 0,
    "Log": [
        {
            "Start": "2018-03-07T07:44:15.481414707-05:00",
            "End": "2018-03-07T07:44:15.556908311-05:00",
            "ExitCode": 0,
            "Output": ""
        },
        {
            "Start": "2018-03-07T07:44:18.557297462-05:00",
            "End": "2018-03-07T07:44:18.63035891-05:00",
            "ExitCode": 0,
            "Output": ""
        },
        ......
}
```

> [!NOTE]说明
>
> - 容器内健康检查的状态信息最多保存5条。会保存最后得到的5条记录。  
> - 容器内健康检查相关配置同时最多只能有一条生效。Dockerfile中配置的靠后的条目会覆盖靠前的；容器创建时的配置会覆盖镜像中的。  
> - 在Dockerfile中可以通过 HEALTHCHECK NONE来取消引用的镜像中的健康检查配置。在容器运行时可以通过配置--no-healthcheck来取消镜像中的健康检查配置。不允许在启动时同时配置健康检查相关选项与--no-healthcheck选项。  
> - 带有健康检查配置的容器启动后，若docker daemon退出，则健康检查不会执行，一直等待。docker daemon再次启动后，容器健康状态会变为starting。之后检查规则同上。  
> - 构建容器镜像时若健康检查相关参数配置为空，则按照缺省值处理。  
> - 容器启动时若健康检查相关参数配置为0，则按照缺省值处理。  

## 停止与删除容器

用docker stop停止名为container1的容器：

```bash
[root@localhost ~]# docker stop container1
```

也可以用docker kill来杀死容器达到停止容器的目的：

```bash
[root@localhost ~]# docker kill container1
```

当容器停止之后，可以使用docker rm删除容器：

```bash
[root@localhost ~]# docker rm container1
```

当然，使用docker rm -f 强制删除容器也是可以的：

```bash
[root@localhost ~]# docker rm -f container1
```

### 注意事项

- 禁止使用docker rm -f XXX 删除容器。如果使用强制删除，docker rm会忽略过程中的错误，可能导致容器相关元数据残留。如果使用普通删除，如果删除过程出错，则会删除失败，不会导致元数据残留。
- 避免使用docker kill命令。docker kill命令发送相关信号给容器内业务进程，依赖于容器内业务进程对信号的处理策略，可能导致业务进程的信号处理行为与指令的预期不符合的情况。
- docker stop处于restarting状态的容器可能容器不会马上停止。如果一个容器使用了重启规则，当容器处于restarting状态时，docker stop这个容器时有很低的概率会立即返回，容器仍然会在重启规则的作用下再次启动。
- 不能用docker restart重启加了--rm参数的容器。加了--rm参数的容器在退出时，容器会主动删除，如果重启一个加了--rm的参数的容器， 可能会导致一些异常情况，比如启动容器时，同时加了--rm与-ti参数，对容器执行restart操作，可能会概率性卡住无法退出。

### docker stop/restart 指定t参数且t<0时，请确保自己容器的应用会处理stop信号

Stop的原理：（Restart会调用Stop流程）

1. Stop会首先给容器发送Stop 信号（15）
2. 然后等待一定的时间（这个时间就是用户输入的 t）
3. 过了一定时间，如果容器还活着，那么就发送kill信号（9）使容器强制退出

输入参数t（单位s）的含义：

- t<0  :  表示死等，不管多久都等待程序优雅退出，既然用户这么输入了，表示对自己的应用比较放心，认为自己的程序有合理的stop信号的处理机制
- t=0 ： 表示不等，立即发送kill -9 到容器
- t\>0 ： 表示等一定的时间，如果容器还未退出，就发送kill -9 到容器

所以如果用户使用t<0 \(比如t=-1\)，请确保自己容器的应用会正确处理signal 15，如果容器忽略了该信号，会导致docker stop一直卡住。

### 如果容器处于Dead状态，可能底层文件系统处于busy状态，需要手动删除

Docker在执行容器删除时，先停止容器的相关进程，之后将容器状态更改为Dead，最后执行容器rootfs的删除操作。当文件系统或者device mapper处于忙碌状态时，最后一步rootfs的删除会失败。docker ps -a查看会发现容器处于Dead状态。Dead状态的容器不能再次启动，需要等待文件系统不繁忙时，手动再次执行docker rm进行删除。

### 共享pid namespace容器，子容器处于pause状态会使得父容器stop卡住，并影响docker run命令执行

使用--pid参数创建共享pid  namespace的父子容器，在执行docker stop父容器时，如果子容器中有进程无法退出（比如处于D状态、pause状态），会产生父容器docker stop命令等待的情况，需要手动恢复这些进程，才能正常执行命令。

遇到该问题的时候，请对pause状态的容器使用docker  inspect 命令查询 PidMode对应的父容器是否为需要docker stop的容器。如果是该容器，请使用docker  unpause将子容器解除pause状态，指令即可继续执行。

一般来说，导致该类问题的可能原因是容器对应的pid  namespace由于进程残留导致无法被销毁。如果上述方法无法解决问题，可以通过借助linux工具，获取容器内残留进程，确定pid  namespace中进程无法退出的原因，解决后容器就可以退出：

- 获取容器pid  namespace id

    ```bash
    docker inspect --format={{.State.Pid}} CONTAINERID | awk '{print  "/proc/"$1"/ns/pid"}' |xargs readlink
    ```

- 获取该namespace下的线程

    ```bash
     ls -l /proc/*/task/*/ns/pid |grep -F PIDNAMESPACE_ID |awk '{print $9}' |awk -F  \/ '{print $5}'
    ```

## 容器信息查询

在任何情况下，容器的状态都不应该以docker命令执行是否成功返回为判断标准。如想查看容器状态，建议使用：

```bash
docker inspect <NAME|ID>
```

## 修改操作

### docker exec进入容器启动多个进程的注意事项

docker exec进入容器执行的第一个命令为 bash 命令时，当退出 exec 时，要保证在这次exec启动的进程都退出了，再执行exit退出，否则会导致exit退出时终端卡住的情况。如果要在exit退出时，exec中启动的进程仍然在后台保持运行，要在启动进程时加上nohup。

### docker rename和docker stats \<container_name>的使用冲突

如果使用`docker stats <container_name>` 实时监控容器，当使用docker rename重命名容器之后，docker stats中显示的名字将还是原来的名字，不是rename后的名字。

### docker rename操作restarting状态的容器可能会失败

对一个处于restarting状态的容器执行rename操作的时候，docker会同步修改容器网络的相关配置。由于restarting状态的容器可能还未真正启动起来，网络是不存在的，导致rename操作报错sandbox不存在。建议rename只操作非restarting的稳定状态的容器。

### docker cp

1. 使用docker cp向容器中拷贝文件时，docker ps以及所有对这个容器的操作都将等待docker cp结束之后才能进行。
2. 容器以非root用户运行，当使用docker cp命令复制主机上的一个非root权限的文件到容器时，文件在容器中的权限角色会变成root。docker cp与cp命令不同，docker cp会修改复制到容器中文件的uid和gid为root。

### docker login

执行docker login后，会将user/passwd经 aes（256位）加密后保存在/root/.docker/config.json，同时生成  _root_.docker/aeskey\(权限0600\)，用来解密/root/.docker/config.json中的 user/passwd。目前不能定时更新aeskey，只能由用户手动删除aeskey来更新。aeskey更新后，不管是否重启过docker daemon，都需要重新login，才可以push。例如：

```bash
root@hello:~/workspace/dockerfile# docker login 
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one. 
Username: example Password: 
Login Succeeded 
root@hello:~/workspace/dockerfile# docker push example/empty 
The push refers to a repository [docker.io/example/empty] 
547b6288eb33: Layer already exists 
latest: digest: sha256:99d4fb4ce6c6f850f3b39f54f8eca0bbd9e92bd326761a61f106a10454b8900b size: 524 
root@hello:~/workspace/dockerfile# rm /root/.docker/aeskey 
root@hello:~/workspace/dockerfile# docker push example/empty 
WARNING: Error loading config file:/root/.docker/config.json - illegal base64 data at input byte 0 
The push refers to a repository [docker.io/example/empty] 
547b6288eb33: Layer already exists 
errors: 
denied: requested access to the resource is denied 
unauthorized: authentication required 
root@hello:~/workspace/dockerfile# docker login 
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one. 
Username: example 
Password: 
Login Succeeded 
root@hello:~/workspace/dockerfile# docker push example/empty 
The push refers to a repository [docker.io/example/empty] 
547b6288eb33: Layer already exists 
latest: digest: sha256:99d4fb4ce6c6f850f3b39f54f8eca0bbd9e92bd326761a61f106a10454b8900b size: 524
```
