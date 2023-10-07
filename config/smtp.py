import os

from config import Config


class SMTPConfig(Config):
    """配置 SMTP 服务器参数"""

    def __init__(self):
        self.__configuration_dict = {
            "host": os.getenv("SMTP_HOST"),
            "port": os.getenv("SMTP_PORT"),
            "user": os.getenv("SMTP_USER"),
            "password": os.getenv("SMTP_PASSWORD")
        }
        for key in self.__configuration_dict.keys():
            if self.__configuration_dict[key] == "":
                raise Exception(f"SMTP 服务器参数 {key} 为空")

    def host(self):
        return self.__configuration_dict["host"]

    def port(self):
        return int(self.__configuration_dict["port"])

    def user(self):
        return self.__configuration_dict["user"]

    def password(self):
        return self.__configuration_dict["password"]
