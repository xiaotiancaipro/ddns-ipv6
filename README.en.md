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



It is recommended to use the Ubuntu 22.04 system and install it using the root user.



1、CLone this project and enter the project directory `cd /usr/local && git clone https://gitee.com/xiaotiancaipro/ipv6-address-acquisition.git && cd /usr/local/ipv6-address-acquisition`;

2、Installation project dependencies `pip3 install -r requirements.txt`；

3、Copy the required configuration files for the project `cp .env.sample .env`，And configure all configuration information in the `. env` configuration file;

4、Execute project main program

​	1> Automatically obtain the IPv6 address when the host is turned on and send it to the designated recipient through email, Add `python3 /usr/local/ipv6-address-acquisition/main.py boot` in the startup script `rc.local`;

​	2> After the host is turned on, the IPv6 address is automatically obtained every 10 minutes. If there is a change in the IPv6 address, it is sent to the designated recipient through email, Adding scheduled tasks `*/10 * * * * python3 /usr/local/ipv6-address-acquisition/main.py` using commands `crontab -e`.



The `rc. local` file in step 4 of the above installation steps requires the following steps to create and implement a custom script for startup:

1、Use the `vim /etc/systemd/system/rc-local.service` command to create the `rc-local.service` file and add the following content:

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

2、Use the `vim /etc/rc.local` command to create the `rc.local` file and add the following content:

```bash
#!/bin/sh -e
python3 /usr/local/ipv6-address-acquisition/main.py boot # Here, the specified script is automatically run when the host starts up
exit 0
```

3、Use the `chmod +x /etc/rc.local` command to add executable permissions to the `rc.local` file.

4、使用 `systemctl enable rc-local` 命令启用服务。



### If this project is of some use to you, thank you for your star

