# ddns-ipv6



## 简介

获取主机 IPv6 地址，并通过邮件服务器发送邮件，同时进行 DDNS，目前支持阿里云。




## 安装



### 克隆项目

```bash
git clone https://github.com/xiaotiancaipro/ddns-ipv6.git
```

在启用服务之前，我们需要首先部署 PostgresSQL 数据库和 Redis，如果本地没有可以使用以下命令启动它们：

```bash
cd docker
docker compose -f docker-compose.yaml -p ddns-ipv6 up -d
```



### 服务端部署

- 异步队列生产服务
- 异步队列消费服务



#### 基础环境安装

服务启动需要 Python 3.10.x 环境。推荐使用 [Anaconda](https://docs.anaconda.com/free/anaconda/install/) 快速安装Python环境，它已包含pip包管理工具。

```bash
cd api
# 创建名为 ddns-ipv6 的 Python 3.10 环境
conda env create -f environment.yaml
# 切换至 ddns-ipv6 Python 环境
conda activate ddns-ipv6
```



#### 启动步骤

1. 进入 api 目录

   ```bash
   cd api
   ```

2. 配置环境变量。创建一个名为 “.env” 的文件，并复制 “.env.example” 中的内容，根据您的需求修改这些环境变量的值

   ```bash
   APP_ENV=PRODUCTION
   
   SYSTEM_SECRET_KEY=
   
   # Redis
   REDIS_HOST=localhost
   REDIS_PORT=6001
   REDIS_PASSWORD=server123456
   
   # PostgreSQL
   DB_HOST=localhost
   DB_PORT=6002
   DB_DATABASE=ddns_ipv6
   DB_USERNAME=postgres
   DB_PASSWORD=server123456
   
   # SMTP
   SMTP_HOST=
   SMTP_PORT=
   SMTP_USER=
   SMTP_PASSWORD=
   
   # Hostname
   HOSTNAME=Server_Example
   
   # Email sender and receiver
   EMAIL_SENDER=
   EMAIL_RECEIVER=
   
   # DDNS
   DOMAIN_NAME=
   RR=
   TTL=
   
   # Supplier
   PROVIDER=aliyun
   
   # Aliyun
   ALIYUN_ACCESSKEY_ID=
   ALIYUN_ACCESSKEY_SECRET=
   ```

3. 安装所需的依赖项

   ```bash
   pip install -r requirements.txt
   ```

4. 执行数据库迁移。 执行数据库迁移到最新版本

   ```bash
   flask db upgrade
   ```

5. 启动异步队列消费服务

   ```bash
   python -m celery -A app.celery worker -c 1 --loglevel INFO
   ```

6. 启动异步队列生产服务

   ```bash
   python -m celery -A app.celery beat -l INFO
   ```

至此启动成功。



**如果本项目对您有些帮助，感谢您的 Star ！**

