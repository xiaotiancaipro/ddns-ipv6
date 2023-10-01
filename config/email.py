import os

from config import Config


class EmailConfig(Config):
    """配置邮件参数"""

    sender = os.getenv("EMAIL_SENDER")
    receivers = [os.getenv("EMAIL_RECEIVERS")]
