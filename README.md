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
│   └── other.py: 其他工具
├── data: 数据缓存位置
├── logs: 项目日志
├── main.py: 主程序
└── .env: 参数配置
```



### 安装教程

1、进入项目目录 `cd ipv6-address-acquisition` ；

2、安装项目依赖 `pip3 install -r requirements.txt` ；

3、复制项目需要的配置文件 `cp .env.sample .env` ，并配置`.env`配置文件中的所有配置信息；

4、执行项目主程序 `python3 main.py`



### 若本项目对您有些用处，感谢您的 star

