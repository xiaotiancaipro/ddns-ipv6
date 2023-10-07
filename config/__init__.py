import os.path

from dotenv import load_dotenv

from utils.path import get_project_abspath


class Config(object):
    load_dotenv(os.path.join(get_project_abspath(), ".env"))  # 加载.env文件中的环境变量


from config.smtp import SMTPConfig
from config.email import EmailConfig
