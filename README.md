# ddns-ipv6



## Description

Obtain the host IPv6 address and send it to the designated recipient through email.




## Installation



### Clone ddns-ipv6

```bash
git clone https://github.com/xiaotiancaipro/ddns-ipv6.git
```

Before enabling business services, we need to first deploy PostgresSQL / Redis (if not locally available). We can start them with the following commands:

```bash
cd docker
docker compose -f docker-compose.yaml -p ddns-ipv6 up -d
```



### Server Deployment

- Beat Asynchronous Queue Production Service
- Worker Asynchronous Queue Consumption Service



#### Installation of the basic environment

Server startup requires Python 3.10.x. It is recommended to use [Anaconda](https://docs.anaconda.com/free/anaconda/install/) for quick installation of the Python environment, which already includes the pip package management tool

```bash
# Create a Python 3.10 environment named "ddns-ipv6"
conda create --name ddns-ipv6 python=3.10
# Switch to the "ddns-ipv6" Python environment
conda activate ddns-ipv6
```



#### Follow these steps

1. Navigate to the "api" directory

   ```bash
   cd api
   ```

2. Configure the environment variables. Create a file named `.env` in the current directory and copy the contents from `.env.example`. Modify the values of these environment variables according to your requirements

   ```bash
   APP_ENV=PRODUCTION
   
   SYSTEM_SECRET_KEY=
   
   # Redis
   REDIS_PASSWORD=server123456
   REDIS_HOST=localhost
   REDIS_PORT=6001
   
   # PostgreSQL
   DB_USERNAME=postgres
   DB_PASSWORD=server123456
   DB_HOST=localhost
   DB_PORT=6002
   DB_DATABASE=ddns_ipv6
   
   # SMTP
   SMTP_HOST=
   SMTP_PORT=
   SMTP_USER=
   SMTP_PASSWORD=
   
   # Hostname
   HOSTNAME=
   
   # Email sender and receiver
   EMAIL_SENDER=
   EMAIL_RECEIVER=
   
   # DDNS
   DOMAIN_NAME=
   RR=
   TTL=
   
   # Provider
   PROVIDER=Aliyun
   
   # Aliyun
   ALIYUN_ACCESSKEY_ID=
   ALIYUN_ACCESSKEY_SECRET=
   ```

3. Install the required dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Perform the database migration. Perform database migration to the latest version

   ```bash
   flask db upgrade
   ```

5. Start the Worker service

   ```bash
   python -m celery -A app.celery worker -c 1 --loglevel INFO
   ```

6. Start the Beat service

   ```bash
   python -m celery -A app.celery beat -l INFO
   ```

After successful startup.



**If this project is of some use to you, thank you for your star !**

