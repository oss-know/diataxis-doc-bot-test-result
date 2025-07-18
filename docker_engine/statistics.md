# 统计信息

## events

用法：**docker events \[OPTIONS\]**

功能：从docker daemon中获取实时事件

选项：

\--since=""         显示指定时间戳之后的事件

\--until=""         显示直到指定时间戳的事件

示例：

该示例中，执行docker events后，用docker run创建并启动一个容器，docker events将输出create事件和start事件。

```sh
$ sudo docker events
2019-08-28T16:23:09.338838795+08:00 container create 53450588a20800d8231aa1dc4439a734e16955387efb5f259c47737dba9e2b5e (image=busybox:latest, name=eager_wu)
2019-08-28T16:23:09.339909205+08:00 container attach 53450588a20800d8231aa1dc4439a734e16955387efb5f259c47737dba9e2b5e (image=busybox:latest, name=eager_wu)
2019-08-28T16:23:09.397717518+08:00 network connect e2e20f52662f1ee2b01545da3b02e5ec7ff9c85adf688dce89a9eb73661dedaa (container=53450588a20800d8231aa1dc4439a734e16955387efb5f259c47737dba9e2b5e, name=bridge, type=bridge)
2019-08-28T16:23:09.922224724+08:00 container start 53450588a20800d8231aa1dc4439a734e16955387efb5f259c47737dba9e2b5e (image=busybox:latest, name=eager_wu)
2019-08-28T16:23:09.924121158+08:00 container resize 53450588a20800d8231aa1dc4439a734e16955387efb5f259c47737dba9e2b5e (height=48, image=busybox:latest, name=eager_wu, width=210)
```

## info

用法：**docker info**

功能：显示docker系统级的相关信息，包括系统中的Container数量、Image数量、Image的存储驱动、容器的执行驱动、内核版本、主机操作系统版本等信息。

选项：无

示例：

```sh
$ sudo docker info
Containers: 4
 Running: 3
 Paused: 0
 Stopped: 1
Images: 45
Server Version: 18.09.0
Storage Driver: devicemapper
 Pool Name: docker-thinpool
 Pool Blocksize: 524.3kB
 Base Device Size: 10.74GB
 Backing Filesystem: ext4
 Udev Sync Supported: true
 Data Space Used: 11GB
 Data Space Total: 51GB
 Data Space Available: 39.99GB
 Metadata Space Used: 5.083MB
 Metadata Space Total: 532.7MB
 Metadata Space Available: 527.6MB
 Thin Pool Minimum Free Space: 5.1GB
 Deferred Removal Enabled: true
 Deferred Deletion Enabled: true
 Deferred Deleted Device Count: 0
......
```

## version

用法：**docker version**

功能：显示docker的版本信息，包括Client版本、Server版本、Go版本、OS/Arch等信息

选项：无

示例：

```sh
$ sudo docker version
Client:
 Version:           18.09.0
 EulerVersion:      18.09.0.48
 API version:       1.39
 Go version:        go1.11
 Git commit:        cbf6283
 Built:             Mon Apr  1 00:00:00 2019
 OS/Arch:           linux/arm64
 Experimental:      false

Server:
 Engine:
  Version:          18.09.0
  EulerVersion:     18.09.0.48
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.11
  Git commit:       cbf6283
  Built:            Mon Apr  1 00:00:00 2019
  OS/Arch:          linux/arm64
  Experimental:     false
```
