# ipv6-address-acquisition



### Description

Obtain the host IPv6 address and send it to the designated recipient through email.



### Project Architecture

```txt
ipv6-address-acquisition
├── config: Parameter configuration package
│   ├── smtp.py: SMTP server configuration
│   └── email.py: Email configuration
├── service
│   ├── email.py: Email related services
│   └── ipv6.py: IPv6 related services
├── view: Main Logic
│   └── ipv6_to_email.py 
├── utils: Utils toolkit
│   ├── logger.py: Log
│   ├── file.py: General tools related to file operations
│   ├── path.py: General tools related to path operations
│   └── system.py: General tools related to operation system
├── data: Data cache location
├── logs: Project log file
├── main.py
└── .env: Configuration information
```



### Installation



建议使用 Ubuntu 22.04 系统，同时使用 root 用户进行安装。



1、CLone this project and enter the project directory `cd /usr/local && git clone https://gitee.com/xiaotiancaipro/ipv6-address-acquisition.git && cd /usr/local/ipv6-address-acquisition`;

2、安装项目依赖 `pip3 install -r requirements.txt`；

3、复制项目需要的配置文件 `cp .env.sample .env`，并配置 `.env` 配置文件中的所有配置信息；

4、执行项目主程序

​	1>  在主机开机时自动获取 IPv6 地址并通过邮箱发送到指定收件人，在开机脚本 `rc.local` 中添加 `python3 /usr/local/ipv6-address-acquisition/main.py boot`；

​	2> 在主机开机后每隔 10 分钟自动获取 IPv6 地址，若 IPv6 地址有变化则通过邮箱发送到指定收件人，使用 `crontab -e` 命令添加计划任务 `*/10 * * * * python3 /usr/local/ipv6-address-acquisition/main.py`。



在以上安装步骤中第 4 步的 1> 中 `rc.local` 文件需要以下步骤来创建实现自定义脚本开机启动：

1、首先使用 `vim /etc/systemd/system/rc-local.service` 命令建立 rc-local.service 文件，并添加以下内容：

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

2、使用 `vim /etc/rc.local` 命令创建 rc.local 文件，并添加以下内容：

```bash
#!/bin/sh -e
python3 /usr/local/ipv6-address-acquisition/main.py boot # 这里实现主机开机自动运行指定脚本
exit 0
```

3、使用 `chmod +x /etc/rc.local` 命令给 rc.local 文件加上可执行权限。

4、使用 `systemctl enable rc-local` 命令启用服务。



### If this project is of some use to you, thank you for your star

