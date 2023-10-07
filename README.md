# ipv6-address-acquisition



### 介绍

获取主机 IPv6 地址，并通过邮箱发送到指定收件人。



### 项目架构

```txt
ipv6-address-acquisition
├── config: 配置信息
│   ├── smtp.py: SMTP服务器配置
│   └── email.py: Email邮件配置
├── service: 服务
│   ├── email.py: 与邮件相关服务
│   └── ipv6.py: 与IPv6相关服务
├── view: 主逻辑
│   └── ipv6_to_email.py 
├── utils: 工具包
│   ├── logger.py: 日志
│   ├── file.py: 与文件操作相关通用工具
│   ├── path.py: 与路径操作相关通用工具
│   └── system.py: 与操作系统相关通用工具
├── data: 数据缓存位置
├── logs: 项目日志
├── main.py: 主程序
└── .env: 参数配置
```



### 安装教程



建议使用 Ubuntu 22.04 系统，同时使用 root 用户进行安装。



1、克隆项目并进入项目目录 `cd /usr/local && git clone https://gitee.com/xiaotiancaipro/ipv6-address-acquisition.git && cd /usr/local/ipv6-address-acquisition` ；

2、安装项目依赖 `pip3 install -r requirements.txt` ；

3、复制项目需要的配置文件 `cp .env.sample .env` ，并配置`.env`配置文件中的所有配置信息；

4、执行项目主程序

​	1>  在主机开机时自动获取 IPv6 地址并通过邮箱发送到指定收件人，在开机脚本`rc.local`中添加`python3 /usr/local/ipv6-address-acquisition/main.py boot`；

​	2> 在主机开机后每隔 10 分钟自动获取 IPv6 地址，若 IPv6 地址有变化则通过邮箱发送到指定收件人，使用`crontab -e`命令添加计划任务`*/10 * * * * python3 /usr/local/ipv6-address-acquisition/main.py`。



在以上安装步骤中第 4 步的 1> 中`rc.local`文件需要以下步骤来创建实现自定义脚本开机启动：

1、首先使用`vim /etc/systemd/system/rc-local.service`命令建立 rc-local.service 文件，并添加以下内容：

```txt
[Unit]
Description=/etc/rc.local Compatibility
ConditionPathExists=/etc/rc.local

[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
StandardOutput=tty
RemainAfterExit=yes
SysVStartPriority=99

[Install]
WantedBy=multi-user.target
```

2、使用`vim /etc/rc.local`命令创建 rc.local 文件，并添加以下内容：

```bash
#!/bin/sh -e
python3 /usr/local/ipv6-address-acquisition/main.py boot # 这里实现主机开机自动运行指定脚本
exit 0
```

3、使用`chmod +x /etc/rc.local`命令给 rc.local 文件加上可执行权限。

4、使用`systemctl enable rc-local`命令启用服务。



### 若本项目对您有些用处，感谢您的 star

