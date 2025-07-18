# 容器引擎

Docker daemon是一个常驻后台的系统进程，docker 子命令执行前先要启动docker  daemon。

如果是通过rpm包或者系统包管理工具安装的，就可以使用systemctl start docker来启动docker daemon。

docker命令支持多个参数选项，对于参数选项有以下约定：

1. 单个字符的选项可以合并在一起，如：

    ```bash
    docker run -t -i busybox /bin/sh
    ```

    可以写成

    ```bash
    docker run -ti busybox /bin/sh
    ```

2. 在命令帮助中看到的如\--icc=true之类的bool命令选项，如果没有使用这个选项，则这个标志位的值就是在命令帮助中看到的缺省值，如果使用了这个选项则这个标志位的值就是命令帮助中看的值的相反值，如果启动docker  daemon没有加上使用\--icc选项，则默认设置了\--icc=true,如果使用了\--icc选项则表示是\--icc=false。
3. 在命令帮助中看到的\--attach=\[\]之类的选项，表示这类的选项可以多次设置，如：

    ```bash
    docker run --attach=stdin --attach=stdout -i -t busybox /bin/sh
    ```

4. 在命令帮助中看到的-a, \--attach=\[\]之类的选项，表示这种选项既可以用-a value指定也可以用\--attach=value指定。如：

    ```bash
    docker run -a stdin --attach=stdout -i -t busybox /bin/sh
    ```

5. \--name=””之类的选项需要的是一个字符串，只能指定一次，-c=0之类的选项需要的是一个整数，只能指定一次。

**表 1**  docker daemon启动时指定参数详解

