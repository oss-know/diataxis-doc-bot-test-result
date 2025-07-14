# 可拆分成的文档类型

解释、指南、参考

# 修改理由和意见

1. 原文档混合了多种内容类型，需按Diátaxis架构拆分：
   - 配置操作步骤归入指南(How-to guides)
   - 配置参数说明归入参考(Reference)
   - 原理说明归入解释(Explanations)

2. 结构不合理之处：
   - 混合了操作步骤与原理说明
   - 配置参数分散在多个章节
   - 缺乏清晰的跳转链接指引

3. 重组方案：
   - 将具体操作步骤提取为指南
   - 将配置参数表格化归入参考
   - 将原理说明单独作为解释文档
   - 在指南中添加指向参考和解释的跳转链接

# 改进后的结果

## 指南（How-to guides）

### 基本安装配置
#### 配置daemon参数
可以通过在/etc/docker/daemon.json文件中添加配置项自定义配置参数，相关配置项以及如何使用可以通过dockerd --help查看。[配置参数说明](#参考-daemon配置参数)

#### 配置overlay2存储驱动
docker默认为使用overlay2存储驱动，也可以通过如下两种方式显式指定：
- 编辑/etc/docker/daemon.json，通过storage-driver字段显式指定。
- 编辑/etc/sysconfig/docker-storage，通过docker daemon启动参数显式指定。

#### 配置devicemapper存储驱动
用户如果需要使用devicemapper存储驱动，可以通过如下两种方式显式指定：
- 编辑/etc/docker/daemon.json，通过storage-driver字段显式指定。
- 编辑/etc/sysconfig/docker-storage，通过docker daemon启动参数显式指定。

### 强制退出处理
#### 信号量残留处理
排查和清理信号量残留的操作步骤：
1. 查看系统上残留的信号量
2. 查看devicemapper创建的信号量
3. 查看内核信号量设置上限
4. 增加信号量使用上限或手动清理信号量

#### 网卡残留处理
当出现网卡残留时，需要手动清理host上的veth设备。

## 参考（Reference）

### daemon配置参数
| 配置项 | 说明 | 示例值 |
|-------|------|-------|
| debug | 调试模式开关 | true |
| storage-driver | 存储驱动类型 | overlay2 |
| storage-opts | 存储驱动选项 | ["overlay2.override_kernel_check=true"] |

### 存储驱动配置参数
```sh
# daemon.json配置示例
{
    "storage-driver": "overlay2"
}
```

```sh
# docker-storage配置示例
DOCKER_STORAGE_OPTIONS="--storage-driver=overlay2"
```

## 解释（Explanations）

### 安装注意事项
- Docker容器的安装需要使用root权限。
- docker-engine rpm包与containerd rpm包、runc rpm包、podman rpm包不能同时安装。

### daemon运行目录配置
用户需要明白重新指定各种运行目录和文件（包括--graph、--exec-root等），可能会存在目录冲突，或文件属性变换，对应用的正常使用造成影响。

### 存储驱动行为差异
overlay2文件系统相比普通文件系统存在以下行为差异：
- Copy-UP性能问题
- rename目录问题
- Hard link break问题
- st_dev和st_ino变化
- fd变化

### 系统掉电影响
主机意外掉电或系统panic等场景下，可能出现的问题包括：
- 容器状态丢失
- 文件损坏
- 数据库损坏

### 组件关联影响
#### firewalld
firewalld服务启动会清空当前系统的iptables规则，可能导致docker服务插入iptables规则失败。

#### journald
重启systemd-journald后需要重启docker daemon，否则可能导致docker日志无法记录。

#### audit
配置docker的audit会导致严重的效率问题，生产环境中请谨慎使用。