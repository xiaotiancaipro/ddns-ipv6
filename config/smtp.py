import os

from config import Config


class SMTPConfig(Config):
    """配置 SMTP 服务器参数"""

    def __init__(self):

        self.__host = os.getenv("SMTP_HOST")
        self.__port = os.getenv("SMTP_PORT")
        self.__user = os.getenv("SMTP_USER")
        self.__password = os.getenv("SMTP_PASSWORD")

        if not self.__host:
            raise Exception("SMTP 服务器参数 host 为空")
        if not self.__port:
            raise Exception("SMTP 服务器参数 port 为空")
        if not self.__user:
            raise Exception("SMTP 服务器参数 user 为空")
        if not self.__password:
            raise Exception("SMTP 服务器参数 password 为空")

    def host(self):
        return self.__host

    def port(self):
        return int(self.__port)

    def user(self):
        return self.__user

    def password(self):
        return self.__password
