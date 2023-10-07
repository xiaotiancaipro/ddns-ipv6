import os

from config import Config


class EmailConfig(Config):
    """配置邮件参数"""

    def __init__(self):
        self.__configuration_dict = {
            "sender": os.getenv("EMAIL_SENDER"),
            "receivers": os.getenv("EMAIL_RECEIVERS")
        }
        for key in self.__configuration_dict.keys():
            if self.__configuration_dict[key] == "":
                raise Exception(f"Email 配置参数 {key} 为空")

    def get_sender(self):
        return self.__configuration_dict["sender"]

    def get_receivers(self):
        return [self.__configuration_dict["receivers"]]