<a name="zh-cn_topic_0183265947_table1863643514129"></a>
<table><thead align="left"><tr id="zh-cn_topic_0183265947_row124414579341"><th class="cellrowborder" id="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p11442165733413"><a name="zh-cn_topic_0183265947_p11442165733413"></a><a name="zh-cn_topic_0183265947_p11442165733413"></a><strong id="zh-cn_topic_0183265947_b151371713357"><a name="zh-cn_topic_0183265947_b151371713357"></a><a name="zh-cn_topic_0183265947_b151371713357"></a>参数名称</strong></p>
</th>
<th class="cellrowborder" id="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p13443185715341"><a name="zh-cn_topic_0183265947_p13443185715341"></a><a name="zh-cn_topic_0183265947_p13443185715341"></a><strong id="zh-cn_topic_0183265947_b1051681753514"><a name="zh-cn_topic_0183265947_b1051681753514"></a><a name="zh-cn_topic_0183265947_b1051681753514"></a>说明</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0183265947_row9949123519122"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p169501935161210"><a name="zh-cn_topic_0183265947_p169501935161210"></a><a name="zh-cn_topic_0183265947_p169501935161210"></a>--api-cors-header</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p19950535111212"><a name="zh-cn_topic_0183265947_p19950535111212"></a><a name="zh-cn_topic_0183265947_p19950535111212"></a>开放远程API调用的  <a href="https://en.wikipedia.org/wiki/Cross-Origin_Resource_Sharing" rel="noopener noreferrer" target="_blank">CORS 头信息</a>。这个接口开关对想进行二次开发的上层应用提供了支持。为remote API设置CORS头信息。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row19501635111219"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p795053515122"><a name="zh-cn_topic_0183265947_p795053515122"></a><a name="zh-cn_topic_0183265947_p795053515122"></a>--authorization-plugin=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p12950035141214"><a name="zh-cn_topic_0183265947_p12950035141214"></a><a name="zh-cn_topic_0183265947_p12950035141214"></a>指定认证插件。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row159504359128"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p9950113512129"><a name="zh-cn_topic_0183265947_p9950113512129"></a><a name="zh-cn_topic_0183265947_p9950113512129"></a>-b,  --bridge=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1495013521213"><a name="zh-cn_topic_0183265947_p1495013521213"></a><a name="zh-cn_topic_0183265947_p1495013521213"></a>挂载已经存在的网桥设备到  Docker 容器里。注意，使用 <strong id="zh-cn_topic_0183265947_b6950235111213"><a name="zh-cn_topic_0183265947_b6950235111213"></a><a name="zh-cn_topic_0183265947_b6950235111213"></a>none </strong>可以停用容器里的网络。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row1895033520122"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p395043511215"><a name="zh-cn_topic_0183265947_p395043511215"></a><a name="zh-cn_topic_0183265947_p395043511215"></a>--bip=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p4951113551219"><a name="zh-cn_topic_0183265947_p4951113551219"></a><a name="zh-cn_topic_0183265947_p4951113551219"></a>使用  CIDR 地址来设定自动创建的网桥的 IP。注意，此参数和 -b 不能一起使用。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row4951173561216"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p18951183520125"><a name="zh-cn_topic_0183265947_p18951183520125"></a><a name="zh-cn_topic_0183265947_p18951183520125"></a>--cgroup-parent</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p159511535121212"><a name="zh-cn_topic_0183265947_p159511535121212"></a><a name="zh-cn_topic_0183265947_p159511535121212"></a>为所有容器设定cgroup父目录。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row79513355126"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p99521235101219"><a name="zh-cn_topic_0183265947_p99521235101219"></a><a name="zh-cn_topic_0183265947_p99521235101219"></a>--config-file=/etc/docker/daemon.json</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p9952143531216"><a name="zh-cn_topic_0183265947_p9952143531216"></a><a name="zh-cn_topic_0183265947_p9952143531216"></a>启动docker  daemon的配置文件。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row16952235151219"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p995243516124"><a name="zh-cn_topic_0183265947_p995243516124"></a><a name="zh-cn_topic_0183265947_p995243516124"></a>--containerd</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p49521935191219"><a name="zh-cn_topic_0183265947_p49521935191219"></a><a name="zh-cn_topic_0183265947_p49521935191219"></a>指定containerd的socket路径。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row18952133515129"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p895214355129"><a name="zh-cn_topic_0183265947_p895214355129"></a><a name="zh-cn_topic_0183265947_p895214355129"></a>-D,  --debug=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p7953935111210"><a name="zh-cn_topic_0183265947_p7953935111210"></a><a name="zh-cn_topic_0183265947_p7953935111210"></a>开启Debug模式。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row1495343551214"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p1195313513122"><a name="zh-cn_topic_0183265947_p1195313513122"></a><a name="zh-cn_topic_0183265947_p1195313513122"></a>--default-gateway</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p14953163561219"><a name="zh-cn_topic_0183265947_p14953163561219"></a><a name="zh-cn_topic_0183265947_p14953163561219"></a>容器IPv4地址的默认网关。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row59531935111219"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p189531735151218"><a name="zh-cn_topic_0183265947_p189531735151218"></a><a name="zh-cn_topic_0183265947_p189531735151218"></a>--default-gateway-v6</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1595316355122"><a name="zh-cn_topic_0183265947_p1595316355122"></a><a name="zh-cn_topic_0183265947_p1595316355122"></a>容器IPv6地址的默认网关。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row1895363510124"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p13953143517127"><a name="zh-cn_topic_0183265947_p13953143517127"></a><a name="zh-cn_topic_0183265947_p13953143517127"></a>--default-ulimit=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1595316356127"><a name="zh-cn_topic_0183265947_p1595316356127"></a><a name="zh-cn_topic_0183265947_p1595316356127"></a>容器的默认ulimit值。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row39539358124"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p18953193512124"><a name="zh-cn_topic_0183265947_p18953193512124"></a><a name="zh-cn_topic_0183265947_p18953193512124"></a>--disable-legacy-registry</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p895414354120"><a name="zh-cn_topic_0183265947_p895414354120"></a><a name="zh-cn_topic_0183265947_p895414354120"></a>不允许使用原版registry。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row209546350125"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p12954735101214"><a name="zh-cn_topic_0183265947_p12954735101214"></a><a name="zh-cn_topic_0183265947_p12954735101214"></a>--dns=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p199541635171220"><a name="zh-cn_topic_0183265947_p199541635171220"></a><a name="zh-cn_topic_0183265947_p199541635171220"></a>强制容器使用DNS服务器。</p>
<p id="zh-cn_topic_0183265947_p10954135131216"><a name="zh-cn_topic_0183265947_p10954135131216"></a><a name="zh-cn_topic_0183265947_p10954135131216"></a>例如：  --dns 8.8.x.x</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row79544358126"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p11954535131217"><a name="zh-cn_topic_0183265947_p11954535131217"></a><a name="zh-cn_topic_0183265947_p11954535131217"></a>--dns-opt=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1495412354126"><a name="zh-cn_topic_0183265947_p1495412354126"></a><a name="zh-cn_topic_0183265947_p1495412354126"></a>指定使用DNS的选项。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row7954935151219"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p6954535121213"><a name="zh-cn_topic_0183265947_p6954535121213"></a><a name="zh-cn_topic_0183265947_p6954535121213"></a>--dns-search=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1295493518126"><a name="zh-cn_topic_0183265947_p1295493518126"></a><a name="zh-cn_topic_0183265947_p1295493518126"></a>强制容器使用指定的DNS搜索域名。</p>
<p id="zh-cn_topic_0183265947_p119541435131217"><a name="zh-cn_topic_0183265947_p119541435131217"></a><a name="zh-cn_topic_0183265947_p119541435131217"></a>例如：  --dns-search example.com</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row19954135161211"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p12955203591211"><a name="zh-cn_topic_0183265947_p12955203591211"></a><a name="zh-cn_topic_0183265947_p12955203591211"></a>--exec-opt=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p109553351127"><a name="zh-cn_topic_0183265947_p109553351127"></a><a name="zh-cn_topic_0183265947_p109553351127"></a>设置运行时执行选项。</p>
<p id="zh-cn_topic_0183265947_p195563591213"><a name="zh-cn_topic_0183265947_p195563591213"></a><a name="zh-cn_topic_0183265947_p195563591213"></a>例如支持native.umask选项：</p>
<pre class="screen" id="zh-cn_topic_0183265947_screen095543517128"><a name="zh-cn_topic_0183265947_screen095543517128"></a><a name="zh-cn_topic_0183265947_screen095543517128"></a># 启动的容器umask值为0022 --exec-opt native.umask=normal # 启动的容器umask值为0027（缺省值）--exec-opt  native.umask=secure</pre>
<p id="zh-cn_topic_0183265947_p79551235141220"><a name="zh-cn_topic_0183265947_p79551235141220"></a><a name="zh-cn_topic_0183265947_p79551235141220"></a>注意如果docker  create/run也配置了native.umask参数则以docker create/run中的配置为准。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row19955635141215"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p6955535151215"><a name="zh-cn_topic_0183265947_p6955535151215"></a><a name="zh-cn_topic_0183265947_p6955535151215"></a>--exec-root=/var/run/docker</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1195512358122"><a name="zh-cn_topic_0183265947_p1195512358122"></a><a name="zh-cn_topic_0183265947_p1195512358122"></a>指定执行状态文件存放的根目录。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row13955203510128"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p5955133521217"><a name="zh-cn_topic_0183265947_p5955133521217"></a><a name="zh-cn_topic_0183265947_p5955133521217"></a>--fixed-cidr=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p09551356124"><a name="zh-cn_topic_0183265947_p09551356124"></a><a name="zh-cn_topic_0183265947_p09551356124"></a>设定子网固定IP（ex:  10.20.0.0/16），这个子网IP必须属于网桥内的。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row595543551213"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p1195633591220"><a name="zh-cn_topic_0183265947_p1195633591220"></a><a name="zh-cn_topic_0183265947_p1195633591220"></a>--fixed-cidr-v6</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p19956535171218"><a name="zh-cn_topic_0183265947_p19956535171218"></a><a name="zh-cn_topic_0183265947_p19956535171218"></a>同上，使用与IPv6。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row6956835181219"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p39567359128"><a name="zh-cn_topic_0183265947_p39567359128"></a><a name="zh-cn_topic_0183265947_p39567359128"></a>-G,  --group="docker"</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1095673514126"><a name="zh-cn_topic_0183265947_p1095673514126"></a><a name="zh-cn_topic_0183265947_p1095673514126"></a>在后台运行模式下，赋予指定的Group到相应的unix  socket上。注意，当此参数 --group 赋予空字符串时，将去除组信息。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row1395683541211"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p99560354123"><a name="zh-cn_topic_0183265947_p99560354123"></a><a name="zh-cn_topic_0183265947_p99560354123"></a>-g,  --graph="/var/lib/docker"</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p095612351125"><a name="zh-cn_topic_0183265947_p095612351125"></a><a name="zh-cn_topic_0183265947_p095612351125"></a>配置Docker运行时根目录。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row3956735101212"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p15957153516121"><a name="zh-cn_topic_0183265947_p15957153516121"></a><a name="zh-cn_topic_0183265947_p15957153516121"></a>-H,  --host=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p179575358122"><a name="zh-cn_topic_0183265947_p179575358122"></a><a name="zh-cn_topic_0183265947_p179575358122"></a>在后台模式下指定socket绑定，可以绑定一个或多个  tcp://host:port, unix:///path/to/socket, fd://* 或 fd://socketfd。例如：</p>
<p id="zh-cn_topic_0183265947_p395713352128"><a name="zh-cn_topic_0183265947_p395713352128"></a><a name="zh-cn_topic_0183265947_p395713352128"></a>$ dockerd -H tcp://0.0.0.0:2375</p>
<p id="zh-cn_topic_0183265947_p11957153591211"><a name="zh-cn_topic_0183265947_p11957153591211"></a><a name="zh-cn_topic_0183265947_p11957153591211"></a>或者</p>
<p id="zh-cn_topic_0183265947_p59571356125"><a name="zh-cn_topic_0183265947_p59571356125"></a><a name="zh-cn_topic_0183265947_p59571356125"></a>$  export DOCKER_HOST="tcp://0.0.0.0:2375"</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row295710358122"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p89571235131216"><a name="zh-cn_topic_0183265947_p89571235131216"></a><a name="zh-cn_topic_0183265947_p89571235131216"></a>--insecure-registry=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p16957133561214"><a name="zh-cn_topic_0183265947_p16957133561214"></a><a name="zh-cn_topic_0183265947_p16957133561214"></a>指定非安全连接的仓库，docker默认所有的连接都是TLS证书来保证安全的，如果仓库不支持https连接或者证书是docker  daemon不清楚的证书颁发机构颁发的，则启动daemon的时候要指定如--insecure-registry=192.168.1.110:5000，使用私有仓库都要指定。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row12957163519126"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p895715354124"><a name="zh-cn_topic_0183265947_p895715354124"></a><a name="zh-cn_topic_0183265947_p895715354124"></a>--image-layer-check=true</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p109571335151210"><a name="zh-cn_topic_0183265947_p109571335151210"></a><a name="zh-cn_topic_0183265947_p109571335151210"></a>开启镜像层完整性检查功能，设置为true；关闭该功能，设置为false。如果没有该参数，默认为关闭。</p>
<p id="zh-cn_topic_0183265947_p19957535141217"><a name="zh-cn_topic_0183265947_p19957535141217"></a><a name="zh-cn_topic_0183265947_p19957535141217"></a>docker启动时会检查镜像层的完整性，如果镜像层被破坏，则相关的镜像不可用。docker进行镜像完整性校验时，无法校验内容为空的文件和目录，以及链接文件。因此若镜像因掉电导致上述类型文件丢失，docker的镜像数据完整性校验可能无法识别。docker版本变更时需要检查是否支持该参数，如果不支持，需要从配置文件中删除。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row395713516126"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p109581635171218"><a name="zh-cn_topic_0183265947_p109581635171218"></a><a name="zh-cn_topic_0183265947_p109581635171218"></a>--icc=true</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1995893518128"><a name="zh-cn_topic_0183265947_p1995893518128"></a><a name="zh-cn_topic_0183265947_p1995893518128"></a>启用容器间的通信。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row19582358124"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p16958635131216"><a name="zh-cn_topic_0183265947_p16958635131216"></a><a name="zh-cn_topic_0183265947_p16958635131216"></a>--ip="0.0.0.0"</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p4958735121213"><a name="zh-cn_topic_0183265947_p4958735121213"></a><a name="zh-cn_topic_0183265947_p4958735121213"></a>容器绑定端口时使用的默认IP地址。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row1195813517123"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p17958535111213"><a name="zh-cn_topic_0183265947_p17958535111213"></a><a name="zh-cn_topic_0183265947_p17958535111213"></a>--ip-forward=true</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p20958835131214"><a name="zh-cn_topic_0183265947_p20958835131214"></a><a name="zh-cn_topic_0183265947_p20958835131214"></a>启动容器的  net.ipv4.ip_forward。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row1695943591210"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p12959123519128"><a name="zh-cn_topic_0183265947_p12959123519128"></a><a name="zh-cn_topic_0183265947_p12959123519128"></a>--ip-masq=true</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1395912358122"><a name="zh-cn_topic_0183265947_p1395912358122"></a><a name="zh-cn_topic_0183265947_p1395912358122"></a>使能IP伪装。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row139591335131213"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p13959193511129"><a name="zh-cn_topic_0183265947_p13959193511129"></a><a name="zh-cn_topic_0183265947_p13959193511129"></a>--iptables=true</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p49592354129"><a name="zh-cn_topic_0183265947_p49592354129"></a><a name="zh-cn_topic_0183265947_p49592354129"></a>启动Docker容器自定义的iptable规则。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row99591335201211"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p19959173519128"><a name="zh-cn_topic_0183265947_p19959173519128"></a><a name="zh-cn_topic_0183265947_p19959173519128"></a>-l,  --log-level=info</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p39591535151217"><a name="zh-cn_topic_0183265947_p39591535151217"></a><a name="zh-cn_topic_0183265947_p39591535151217"></a>设置日志级别。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row6959435151218"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p10959153513123"><a name="zh-cn_topic_0183265947_p10959153513123"></a><a name="zh-cn_topic_0183265947_p10959153513123"></a>--label=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p395993541212"><a name="zh-cn_topic_0183265947_p395993541212"></a><a name="zh-cn_topic_0183265947_p395993541212"></a>设置daemon标签，以key=value形式设置。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row795923510120"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p6959113519129"><a name="zh-cn_topic_0183265947_p6959113519129"></a><a name="zh-cn_topic_0183265947_p6959113519129"></a>--log-driver=json-file</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1396010353127"><a name="zh-cn_topic_0183265947_p1396010353127"></a><a name="zh-cn_topic_0183265947_p1396010353127"></a>设置容器日志的默认日志驱动。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row7960113512124"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p169601435141212"><a name="zh-cn_topic_0183265947_p169601435141212"></a><a name="zh-cn_topic_0183265947_p169601435141212"></a>--log-opt=map[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p20960735201210"><a name="zh-cn_topic_0183265947_p20960735201210"></a><a name="zh-cn_topic_0183265947_p20960735201210"></a>设置日志驱动参数。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row1796012356127"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p5960193531212"><a name="zh-cn_topic_0183265947_p5960193531212"></a><a name="zh-cn_topic_0183265947_p5960193531212"></a>--mtu=0</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p8960103514124"><a name="zh-cn_topic_0183265947_p8960103514124"></a><a name="zh-cn_topic_0183265947_p8960103514124"></a>设置容器网络的MTU值，如果没有这个参数，选用默认  route MTU，如果没有默认route，就设置成常量值 1500。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row139602035111217"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p159602035161215"><a name="zh-cn_topic_0183265947_p159602035161215"></a><a name="zh-cn_topic_0183265947_p159602035161215"></a>-p,  --pidfile="/var/run/docker.pid"</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p996013591220"><a name="zh-cn_topic_0183265947_p996013591220"></a><a name="zh-cn_topic_0183265947_p996013591220"></a>后台进程PID文件路径。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row996073513129"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p5960163511215"><a name="zh-cn_topic_0183265947_p5960163511215"></a><a name="zh-cn_topic_0183265947_p5960163511215"></a>--raw-logs</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p149606354127"><a name="zh-cn_topic_0183265947_p149606354127"></a><a name="zh-cn_topic_0183265947_p149606354127"></a>带有全部时间戳并不带ANSI颜色方案的日志。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row169602359120"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p896083517128"><a name="zh-cn_topic_0183265947_p896083517128"></a><a name="zh-cn_topic_0183265947_p896083517128"></a>--registry-mirror=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p2960113517121"><a name="zh-cn_topic_0183265947_p2960113517121"></a><a name="zh-cn_topic_0183265947_p2960113517121"></a>指定dockerd优先使用的镜像仓库。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row9960535101215"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p196020352120"><a name="zh-cn_topic_0183265947_p196020352120"></a><a name="zh-cn_topic_0183265947_p196020352120"></a>-s,  --storage-driver=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p13960173521210"><a name="zh-cn_topic_0183265947_p13960173521210"></a><a name="zh-cn_topic_0183265947_p13960173521210"></a>强制容器运行时使用指定的存储驱动</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row12961635181213"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p149612035141215"><a name="zh-cn_topic_0183265947_p149612035141215"></a><a name="zh-cn_topic_0183265947_p149612035141215"></a>--selinux-enabled=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p196112351129"><a name="zh-cn_topic_0183265947_p196112351129"></a><a name="zh-cn_topic_0183265947_p196112351129"></a>启用selinux支持，3.10.0-862.14及以上内核版本不支持--selinux-enabled=true。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row996118350122"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p10961193521219"><a name="zh-cn_topic_0183265947_p10961193521219"></a><a name="zh-cn_topic_0183265947_p10961193521219"></a>--storage-opt=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1396163513121"><a name="zh-cn_topic_0183265947_p1396163513121"></a><a name="zh-cn_topic_0183265947_p1396163513121"></a>配置存储驱动的参数，存储驱动为devicemapper的时候有效（e.g.  dockerd --storage-opt dm.blocksize=512K）。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row5961123510122"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p19611935181214"><a name="zh-cn_topic_0183265947_p19611935181214"></a><a name="zh-cn_topic_0183265947_p19611935181214"></a>--tls=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p09611735161213"><a name="zh-cn_topic_0183265947_p09611735161213"></a><a name="zh-cn_topic_0183265947_p09611735161213"></a>启动TLS认证开关。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row13961183531216"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p3961163581215"><a name="zh-cn_topic_0183265947_p3961163581215"></a><a name="zh-cn_topic_0183265947_p3961163581215"></a>--tlscacert="/root/.docker/ca.pem"</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p4961173514126"><a name="zh-cn_topic_0183265947_p4961173514126"></a><a name="zh-cn_topic_0183265947_p4961173514126"></a>通过CA认证过的certificate文件路径。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row696111359122"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p1796113515120"><a name="zh-cn_topic_0183265947_p1796113515120"></a><a name="zh-cn_topic_0183265947_p1796113515120"></a>--tlscert="/root/.docker/cert.pem"</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p99611357128"><a name="zh-cn_topic_0183265947_p99611357128"></a><a name="zh-cn_topic_0183265947_p99611357128"></a>TLS的certificate文件路径。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row109613356121"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p2096163521211"><a name="zh-cn_topic_0183265947_p2096163521211"></a><a name="zh-cn_topic_0183265947_p2096163521211"></a>--tlskey="/root/.docker/key.pem"</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p196173521218"><a name="zh-cn_topic_0183265947_p196173521218"></a><a name="zh-cn_topic_0183265947_p196173521218"></a>TLS的key文件路径。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row396153517121"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p596263510123"><a name="zh-cn_topic_0183265947_p596263510123"></a><a name="zh-cn_topic_0183265947_p596263510123"></a>--tlsverify=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p199621035151212"><a name="zh-cn_topic_0183265947_p199621035151212"></a><a name="zh-cn_topic_0183265947_p199621035151212"></a>使用TLS并做后台进程与客户端通讯的验证。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row1596223520126"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p69622035141217"><a name="zh-cn_topic_0183265947_p69622035141217"></a><a name="zh-cn_topic_0183265947_p69622035141217"></a>--insecure-skip-verify-enforce</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p19962235141213"><a name="zh-cn_topic_0183265947_p19962235141213"></a><a name="zh-cn_topic_0183265947_p19962235141213"></a>是否强制跳过证书的主机名/域名验证，默认为false（不跳过）。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row1396273591220"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p19962235171211"><a name="zh-cn_topic_0183265947_p19962235171211"></a><a name="zh-cn_topic_0183265947_p19962235171211"></a>--use-decrypted-key=true</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p296263531214"><a name="zh-cn_topic_0183265947_p296263531214"></a><a name="zh-cn_topic_0183265947_p296263531214"></a>指定使用解密私钥。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row15962203541214"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p14962113551211"><a name="zh-cn_topic_0183265947_p14962113551211"></a><a name="zh-cn_topic_0183265947_p14962113551211"></a>--userland-proxy=true</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1896218356123"><a name="zh-cn_topic_0183265947_p1896218356123"></a><a name="zh-cn_topic_0183265947_p1896218356123"></a>容器LO设备使用userland  proxy。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183265947_row199621435121215"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="41.08%"><p id="zh-cn_topic_0183265947_p196203551217"><a name="zh-cn_topic_0183265947_p196203551217"></a><a name="zh-cn_topic_0183265947_p196203551217"></a>--userns-remap</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="58.919999999999995%"><p id="zh-cn_topic_0183265947_p1962163510124"><a name="zh-cn_topic_0183265947_p1962163510124"></a><a name="zh-cn_topic_0183265947_p1962163510124"></a>容器内使用user命名空间的用户映射表。</p>
<div class="note" id="zh-cn_topic_0183265947_note383035019435"><a name="zh-cn_topic_0183265947_note383035019435"></a><a name="zh-cn_topic_0183265947_note383035019435"></a><span class="notetitle"> 说明： </span><div class="notebody"><p id="zh-cn_topic_0183265947_p5962163541216"><a name="zh-cn_topic_0183265947_p5962163541216"></a><a name="zh-cn_topic_0183265947_p5962163541216"></a>当前版本不支持该参数。</p>
</div></div>
</td>
</tr>
</tbody>
</table>
