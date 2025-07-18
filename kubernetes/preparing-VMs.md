# 准备虚拟机

本章介绍使用 virt  manager 安装虚拟机的方法，如果您已经准备好虚拟机，可以跳过本章节。

## 安装依赖工具

安装虚拟机，会依赖相关工具，安装依赖并使能 libvirtd 服务的参考命令如下（如果需要代理，请先配置代理）：

```bash
$ dnf install virt-install virt-manager libvirt-daemon-qemu edk2-aarch64.noarch virt-viewer
$ systemctl start libvirtd
$ systemctl enable libvirtd
```

## 准备虚拟机磁盘文件

```bash
$ dnf install -y qemu-img
$ virsh pool-define-as vmPool --type dir --target /mnt/vm/images/
$ virsh pool-build vmPool
$ virsh pool-start vmPool
$ virsh pool-autostart  vmPool
$ virsh vol-create-as --pool vmPool --name master0.img --capacity 200G --allocation 1G --format qcow2
$ virsh vol-create-as --pool vmPool --name master1.img --capacity 200G --allocation 1G --format qcow2
$ virsh vol-create-as --pool vmPool --name master2.img --capacity 200G --allocation 1G --format qcow2
$ virsh vol-create-as --pool vmPool --name node1.img --capacity 300G --allocation 1G --format qcow2
$ virsh vol-create-as --pool vmPool --name node2.img --capacity 300G --allocation 1G --format qcow2
$ virsh vol-create-as --pool vmPool --name node3.img --capacity 300G --allocation 1G --format qcow2
```

## 打开 VNC 防火墙端口

**方法一**

1. 查询端口

   ```shell
   $ netstat -lntup | grep qemu-kvm
   ```

2. 打开 VNC 的防火墙端口。假设端口从 5900 开始，参考命令如下：

   ```shell
   $ firewall-cmd --zone=public --add-port=5900/tcp
   $ firewall-cmd --zone=public --add-port=5901/tcp
   $ firewall-cmd --zone=public --add-port=5902/tcp
   $ firewall-cmd --zone=public --add-port=5903/tcp
   $ firewall-cmd --zone=public --add-port=5904/tcp
   $ firewall-cmd --zone=public --add-port=5905/tcp
   ```

**方法二**

直接关闭防火墙 

```shell
$ systemctl stop firewalld
```

## 准备虚拟机配置文件

创建虚拟机需要虚拟机配置文件。假设配置文件为 master.xml ，以虚拟机 hostname 为 k8smaster0 的节点为例，参考配置如下：

```bash
 cat master.xml

<domain type='kvm'>
    <name>k8smaster0</name>
    <memory unit='GiB'>8</memory>
    <vcpu>8</vcpu>
    <os>
 <type arch='aarch64' machine='virt'>hvm</type>
 <loader readonly='yes' type='pflash'>/usr/share/edk2/aarch64/QEMU_EFI-pflash.raw</loader>
 <nvram>/var/lib/libvirt/qemu/nvram/k8smaster0.fd</nvram>
    </os>
    <features>
 <acpi/>
 <gic version='3'/>
    </features>
    <cpu mode='host-passthrough'>
        <topology sockets='2' cores='4' threads='1'/>
    </cpu>
    <iothreads>1</iothreads>
    <clock offset='utc'/>
    <on_poweroff>destroy</on_poweroff>
    <on_reboot>restart</on_reboot>
    <on_crash>restart</on_crash>
    <devices>
 <emulator>/usr/libexec/qemu-kvm</emulator>
 <disk type='file' device='disk'>
     <driver name='qemu' type='qcow2' iothread="1"/>
     <source file='/mnt/vm/images/master0.img'/>
     <target dev='vda' bus='virtio'/>
     <boot order='1'/>
 </disk>
 <disk type='file' device='cdrom'>
     <driver name='qemu' type='raw'/>
     <source file='/mnt/openEuler-21.09-everything-aarch64-dvd.iso'/>
     <readonly/>
     <target dev='sdb' bus='scsi'/>
     <boot order='2'/>
 </disk>
        <interface type='network'>
           <mac address='52:54:00:00:00:80'/>
           <source network='default'/>
           <model type='virtio'/>
        </interface>
 <console type='pty'/>
        <video>
           <model type='virtio'/>
        </video>
        <controller type='scsi' index='0' model='virtio-scsi'/>
 <controller type='usb' model='ehci'/>
 <input type='tablet' bus='usb'/>
 <input type='keyboard' bus='usb'/>
 <graphics type='vnc' listen='0.0.0.0'/>
    </devices>
    <seclabel type='dynamic' model='dac' relabel='yes'/>
</domain>
```

由于虚拟机相关配置必须唯一，新增虚拟机需要适配修改如下内容，保证虚拟机的唯一性：

- name：虚拟机 hostname，建议尽量小写。例中为 `k8smaster0`
- nvram：nvram的句柄文件路径，需要全局唯一。例中为  `/var/lib/libvirt/qemu/nvram/k8smaster0.fd`
- disk 的 source file：虚拟机磁盘文件路径。例中为  `/mnt/vm/images/master0.img`
- interface 的 mac address：interface 的 mac 地址。例中为 `52:54:00:00:00:80`

## 安装虚拟机

1. 创建并启动虚拟机

   ```shell
   $ virsh define master.xml
   $ virsh start k8smaster0
   ```

2. 获取虚拟机的 VNC 端口号

   ```shell
   $ virsh vncdisplay k8smaster0
   ```

3. 使用虚拟机连接工具，例如 VNC Viewer 远程连接虚拟机，并根据提示依次选择配置，完成系统安装

4. 设置虚拟机 hostname，例如设置为 k8smaster0

   ```shell
   $ hostnamectl set-hostname k8smaster0
   ```
