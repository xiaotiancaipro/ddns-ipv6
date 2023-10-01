import os

from config import Config


class SMTPConfig(Config):
    """配置 SMTP 服务器参数"""

    host = os.getenv("SMTP_HOST")
    port = os.getenv("SMTP_PORT")
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    receivers = [os.getenv("SMTP_RECEIVERS")]
