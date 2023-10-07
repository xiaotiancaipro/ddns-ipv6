import os

from config import Config


class EmailConfig(Config):
    """配置邮件参数"""

    def __init__(self):
        self.__sender = os.getenv("EMAIL_SENDER"),
        self.__receivers = [os.getenv("EMAIL_RECEIVERS")]
        if self.__sender is None:
            raise Exception("发件人配置信息为空")
        if self.__receivers is None:
            raise Exception("收件人配置信息为空")

    def sender(self):
        return self.__sender

    def receivers(self):
        return self.__receivers
