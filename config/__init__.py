import os.path

from dotenv import load_dotenv

from smtp import SMTPConfig
from utils.other import get_project_abspath


class Config(object):
    load_dotenv(os.path.join(get_project_abspath(), ".env"))  # 加载.env文件中的环境变量
