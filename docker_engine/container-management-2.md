# 容器管理

- [容器管理](#容器管理)
    - [总体说明](#总体说明)
    - [attach](#attach)
    - [commit](#commit)
    - [cp](#cp)
    - [create](#create)
    - [diff](#diff)
    - [exec](#exec)
    - [export](#export)
    - [inspect](#inspect)
    - [logs](#logs)
    - [pause/unpause](#pause-unpause)
    - [port](#port)
    - [ps](#ps)
    - [rename](#rename)
    - [restart](#restart)
    - [rm](#rm)
    - [run](#run)
    - [start](#start)
    - [stats](#stats)
    - [stop](#stop)
    - [top](#top)
    - [update](#update)
    - [wait](#wait)

# 总体说明

当前docker支持的子命令，按照功能划分为以下几组：

<a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_table16458469"></a>
<table><thead align="left"><tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row1183915"><th class="cellrowborder" id="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28788263"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28788263"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28788263"></a><strong id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_b6803444357"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_b6803444357"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_b6803444357"></a>功能划分</strong></p>
</th>
<th class="cellrowborder" colspan="2" id="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p50147992"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p50147992"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p50147992"></a><strong id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_b683194415355"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_b683194415355"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_b683194415355"></a>命令</strong></p>
</th>
<th class="cellrowborder" id="mcps1.1.5.1.3" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35455590"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35455590"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35455590"></a><strong id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_b1384144133513"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_b1384144133513"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_b1384144133513"></a>命令功能</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row50664859"><td class="cellrowborder" headers="mcps1.1.5.1.1" rowspan="2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p10212927"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p10212927"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p10212927"></a>主机环境相关</p>
</td>
<td class="cellrowborder" colspan="2" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21940722"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21940722"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21940722"></a>version</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.3" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p32368095"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p32368095"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p32368095"></a>查看docker版本信息</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row22877402"><td class="cellrowborder" colspan="2" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p41130254"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p41130254"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p41130254"></a>info</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.3" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p43216271"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p43216271"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p43216271"></a>查看docker系统和主机环境信息</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row53402119"><td class="cellrowborder" headers="mcps1.1.5.1.1" rowspan="20" valign="top" width="25%"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30604389"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30604389"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30604389"></a>容器相关</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" rowspan="7" valign="top" width="25%"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p63036484"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p63036484"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p63036484"></a>容器生命周期管理</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top" width="25%"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p5681612"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p5681612"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p5681612"></a>create</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.3" valign="top" width="25%"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p57557412"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p57557412"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p57557412"></a>由image创建一个容器</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row48254661"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p16313497"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p16313497"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p16313497"></a>run</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p46324881"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p46324881"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p46324881"></a>由image创建一个容器并运行</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row14270750"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p15080136"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p15080136"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p15080136"></a>start</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p13531531"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p13531531"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p13531531"></a>开始一个已停止运行的容器</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row54674917"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p66592127"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p66592127"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p66592127"></a>stop</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p25253189"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p25253189"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p25253189"></a>停止一个运行中的容器</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row25952117"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21746729"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21746729"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21746729"></a>restart</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p16654654"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p16654654"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p16654654"></a>重启一个容器</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row45420240"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p55160823"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p55160823"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p55160823"></a>wait</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p38841670"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p38841670"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p38841670"></a>等待一个容器停止，并打印出退出码</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row14030717"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p62746268"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p62746268"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p62746268"></a>rm</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p49282936"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p49282936"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p49282936"></a>删除一个容器</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row40893240"><td class="cellrowborder" headers="mcps1.1.5.1.1" rowspan="4" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p24018105"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p24018105"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p24018105"></a>容器内进程管理</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p66418347"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p66418347"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p66418347"></a>pause</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p11177013"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p11177013"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p11177013"></a>暂停一个容器内的所有进程</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row33484259"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p27870469"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p27870469"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p27870469"></a>unpause</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p42915540"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p42915540"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p42915540"></a>恢复一个容器内被暂停的所用进程</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row50695543"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p12698356"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p12698356"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p12698356"></a>top</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21933905"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21933905"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21933905"></a>查看容器内的进程</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row63187419"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p17907308"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p17907308"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p17907308"></a>exec</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p41205809"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p41205809"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p41205809"></a>在容器内执行进程</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row35307962"><td class="cellrowborder" headers="mcps1.1.5.1.1" rowspan="9" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p41372713"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p41372713"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p41372713"></a>容器检视工具</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p62855489"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p62855489"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p62855489"></a>ps</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p58129833"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p58129833"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p58129833"></a>查看运行中的容器（不加任何选项）</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row53406450"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30955222"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30955222"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30955222"></a>logs</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p24345054"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p24345054"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p24345054"></a>显示一个容器的日志信息</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row17778899"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30804749"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30804749"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30804749"></a>attach</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p12156768"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p12156768"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p12156768"></a>连接到一个容器的标准输入输出</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row42302050"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p3913996"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p3913996"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p3913996"></a>inspect</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p48598242"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p48598242"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p48598242"></a>返回容器的底层信息</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row34731002"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p61747774"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p61747774"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p61747774"></a>port</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35513827"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35513827"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35513827"></a>列出容器与主机的端口映射</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row51188993"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p52667802"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p52667802"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p52667802"></a>diff</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p38233575"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p38233575"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p38233575"></a>返回容器相对于镜像中的rootfs所作的改动</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row8557861"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p22098140"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p22098140"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p22098140"></a>cp</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p45118907"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p45118907"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p45118907"></a>容器与主机之间复制文件</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row3416986"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p8340425"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p8340425"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p8340425"></a>export</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p4485813"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p4485813"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p4485813"></a>将一个容器中的文件系统导出为一个tar包</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row44406948121132"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35936326121132"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35936326121132"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35936326121132"></a>stats</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p25161274121132"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p25161274121132"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p25161274121132"></a>实时查看容器的资源占用情况</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row40372317"><td class="cellrowborder" headers="mcps1.1.5.1.1" rowspan="14" valign="top" width="25%"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p48932206"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p48932206"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p48932206"></a>images相关</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" rowspan="4" valign="top" width="25%"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p4085744"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p4085744"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p4085744"></a>生成一个新image</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top" width="25%"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p62509834"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p62509834"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p62509834"></a>build</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.3" valign="top" width="25%"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30131813"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30131813"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p30131813"></a>通过一个Dockerfile构建一个image</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row2750866"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21493617"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21493617"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p21493617"></a>commit</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p63261412"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p63261412"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p63261412"></a>基于容器的rootfs创建一个新的image</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row32481801"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p13780214"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p13780214"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p13780214"></a>import</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p42455531"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p42455531"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p42455531"></a>将tar包中的内容作为文件系统创建一个image</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row46555465"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p12896286"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p12896286"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p12896286"></a>load</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p37966223"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p37966223"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p37966223"></a>从一个tar包中加载一个image</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row6151694"><td class="cellrowborder" headers="mcps1.1.5.1.1" rowspan="5" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28525238"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28525238"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28525238"></a>与image仓库有关</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28842926"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28842926"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28842926"></a>login</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p54575646"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p54575646"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p54575646"></a>登录一个registry</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row21418771"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p57198891"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p57198891"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p57198891"></a>logout</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p2598608"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p2598608"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p2598608"></a>登出一个registry</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row23387474"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p15337269"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p15337269"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p15337269"></a>pull</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p34359256"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p34359256"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p34359256"></a>从registry中拉取一个image</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row40797849"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p16291455"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p16291455"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p16291455"></a>push</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p44539515"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p44539515"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p44539515"></a>将一个image推送到registry中</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row65311315"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p55725192"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p55725192"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p55725192"></a>search</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p17446726"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p17446726"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p17446726"></a>在registry中搜寻image</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row22802807"><td class="cellrowborder" headers="mcps1.1.5.1.1" rowspan="5" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35088084"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35088084"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p35088084"></a>与image管理有关</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p23562574"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p23562574"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p23562574"></a>images</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p29520332"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p29520332"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p29520332"></a>显示系统中的image</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row64356400"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p45485936"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p45485936"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p45485936"></a>history</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p60482217"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p60482217"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p60482217"></a>显示一个image的变化历史</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row7469042"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p1012626"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p1012626"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p1012626"></a>rmi</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p14913854"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p14913854"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p14913854"></a>删除image</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row6965"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p564191"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p564191"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p564191"></a>tag</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p45699530"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p45699530"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p45699530"></a>给image打标签</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row8642591"><td class="cellrowborder" headers="mcps1.1.5.1.1" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28961294"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28961294"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p28961294"></a>save</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p64163473"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p64163473"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p64163473"></a>将一个image保存到一个tar包中</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row40600350"><td class="cellrowborder" headers="mcps1.1.5.1.1" rowspan="2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p294043"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p294043"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p294043"></a>其他</p>
</td>
<td class="cellrowborder" colspan="2" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p23817504"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p23817504"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p23817504"></a>events</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.3" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p50169686"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p50169686"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p50169686"></a>从docker daemon中获取实时事件</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_row2952396121125"><td class="cellrowborder" colspan="2" headers="mcps1.1.5.1.2" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p5522470121253"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p5522470121253"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p5522470121253"></a>rename</p>
</td>
<td class="cellrowborder" headers="mcps1.1.5.1.3" valign="top"><p id="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p9096874121125"><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p9096874121125"></a><a name="zh-cn_topic_0183243657_zh-cn_topic_0155236992_zh-cn_topic_0076221003_zh-cn_topic_0043209396_p9096874121125"></a>重命名容器</p>
</td>
</tr>
</tbody>
</table>

其中有些子命令还有一些参数选项如docker run,通过docker COMMAND --help可以查看相应COMMAND命令的帮助，命令选项参考上文的命令选项约定。下面详细介绍每个命令的使用。

## attach

用法：**docker attach \[OPTIONS\] CONTAINER**

功能：附加到一个运行着的容器

选项：

\--no-stdin=false    不附加STDIN

\--sig-proxy=true    代理所有到容器内部的信号，不代理SIGCHLD, SIGKILL, SIGSTOP

示例：

```shell
$ sudo docker attach attach_test
root@2988b8658669:/# ls bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

## commit

用法：**docker commit \[OPTIONS\] CONTAINER \[REPOSITORY\[:TAG\]\]**

功能：由一个容器创建一个新的image

选项：

-a, \--author=""    指定作者

-m, \--message=""  提交的信息

-p, \--pause=true   在提交过程中暂停容器

示例：

运行一个容器，然后将这个容器提交成一个新的image

```shell
$ sudo docker commit test busybox:test
sha256:be4672959e8bd8a4291fbdd9e99be932912fe80b062fba3c9b16ee83720c33e1

$ sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
busybox             latest              e02e811dd08f        2 years ago         1.09MB
```

## cp

用法：docker cp \[OPTIONS\] CONTAINER:SRC\_PATH DEST\_PATH|-

docker cp \[OPTIONS\] SRC\_PATH|- CONTAINER:DEST\_PATH

功能：从指定的容器内的一个路径复制文件或文件夹到主机的指定路径中，或者把主机的文件或者文件夹拷贝到容器内。

注意：docker cp不支持容器内/proc，/sys，/dev，/tmp等虚拟文件系统以及用户在容器内自行挂载的文件系统内的文件拷贝。

选项：

-a, \--archive   将拷贝到容器的文件属主设置为容器运行用户（\--user）

-L, \--follow-link   解析并跟踪文件的符号链接

示例：

复制registry容器中/test目录到主机的/home/aaa目录中

```shell
$ sudo docker cp registry:/test /home/aaa
```

## create

用法：**docker create \[OPTIONS\] IMAGE \[COMMAND\] \[ARG...\]**

功能：使用image创建一个新的容器，并将返回一个容器的ID，创建之后的容器用docker start命令启动，OPTIONS用于创建容器时对容器进行配置，有些选项将覆盖image中对容器的配置，COMMAND指定容器启动时执行的命令。

选项：

**表 2**  参数说明

<a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_table1239044502210"></a>
<table><thead align="left"><tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row439004518223"><th class="cellrowborder" id="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19390104532213"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19390104532213"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19390104532213"></a>参数</p>
</th>
<th class="cellrowborder" id="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1039064522216"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1039064522216"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1039064522216"></a>参数含义</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row13390104518221"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p16390174542214"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p16390174542214"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p16390174542214"></a>-a --attach=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1239011453221"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1239011453221"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1239011453221"></a>使控制台Attach到容器内进程的STDIN,STDOUT,STDERR</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row03908454227"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p639018453223"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p639018453223"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p639018453223"></a>--name=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p4391134519226"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p4391134519226"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p4391134519226"></a>指定容器的名字</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row163918452222"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p10391174517228"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p10391174517228"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p10391174517228"></a>--add-host=[host:ip]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p661113016127"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p661113016127"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p661113016127"></a>在容器内的/etc/hosts中添加一个hostname到IP地址的映射</p>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p0783519172414"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p0783519172414"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p0783519172414"></a>e.g. --add-host=test:10.10.10.10</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row10693921155915"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17958540404"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17958540404"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17958540404"></a>--annotation</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p20424151611011"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p20424151611011"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p20424151611011"></a>设置容器的annotations。例如支持native.umask选项：</p>
<pre class="screen" id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_screen188792816013"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_screen188792816013"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_screen188792816013"></a>--annotation native.umask=normal  启动的容器umask值为0022
--annotation native.umask=secure # 启动的容器umask值为0027</pre>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p126931121195914"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p126931121195914"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p126931121195914"></a>注意如果没有配置该参数，则使用dockerd中的umask配置。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row939164522218"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p03911345142218"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p03911345142218"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p03911345142218"></a>--blkio-weight</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1139111453223"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1139111453223"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1139111453223"></a>blockio的相对权重，从10到1000</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1139110458220"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1339110456222"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1339110456222"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1339110456222"></a>--blkio-weight-device=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p5912131582516"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p5912131582516"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p5912131582516"></a>blockio权重（设置相对权重）</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row339184572217"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p83911445172217"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p83911445172217"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p83911445172217"></a>-c, --cpu-shares=0</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3391145132220"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3391145132220"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3391145132220"></a>容器获得主机CPU的相对权重，通过设置这个选项获得更高的优先级，默认所有的容器都是获得相同的CPU优先权。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1639114454221"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p143911545142214"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p143911545142214"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p143911545142214"></a>--cap-add=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p02723315267"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p02723315267"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p02723315267"></a>添加Linux权能</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row16136171852612"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18137121810261"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18137121810261"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18137121810261"></a>--cap-drop=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p7137141892617"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p7137141892617"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p7137141892617"></a>清除Linux权能</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1695452015268"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p13954192022614"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p13954192022614"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p13954192022614"></a>--cgroup-parent</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p729685122617"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p729685122617"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p729685122617"></a>为容器设置cgroup父目录</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1838402332617"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p15384122332619"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p15384122332619"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p15384122332619"></a>--cidfile=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p147641332151417"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p147641332151417"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p147641332151417"></a>将容器的ID写到指定的文件中</p>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p23841223192619"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p23841223192619"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p23841223192619"></a>e.g. --cidfile=/home/cidfile-test 将该容器的ID写入到/home/cidfile-test中</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row8107726122617"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p51070266260"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p51070266260"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p51070266260"></a>--cpu-period</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p6107926132615"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p6107926132615"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p6107926132615"></a>设置CFS（完全公平调度策略）进程的CPU周期。</p>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1869573811136"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1869573811136"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1869573811136"></a>缺省值为100ms；一般--cpu-period参数和--cpu-quota是配合使用的，比如--cpu-period=50000 --cpu-quota=25000，意味着如果有1个CPU，该容器可以每50ms获取到50%的CPU。</p>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p754192711814"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p754192711814"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p754192711814"></a>使用--cpus=0.5也可达到同样的效果</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row5206162817268"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3206528112617"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3206528112617"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3206528112617"></a>--cpu-quota</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p416835333813"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p416835333813"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p416835333813"></a>设置CFS(完全公平调度策略)进程的CPU配额，默认为0，即没有限制</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row156458413395"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1264694173910"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1264694173910"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1264694173910"></a>--cpuset-cpus</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p924612309396"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p924612309396"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p924612309396"></a>设置容器中进程允许运行的CPU (0-3, 0,1)。默认没有限制</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row2946124394"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p494181216393"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p494181216393"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p494181216393"></a>--cpuset-mems</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p20942126396"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p20942126396"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p20942126396"></a>设置容器中进程运行的内存节点 (0-3, 0,1)，只对NUMA系统起作用</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1246231483919"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1046321410394"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1046321410394"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1046321410394"></a>--device=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17463141416395"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17463141416395"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17463141416395"></a>将主机的设备添加到容器中 (e.g. --device=/dev/sdc:/dev/xvdc:rwm)</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row5677161718393"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p9677717143920"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p9677717143920"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p9677717143920"></a>--dns=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p8677191743912"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p8677191743912"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p8677191743912"></a>强制容器使用指定的dns服务器（e.g. 创建容器时指定--dns=114.114.xxx.xxx，将在容器的/etc/resolv.conf中写入nameserver 114.114.xxx.xxx并将覆盖原来的内容）</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row35991149113218"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p9599849173216"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p9599849173216"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p9599849173216"></a>--dns-opt=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p157887213330"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p157887213330"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p157887213330"></a>设置DNS选项</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row10476452143212"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p147616528321"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p147616528321"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p147616528321"></a>--dns-search=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p44042037103310"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p44042037103310"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p44042037103310"></a>强制容器使用指定的dns搜索域名</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row115101955143215"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3510855103218"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3510855103218"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3510855103218"></a>-e, --env=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1510125516321"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1510125516321"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1510125516321"></a>设置容器的环境变量</p>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p6236165619264"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p6236165619264"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p6236165619264"></a>--env=[KERNEL_MODULES=]:</p>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p174241144162614"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p174241144162614"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p174241144162614"></a>在容器中插入指定模块。目前仅支持Host主机上有的模块，且容器删除后Host主机上模块仍然驻留，且容器需要同时指定--hook-spec选项。以下都是参数的合法格式：</p>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p9502124212615"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p9502124212615"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p9502124212615"></a>KERNEL_MODULERS=</p>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17753847172611"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17753847172611"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17753847172611"></a>KERNEL_MODULERS=a</p>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p953414962610"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p953414962610"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p953414962610"></a>KERNEL_MODULERS=a,b</p>
<p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1381113162616"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1381113162616"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1381113162616"></a>KERNEL_MODULERS=a,b,</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row763085713328"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1663015712322"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1663015712322"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1663015712322"></a>--entrypoint=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1763135714328"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1763135714328"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1763135714328"></a>覆盖image中原有的entrypoint，entrypoint设置容器启动时执行的命令</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1774265915324"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2074275918322"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2074275918322"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2074275918322"></a>--env-file=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1774275913325"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1774275913325"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1774275913325"></a>从一个文件中读取环境变量，多个环境变量在文件中按行分割（e.g. --env-file=/home/test/env,其中env文件中存放了多个环境变量）</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row638182183316"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2038112143313"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2038112143313"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2038112143313"></a>--expose=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3518135163415"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3518135163415"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3518135163415"></a>开放一个容器内部的端口，使用下文介绍的-P选项将会使开放的端口映射到主机的一个端口。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1571316419339"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p971311443316"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p971311443316"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p971311443316"></a>--group-add=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p343520423515"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p343520423515"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p343520423515"></a>指定容器添加到额外的组</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row11663811333"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p16661381334"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p16661381334"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p16661381334"></a>-h, --hostname=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p966158203310"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p966158203310"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p966158203310"></a>设置容器主机名</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row51351554164810"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12135115420482"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12135115420482"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12135115420482"></a>--health-cmd</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1213565464815"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1213565464815"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1213565464815"></a>设置容器健康检查执行的命令</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row8969222144910"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p0969922164919"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p0969922164919"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p0969922164919"></a>--health-interval</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p13295335504"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p13295335504"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p13295335504"></a>相邻两次命令执行的间隔时间，默认 30s</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row649018725011"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1949177205019"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1949177205019"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1949177205019"></a>--health-timeout</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p104917718506"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p104917718506"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p104917718506"></a>单次检查命令执行的时间上限，超时则任务命令执行失败，默认30s</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row126076111509"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1660751155012"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1660751155012"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1660751155012"></a>--health-start-period</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17607711175014"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17607711175014"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17607711175014"></a>容器启动距离第一次执行健康检查开始的时间，默认0s</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row66385917505"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1363814925013"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1363814925013"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1363814925013"></a>--health-retries</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1863816915017"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1863816915017"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1863816915017"></a>健康检查失败最大的重试次数，默认3</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row15336158104814"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p93366583488"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p93366583488"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p93366583488"></a>--health-exit-on-unhealthy</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p14336125813484"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p14336125813484"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p14336125813484"></a>容器被检查为非健康后停止容器，默认false</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1463141184610"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p176421112467"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p176421112467"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p176421112467"></a>--host-channel=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12641211194620"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12641211194620"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12641211194620"></a>设置一个通道供容器内进程与主机进行通信，格式：&lt;host path&gt;:&lt;container path&gt;:&lt;rw/ro&gt;:&lt;size limit&gt;</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row16526101063313"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p105261107331"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p105261107331"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p105261107331"></a>-i, --interactive=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p841113270358"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p841113270358"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p841113270358"></a>设置STDIN打开即使没有attached</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row950341273310"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19503121273317"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19503121273317"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19503121273317"></a>--ip</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1547019395354"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1547019395354"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1547019395354"></a>设置容器的IPv4地址</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row87181149143513"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p171814919351"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p171814919351"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p171814919351"></a>--ip6</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p67181649103512"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p67181649103512"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p67181649103512"></a>设置容器的IPv6地址</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1717716527350"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p111771752113512"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p111771752113512"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p111771752113512"></a>--ipc</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1689831418365"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1689831418365"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1689831418365"></a>指定容器的ipc命名空间</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row10615195415353"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17615654143517"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17615654143517"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17615654143517"></a>--isolation</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p178131223133615"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p178131223133615"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p178131223133615"></a>指定容器隔离策略</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row15103164904017"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p210364914409"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p210364914409"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p210364914409"></a>-l, --label=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p185289288418"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p185289288418"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p185289288418"></a>设置容器的标签</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1669151694117"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1669110162412"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1669110162412"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1669110162412"></a>--label-file=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p48722030164217"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p48722030164217"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p48722030164217"></a>从文件中获取标签</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row157612515412"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18576165164117"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18576165164117"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18576165164117"></a>--link=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19577655418"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19577655418"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19577655418"></a>链接到其他容器，这个选项将在容器中添加一些被链接容器IP地址和端口的环境变量及在/etc/hosts中添加一条映射（e.g. --link=name:alias）</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row6312814104119"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p163125144414"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p163125144414"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p163125144414"></a>--log-driver</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p16201659144116"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p16201659144116"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p16201659144116"></a>设置容器的日志驱动</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1943121115418"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p394331118414"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p394331118414"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p394331118414"></a>--log-opt=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1348874894116"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1348874894116"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1348874894116"></a>设置日志驱动选项</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1469012816412"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p26901688416"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p26901688416"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p26901688416"></a>-m, --memory=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1469017824112"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1469017824112"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1469017824112"></a>设置容器的内存限制，格式&lt;number&gt;&lt;optional unit&gt;, 其中 unit = b, k, m or g。该参数最小值为4m。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row102019564425"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p10201566422"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p10201566422"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p10201566422"></a>--mac-address</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p920175644216"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p920175644216"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p920175644216"></a>设置容器的mac地址 (e.g. 92:d0:c6:0a:xx:xx)</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1718125964210"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p11811595428"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p11811595428"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p11811595428"></a>--memory-reservation</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p21815598424"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p21815598424"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p21815598424"></a>设置容器内存限制，默认与--memory一致。可认为--memory是硬限制，--memory-reservation是软限制；当使用内存超过预设值时，会动态调整（系统回收内存时尝试将使用内存降低到预设值以下），但不确保一定不超过预设值。一般可以和--memory一起使用，数值小于--memory的预设值。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row13297131204317"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17297171144317"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17297171144317"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p17297171144317"></a>--memory-swap</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p20638163719436"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p20638163719436"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p20638163719436"></a>设置普通内存和交换分区的使用总量，-1为不做限制。如果不设置，则为--memory值的2倍，即SWAP可再使用与--memory相同的内存量。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row586111317439"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p168611638434"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p168611638434"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p168611638434"></a>--memory-swappiness=-1</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1463649144316"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1463649144316"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1463649144316"></a>设置容器使用交换内存的时机,以剩余内存百分比为度量（0-100）</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1115912604311"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p916016613431"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p916016613431"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p916016613431"></a>--net="bridge"</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1396135910430"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1396135910430"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1396135910430"></a>设置容器的网络模式，当前1.3.0版本的docker有四个模式：bridge、host、none、container:&lt;name|id&gt;。默认使用的是bridge。</p>
<a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_ul9922135114448"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_ul9922135114448"></a><ul id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_ul9922135114448"><li>bridge：使用桥接模式在docker daemon启动时使用的网桥上创建一个网络栈。</li><li>host：在容器内使用主机的网络栈</li><li>none：不使用网络</li><li>container:&lt;name|id&gt;：重复利用另外一个容器的网络栈</li></ul>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row5294172735110"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1129516276515"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1129516276515"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1129516276515"></a>--no-healthcheck</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2295162775113"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2295162775113"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2295162775113"></a>设置容器不使用健康检查</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row168110614418"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1281116624417"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1281116624417"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1281116624417"></a>--oom-kill-disable</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p444212918453"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p444212918453"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p444212918453"></a>禁用OOM killer，建议如果不设置-m参数，也不要设置此参数。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row341617138444"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1841691311447"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1841691311447"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1841691311447"></a>--oom-score-adj</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2416131319445"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2416131319445"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2416131319445"></a>调整容器的oom规则（-1000到1000）</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row246419153446"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12464215164418"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12464215164418"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12464215164418"></a>-P, --publish-all=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12464201574416"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12464201574416"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p12464201574416"></a>将容器开放的所有端口一一映射到主机的端口，通过主机的端口可以访问容器内部，通过下文介绍的docker port命令可以查看具体容器端口和主机端口具体的映射关系。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row9418171810445"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p841881874416"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p841881874416"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p841881874416"></a>-p, --publish=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1541861824418"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1541861824418"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1541861824418"></a>将容器内的一个端口映射到主机的一个端口，format: ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort | containerPort，如果没有指定IP代表侦听主机所有网卡的访问，如果没有指定hostPort,表示自动分配主机的端口。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row89921542103611"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p11992134219363"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p11992134219363"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p11992134219363"></a>--pid</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18568141920378"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18568141920378"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18568141920378"></a>设置容器的PID命名空间</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row89658387"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1092051386"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1092051386"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1092051386"></a>--privileged=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3910573819"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3910573819"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p3910573819"></a>给予容器额外的权限，当使用了--privileged选项，容器将可以访问主机的所有设备。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row15237826153817"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p0237182619382"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p0237182619382"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p0237182619382"></a>--restart=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2345184412396"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2345184412396"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p2345184412396"></a>设置容器退出时候的重启规则，当前1.3.1版本支持3个规则：</p>
<a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_ul17280105917391"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_ul17280105917391"></a><ul id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_ul17280105917391"><li>no：当容器停止时，不重启。</li><li>on-failure：当容器退出码为非0时重启容器，这个规则可以附加最大重启次数，如on-failure:5，最多重启5次。</li><li>always：无论退出码是什么都退出。</li></ul>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row18911132323815"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p691142343810"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p691142343810"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p691142343810"></a>--read-only</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18668559397"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18668559397"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18668559397"></a>将容器的根文件系统以只读的形式挂载</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row115202185389"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p35201018113818"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p35201018113818"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p35201018113818"></a>--security-opt=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p10176115516385"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p10176115516385"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p10176115516385"></a>容器安全规则</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row95053164386"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p05053168384"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p05053168384"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p05053168384"></a>--shm-size</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p108581345163819"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p108581345163819"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p108581345163819"></a>/dev/shm设备的大小，缺省值是64M</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row34721411143812"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1847261112385"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1847261112385"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1847261112385"></a>--stop-signal=SIGTERM</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p147783314387"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p147783314387"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p147783314387"></a>容器停止信号，默认为SIGTERM</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row18696045133612"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p66961459369"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p66961459369"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p66961459369"></a>-t, --tty=false</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18445955113719"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18445955113719"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p18445955113719"></a>分配一个伪终端</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row842624843616"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p144266481367"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p144266481367"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p144266481367"></a>--tmpfs=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p942618487361"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p942618487361"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p942618487361"></a>挂载tmpfs目录</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row12203175133620"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p620395113367"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p620395113367"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p620395113367"></a>-u, --user=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1388111347372"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1388111347372"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1388111347372"></a>指定用户名或者用户ID</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row14460853103619"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p246185363611"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p246185363611"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p246185363611"></a>--ulimit=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p117531243374"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p117531243374"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p117531243374"></a>ulimit选项</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row864743674613"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p36471436134619"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p36471436134619"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p36471436134619"></a>--userns</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p122220164710"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p122220164710"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p122220164710"></a>指定容器的user命名空间</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row1165391469"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p4693913466"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p4693913466"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p4693913466"></a>-v, --volume=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p96153964610"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p96153964610"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p96153964610"></a>将主机的一个目录挂载到容器内部，或者在容器中创建一个新卷（e.g. -v /home/test:/home将主机的/home/test目录挂载到容器的/home目录下，-v /tmp 在容器中的根目录下创建tmp文件夹，该文件夹可以被其他容器用--volumes-from选项共享 ）。不支持将主机目录挂载到容器/proc子目录，否则启动容器会报错。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row764314134618"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p196438413462"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p196438413462"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p196438413462"></a>--volume-driver</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19643184184612"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19643184184612"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p19643184184612"></a>设置容器的数据卷驱动，可选。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row429319445461"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p11293204410466"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p11293204410466"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p11293204410466"></a>--volumes-from=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p112931244114612"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p112931244114612"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p112931244114612"></a>将另外一个容器的卷挂载到本容器中，实现卷的共享（e.g. -volumes-from container_name将container_name中的卷挂载到这个容器中 ）。-v和--volumes-from=[]是两个非常重要的选项用于数据的备份和热迁移。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_row12256348174612"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p925654819460"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p925654819460"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p925654819460"></a>-w, --workdir=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1624165744718"><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1624165744718"></a><a name="zh-cn_topic_0183243660_zh-cn_topic_0155236887_zh-cn_topic_0124544921_zh-cn_topic_0043209392_p1624165744718"></a>指定容器的工作目录，进入容器时的目录</p>
</td>
</tr>
</tbody>
</table>

示例：

创建了一个名为busybox的容器，创建之后的容器用docker start命令启动。

```shell
$ sudo docker create -ti --name=busybox busybox /bin/bash
```

## diff

用法：**docker diff CONTAINER**

功能：检视容器的差异，相比于容器刚创建时做了哪些改变

选项：无

示例：

```shell
$ sudo docker diff registry
C /root
A /root/.bash_history
A /test
```

## exec

### 接口原型

```shell
rpc Exec(ExecRequest) returns (ExecResponse) {}
```

### 接口描述

在容器中执行命令，采用的gRPC通讯方式从CRI服务端获取url，再通过获得的url与websocket服务端建立长连接，实现与容器的交互。

### 注意事项

执行一条单独的命令，也能打开终端与容器交互。stdin/stdout/stderr之一必须是真的。如果tty为真，stderr必须是假的。 不支持多路复用，在这种情况下，stdout和stderr的输出将合并为单流。

### 参数

<a name="zh-cn_topic_0183088053_table184320467318"></a>
<table><tbody><tr id="zh-cn_topic_0183088053_row78917461336"><td class="cellrowborder" valign="top" width="39.54%"><p id="zh-cn_topic_0183088053_p1089154617315"><a name="zh-cn_topic_0183088053_p1089154617315"></a><a name="zh-cn_topic_0183088053_p1089154617315"></a><strong id="zh-cn_topic_0183088053_b98915462314"><a name="zh-cn_topic_0183088053_b98915462314"></a><a name="zh-cn_topic_0183088053_b98915462314"></a>参数成员</strong></p>
</td>
<td class="cellrowborder" valign="top" width="60.46%"><p id="zh-cn_topic_0183088053_p128984613319"><a name="zh-cn_topic_0183088053_p128984613319"></a><a name="zh-cn_topic_0183088053_p128984613319"></a><strong id="zh-cn_topic_0183088053_b989164612317"><a name="zh-cn_topic_0183088053_b989164612317"></a><a name="zh-cn_topic_0183088053_b989164612317"></a>描述</strong></p>
</td>
</tr>
<tr id="zh-cn_topic_0183088053_row10898461533"><td class="cellrowborder" valign="top" width="39.54%"><p id="zh-cn_topic_0183088053_p1253351115517"><a name="zh-cn_topic_0183088053_p1253351115517"></a><a name="zh-cn_topic_0183088053_p1253351115517"></a>string container_id</p>
</td>
<td class="cellrowborder" valign="top" width="60.46%"><p id="zh-cn_topic_0183088053_p1189846434"><a name="zh-cn_topic_0183088053_p1189846434"></a><a name="zh-cn_topic_0183088053_p1189846434"></a>容器ID</p>
</td>
</tr>
<tr id="zh-cn_topic_0183088053_row17894468314"><td class="cellrowborder" valign="top" width="39.54%"><p id="zh-cn_topic_0183088053_p1489111122411"><a name="zh-cn_topic_0183088053_p1489111122411"></a><a name="zh-cn_topic_0183088053_p1489111122411"></a>repeated string cmd</p>
</td>
<td class="cellrowborder" valign="top" width="60.46%"><p id="zh-cn_topic_0183088053_p780820166266"><a name="zh-cn_topic_0183088053_p780820166266"></a><a name="zh-cn_topic_0183088053_p780820166266"></a>待执行的命令</p>
</td>
</tr>
<tr id="zh-cn_topic_0183088053_row4812119101610"><td class="cellrowborder" valign="top" width="39.54%"><p id="zh-cn_topic_0183088053_p3218304144"><a name="zh-cn_topic_0183088053_p3218304144"></a><a name="zh-cn_topic_0183088053_p3218304144"></a>bool tty</p>
</td>
<td class="cellrowborder" valign="top" width="60.46%"><p id="zh-cn_topic_0183088053_p1947314925616"><a name="zh-cn_topic_0183088053_p1947314925616"></a><a name="zh-cn_topic_0183088053_p1947314925616"></a>是否在TTY中执行命令</p>
</td>
</tr>
<tr id="zh-cn_topic_0183088053_row1569883411415"><td class="cellrowborder" valign="top" width="39.54%"><p id="zh-cn_topic_0183088053_p06982346147"><a name="zh-cn_topic_0183088053_p06982346147"></a><a name="zh-cn_topic_0183088053_p06982346147"></a>bool stdin</p>
</td>
<td class="cellrowborder" valign="top" width="60.46%"><p id="zh-cn_topic_0183088053_p469919340142"><a name="zh-cn_topic_0183088053_p469919340142"></a><a name="zh-cn_topic_0183088053_p469919340142"></a>是否流式标准输入</p>
</td>
</tr>
<tr id="zh-cn_topic_0183088053_row12135742161414"><td class="cellrowborder" valign="top" width="39.54%"><p id="zh-cn_topic_0183088053_p5135242161417"><a name="zh-cn_topic_0183088053_p5135242161417"></a><a name="zh-cn_topic_0183088053_p5135242161417"></a>bool stdout</p>
</td>
<td class="cellrowborder" valign="top" width="60.46%"><p id="zh-cn_topic_0183088053_p1613584220142"><a name="zh-cn_topic_0183088053_p1613584220142"></a><a name="zh-cn_topic_0183088053_p1613584220142"></a>是否流式标准输出</p>
</td>
</tr>
<tr id="zh-cn_topic_0183088053_row101281154171413"><td class="cellrowborder" valign="top" width="39.54%"><p id="zh-cn_topic_0183088053_p151281754181412"><a name="zh-cn_topic_0183088053_p151281754181412"></a><a name="zh-cn_topic_0183088053_p151281754181412"></a>bool stderr</p>
</td>
<td class="cellrowborder" valign="top" width="60.46%"><p id="zh-cn_topic_0183088053_p51282542141"><a name="zh-cn_topic_0183088053_p51282542141"></a><a name="zh-cn_topic_0183088053_p51282542141"></a>是否流式输出标准错误</p>
</td>
</tr>
</tbody>
</table>

### 返回值

<a name="zh-cn_topic_0183088053_table15296551936"></a>
<table><tbody><tr id="zh-cn_topic_0183088053_row18741555834"><td class="cellrowborder" valign="top" width="39.54%"><p id="zh-cn_topic_0183088053_p197485518319"><a name="zh-cn_topic_0183088053_p197485518319"></a><a name="zh-cn_topic_0183088053_p197485518319"></a><strong id="zh-cn_topic_0183088053_b77413551933"><a name="zh-cn_topic_0183088053_b77413551933"></a><a name="zh-cn_topic_0183088053_b77413551933"></a>返回值</strong></p>
</td>
<td class="cellrowborder" valign="top" width="60.46%"><p id="zh-cn_topic_0183088053_p374185520310"><a name="zh-cn_topic_0183088053_p374185520310"></a><a name="zh-cn_topic_0183088053_p374185520310"></a><strong id="zh-cn_topic_0183088053_b174125511315"><a name="zh-cn_topic_0183088053_b174125511315"></a><a name="zh-cn_topic_0183088053_b174125511315"></a>描述</strong></p>
</td>
</tr>
<tr id="zh-cn_topic_0183088053_row87419551317"><td class="cellrowborder" valign="top" width="39.54%"><p id="zh-cn_topic_0183088053_p15574205011242"><a name="zh-cn_topic_0183088053_p15574205011242"></a><a name="zh-cn_topic_0183088053_p15574205011242"></a>string url</p>
</td>
<td class="cellrowborder" valign="top" width="60.46%"><p id="zh-cn_topic_0183088053_p103555206255"><a name="zh-cn_topic_0183088053_p103555206255"></a><a name="zh-cn_topic_0183088053_p103555206255"></a>exec流服务器的完全限定URL</p>
</td>
</tr>
</tbody>
</table>

## export

用法：**docker export CONTAINER**

功能：将一个容器的文件系统内容以tar包导出到STDOUT

选项：无

示例：

将名为busybox的容器的内容导出到busybox.tar包中：

```shell
$ sudo docker export busybox > busybox.tar
$ ls
busybox.tar 
```

## inspect

用法：**docker inspect \[OPTIONS\] CONTAINER|IMAGE \[CONTAINER|IMAGE...\]**

功能：返回一个容器或者镜像的底层信息

选项：

-f, \--format=""    按照给定的格式输出信息

-s, \--size    若查询类型为容器，显示该容器的总体文件大小

\--type    返回指定类型的JSON格式

-t, \--time=120 超时时间的秒数，若在该时间内docker inspect未执行成功，则停止等待并立即报错。默认为120秒。

示例：

1. 返回一个容器的信息

    ```shell
    $ sudo docker inspect busybox_test
    [
        {
            "Id": "9fbb8649d5a8b6ae106bb0ac7686c40b3cbd67ec2fd1ab03e0c419a70d755577",
            "Created": "2019-08-28T07:43:51.27745746Z",
            "Path": "bash",
            "Args": [],
            "State": {
                "Status": "running",
                "Running": true,
                "Paused": false,
                "Restarting": false,
                "OOMKilled": false,
                "Dead": false,
                "Pid": 64177,
                "ExitCode": 0,
                "Error": "",
                "StartedAt": "2019-08-28T07:43:53.021226383Z",
                "FinishedAt": "0001-01-01T00:00:00Z"
            },
    ......
    ```

2. 按照给定格式返回一个容器的指定信息，下面的例子返回busybox\_test容器IP地址

    ```shell
    $ sudo docker inspect -f {{.NetworkSettings.IPAddress}} busybox_test
    172.17.0.91
    ```

## logs

用法：**docker logs \[OPTIONS\] CONTAINER**

功能：抓取容器内的日志信息，容器可以是运行状态的也可以是停止状态的

选项：

-f, \--follow=false        实时打印日志信息

-t, \--timestamps=false     显示日志的时间戳

\--since     显示指定时间之后的日志

\--tail="all"              设置显示的行数，默认显示所有

示例：

1. 查看jaegertracing容器的日志信息，该容器上跑了一个jaegertracing服务

    ```shell
    $ sudo docker logs jaegertracing
    {"level":"info","ts":1566979103.3696961,"caller":"healthcheck/handler.go:99","msg":"Health Check server started","http-port":14269,"status":"unavailable"}
    {"level":"info","ts":1566979103.3820567,"caller":"memory/factory.go:55","msg":"Memory storage configuration","configuration":{"MaxTraces":0}}
    {"level":"info","ts":1566979103.390773,"caller":"tchannel/builder.go:94","msg":"Enabling service discovery","service":"jaeger-collector"}
    {"level":"info","ts":1566979103.3908608,"caller":"peerlistmgr/peer_list_mgr.go:111","msg":"Registering active peer","peer":"127.0.0.1:14267"}
    {"level":"info","ts":1566979103.3922884,"caller":"all-in-one/main.go:186","msg":"Starting agent"}
    {"level":"info","ts":1566979103.4047635,"caller":"all-in-one/main.go:226","msg":"Starting jaeger-collector TChannel server","port":14267}
    {"level":"info","ts":1566979103.404901,"caller":"all-in-one/main.go:236","msg":"Starting jaeger-collector HTTP server","http-port":14268}
    {"level":"info","ts":1566979103.4577134,"caller":"all-in-one/main.go:256","msg":"Listening for Zipkin HTTP traffic","zipkin.http-port":9411}
    ```

2. 加上-f选项，实时打印jaegertracing容器的日志信息

    ```shell
    $ sudo docker logs -f jaegertracing
    {"level":"info","ts":1566979103.3696961,"caller":"healthcheck/handler.go:99","msg":"Health Check server started","http-port":14269,"status":"unavailable"}
    {"level":"info","ts":1566979103.3820567,"caller":"memory/factory.go:55","msg":"Memory storage configuration","configuration":{"MaxTraces":0}}
    {"level":"info","ts":1566979103.390773,"caller":"tchannel/builder.go:94","msg":"Enabling service discovery","service":"jaeger-collector"}
    {"level":"info","ts":1566979103.3908608,"caller":"peerlistmgr/peer_list_mgr.go:111","msg":"Registering active peer","peer":"127.0.0.1:14267"}
    {"level":"info","ts":1566979103.3922884,"caller":"all-in-one/main.go:186","msg":"Starting agent"}
    ```

## pause-unpause

用法：**docker pause CONTAINER**

**docker unpause CONTAINER**

功能：这两个命令是配对使用的，docker pause暂停容器内的所有进程，docker unpause恢复暂停的进程

选项：无

示例：

本示例将演示一个跑了docker registry（docker镜像服务）服务的容器，当使用docker pause 命令暂停这个容器的进程后，使用curl命令访问该registry服务将阻塞，使用docker unpause命令将恢复registry服务，可以用curl命令访问。

1. 启动一个registry容器

    ```shell
    $ sudo docker run -d --name pause_test -p 5000:5000 registry
    ```

    此时可以用curl命令访问这个服务，请求状态码会返回200 OK。

    ```shell
    $ sudo curl -v 127.0.0.1:5000
    ```

2. 暂停这个容器内的进程

    ```shell
    $ sudo docker pause pause_test
    ```

    此时用curl命令访问这个服务将阻塞，等待服务开启。

3. 恢复运行这个容器内的进程

    ```shell
    $ sudo docker unpause pause_test
    ```

    此时步骤2中的curl访问将恢复运行，请求状态码返回200 OK。

## port

用法：**docker port CONTAINER \[PRIVATE\_PORT\[/PROTO\]\]**

功能：列出容器的端口映射，或者查找指定端口在主机的哪个端口

选项：无

示例：

1. 列出容器所有的端口映射

    ```shell
    $ sudo docker port registry
    5000/tcp -> 0.0.0.0.：5000
    ```

2. 查找容器指定端口的映射

    ```shell
    $ sudo docker port registry 5000
    0.0.0.0.：5000
    ```

## ps

用法：**docker ps \[OPTIONS\]**

功能：根据不同的选项列出不同状态的容器，在不加任何选项的情况下，将列出正在运行的容器

选项：

-a, \--all=false     显示所用的容器

-f, \--filter=\[\]      筛选值，可用的筛选值有：exited=<int\>容器的退出码status=\(restarting|running|paused|exited\)容器的状态码（e.g. -f status=running，列出正在运行的容器）

-l, \--latest=false   列出最近创建的一个容器

-n=-1            列出最近n次创建的容器

\--no-trunc=false   将64位的容器ID全部显示出来，默认显示12位容器的ID

-q, \--quiet=false   显示容器的ID

-s, \--size=false    显示容器的大小

示例：

1. 列出正在运行的容器

    ```shell
    $ sudo docker ps
    ```

2. 列出所有的容器

    ```shell
    $ sudo docker ps -a
    ```

## rename

用法：**docker rename OLD\_NAME NEW\_NAME**

功能：重命名容器

示例：

示例中，用docker run创建并启动一个容器，使用docker rename对容器重命名，并查看容器名是否改变。

```shell
$ sudo docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
b15976967abb        busybox:latest        "bash"              3 seconds ago       Up 2 seconds                            festive_morse
$ sudo docker rename pedantic_euler new_name
$ sudo docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
b15976967abb        busybox:latest        "bash"              34 seconds ago      Up 33 seconds                           new_name
```

## restart

用法：**docker restart \[OPTIONS\] CONTAINER \[CONTAINER...\]**

功能：重启一个运行中的容器

选项：

-t, \--time=10   在杀掉容器之前等待容器停止的秒数，如果容器已停止，就重启。默认为10秒。

示例：

```shell
$ sudo docker restart busybox
```

> [!NOTE]说明
>
> 容器在restart过程中，如果容器内存在D状态或Z状态的进程，可能会导致容器重启失败，这需要进一步分析导致容器内进程D状态或Z状态的原因，待容器内进程D状态或Z状态解除后，再进行容器restart操作。  

## rm

用法：**docker rm \[OPTIONS\] CONTAINER \[CONTAINER...\]**

功能：删除一个或多个容器

选项：

-f, \--force=false      强制删除运行中的容器

-l, \--link=false       删除指定的链接，而不是底层容器

-v, \--volumes=false    删除与容器关联的卷

示例：

1. 删除一个停止运行的容器

    ```shell
    $ sudo docker rm test
    ```

2. 删除一个正在运行的容器

    ```shell
    $ sudo docker rm -f rm_test
    ```

## run

用法：**docker run \[OPTIONS\] IMAGE \[COMMAND\] \[ARG...\]**

功能：该命令将由指定的image（如果指定的IMAGE不存在，则从官方镜像库中下载一个镜像）创建一个容器，并启动这个容器，并在容器中执行指定的命令。该命令集成了docker create命令、docker start命令、docker exec命令。

选项：（该命令的选项与docker create命令的选项一样，请参考docker create命令选项，仅仅多了以下两个选项）

\--rm=false        设置容器退出时自动删除容器

-v 挂载本地目录或匿名卷到容器内。注意：当将本地目录以带有selinux的安全标签的方式挂载到容器内的同时，尽量不要同时做该本地目录的增删操作，否则该安全标签可能不生效

\--sig-proxy=true    发往进程信号的代理，SIGCHLD, SIGSTOP, SIGKILL不使用代理

示例：

使用busybox镜像运行一个容器，在容器启动后执行/bin/sh

```shell
$ sudo docker run -ti busybox /bin/sh
```

## start

用法：**docker start \[OPTIONS\] CONTAINER \[CONTAINER...\]**

功能：启动一个或多个未运行容器

选项：

-a, \--attach=false     容器的标准输出和错误输出附加到host的STDOUT和STDERR上

-i, \--interactive=false  容器的标准输入附加到host的STDIN上

示例：

启动一个名为busybox的容器，添加-i -a选项附加标准输入输出，容器启动后直接进入容器内部，输入exit可以退出容器。

如果启动容器时不加-i -a选项，容器将在后台启动。

```shell
$ sudo docker start -i -a busybox
```

## stats

用法：**docker stats \[OPTIONS\] \[CONTAINER...\]**

功能：持续监控并显示指定容器（若不指定，则默认全部容器）的资源占用情况

选项：

-a, \--all        显示所有容器（默认仅显示运行状态的容器）

\--no-stream    只显示第一次的结果，不持续监控

示例：

示例中，用docker run创建并启动一个容器，docker stats将输出容器的资源占用情况。

```shell
$ sudo docker stats
CONTAINER ID        NAME                    CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
2e242bcdd682        jaeger                  0.00%               77.08MiB / 125.8GiB   0.06%               42B / 1.23kB        97.9MB / 0B         38
02a06be42b2c        relaxed_chandrasekhar   0.01%               8.609MiB / 125.8GiB   0.01%               0B / 0B             0B / 0B             10
deb9e49fdef1        hardcore_montalcini     0.01%               12.79MiB / 125.8GiB   0.01%               0B / 0B             0B / 0B             9
```

## stop

用法：**docker stop \[OPTIONS\] CONTAINER \[CONTAINER...\]**

功能：通过向容器发送一个SIGTERM信号并在一定的时间后发送一个SIGKILL信号停止容器

选项：

-t, \--time=10   在杀掉容器之前等待容器退出的秒数，默认为10S

示例：

```shell
$ sudo docker stop -t=15 busybox
```

## top

用法：**docker top CONTAINER \[ps OPTIONS\]**

功能：显示一个容器内运行的进程

选项：无

示例：

先运行了一个名为top\_test的容器，并在其中执行了top指令

```shell
$ sudo docker top top_test
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                70045               70028               0                   15:52               pts/0               00:00:00            bash
```

显示的PID是容器内的进程在主机中的PID号。

## update

用法：**docker update \[OPTIONS\] CONTAINER \[CONTAINER...\]**

功能：热变更一个或多个容器配置。

选项：

**表 3**  参数说明

<a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_table1239044502210"></a>
<table><thead align="left"><tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row439004518223"><th class="cellrowborder" id="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p19390104532213"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p19390104532213"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p19390104532213"></a>参数</p>
</th>
<th class="cellrowborder" id="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1039064522216"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1039064522216"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1039064522216"></a>参数含义</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row1349192781120"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p2350827111119"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p2350827111119"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p2350827111119"></a>--accel=[]</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p535052711113"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p535052711113"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p535052711113"></a>设置容器加速器，可设置一个或多个</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row939164522218"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p03911345142218"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p03911345142218"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p03911345142218"></a>--blkio-weight</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1139111453223"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1139111453223"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1139111453223"></a>设置容器blockio的相对权重，从10到1000</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row339184572217"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p83911445172217"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p83911445172217"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p83911445172217"></a>--cpu-shares</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p3391145132220"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p3391145132220"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p3391145132220"></a>设置容器获得主机CPU的相对权重，通过设置这个选项获得更高的优先级，默认所有的容器都是获得相同的CPU优先权。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row8107726122617"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p51070266260"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p51070266260"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p51070266260"></a>--cpu-period</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p6107926132615"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p6107926132615"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p6107926132615"></a>设置CFS（完全公平调度策略）进程的CPU周期。</p>
<p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1869573811136"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1869573811136"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1869573811136"></a>缺省值为100ms；一般--cpu-period参数和--cpu-quota是配合使用的，比如--cpu-period=50000 --cpu-quota=25000，意味着如果有1个CPU，该容器可以每50ms获取到50%的CPU。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row5206162817268"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p3206528112617"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p3206528112617"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p3206528112617"></a>--cpu-quota</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p416835333813"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p416835333813"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p416835333813"></a>设置CFS(完全公平调度策略)进程的CPU配额，默认为0，即没有限制</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row156458413395"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1264694173910"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1264694173910"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1264694173910"></a>--cpuset-cpus</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p924612309396"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p924612309396"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p924612309396"></a>设置容器中进程允许运行的CPU (0-3, 0,1)。默认没有限制</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row2946124394"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p494181216393"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p494181216393"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p494181216393"></a>--cpuset-mems</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p20942126396"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p20942126396"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p20942126396"></a>设置容器中进程运行运行的内存内存节点 (0-3, 0,1)，只对NUMA系统起作用</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row125801648161311"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p7581448101317"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p7581448101317"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p7581448101317"></a>--kernel-memory=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1858174812134"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1858174812134"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1858174812134"></a>设置容器的kernerl内存限制，格式&lt;number&gt;&lt;optional unit&gt;, 其中 unit = b, k, m or g</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row1469012816412"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p26901688416"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p26901688416"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p26901688416"></a>-m, --memory=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1469017824112"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1469017824112"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1469017824112"></a>设置容器的内存限制，格式&lt;number&gt;&lt;optional unit&gt;, 其中 unit = b, k, m or g。该参数最小值为4m。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row1718125964210"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p11811595428"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p11811595428"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p11811595428"></a>--memory-reservation</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p21815598424"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p21815598424"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p21815598424"></a>设置容器内存限制，默认与--memory一致。可认为--memory是硬限制，--memory-reservation是软限制；当使用内存超过预设值时，会动态调整（系统回收内存时尝试将使用内存降低到预设值以下），但不确保一定不超过预设值。一般可以和--memory一起使用，数值小于--memory的预设值。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row13297131204317"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p17297171144317"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p17297171144317"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p17297171144317"></a>--memory-swap</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p20638163719436"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p20638163719436"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p20638163719436"></a>设置普通内存和交换分区的使用总量，-1为不做限制。如果不设置，则为--memory值的2倍，即SWAP可再使用与--memory相同的内存量。</p>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row15237826153817"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p0237182619382"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p0237182619382"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p0237182619382"></a>--restart=""</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p2345184412396"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p2345184412396"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p2345184412396"></a>设置容器退出时候的重启规则，当前1.3.1版本支持3个规则：</p>
<a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_ul17280105917391"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_ul17280105917391"></a><ul id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_ul17280105917391"><li>no：当容器停止时，不重启。</li><li>on-failure：当容器退出码为非0时重启容器，这个规则可以附加最大重启次数，如on-failure:5，最多重启5次。</li><li>always：无论退出码是什么都退出。</li></ul>
</td>
</tr>
<tr id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_row209473268151"><td class="cellrowborder" headers="mcps1.2.3.1.1" valign="top" width="32%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p189474268154"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p189474268154"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p189474268154"></a>--help</p>
</td>
<td class="cellrowborder" headers="mcps1.2.3.1.2" valign="top" width="68%"><p id="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1394720264154"><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1394720264154"></a><a name="zh-cn_topic_0183243758_zh-cn_topic_0155237612_zh-cn_topic_0138971318_p1394720264154"></a>打印help信息</p>
</td>
</tr>
</tbody>
</table>

示例：

变更一个容器名为busybox的cpu和mem配置，包括容器获得主机CPU的相对权重值为512，容器中进程允许运行的CPU核心为0,1,2,3，容器运行内存限制为512m。

```shell
$ sudo docker update  --cpu-shares 512  --cpuset-cpus=0,3 --memory 512m ubuntu 
```

## wait

用法：**docker wait CONTAINER \[CONTAINER...\]**

功能：等待一个容器停止，并打印出容器的退出码

选项：无

示例：

先开启一个名为busybox的容器

```shell
$ sudo docker start -i -a busybox
```

执行docker wait

```shell
$ sudo docker wait busybox
0
```

将阻塞等待busybox容器的退出，退出busybox容器后将看到打印退出码“0”。
