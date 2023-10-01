import os
import re

from utils.logger import Logger
from utils.other import get_platform

logger = Logger().get_logger()


def get_global_ipv6_address():
    """获取主机公网 IPv6 地址"""

    # 自定义日志头部
    logger_begin = "[service.ipv6.get_global_ipv6_address] "

    # 定义获取 IP 地址命令字典
    get_ipv6_command_dict = {
        "Linux": "ifconfig",
        "MacOS": "ifconfig",
        "Windows": "ipconfig /all"
    }

    # 通过获取系统平台得到运行获取 IP 地址的命令
    try:
        system_platform = get_platform()
    except Exception as e:
        logger.error(f"{logger_begin}获取系统平台失败")
        logger.error(f"{logger_begin}{e}")
        return None
    get_ipv6_command = get_ipv6_command_dict[system_platform]

    # 运行命令
    try:
        get_ipv6_process = str(os.popen(get_ipv6_command).read())
    except Exception as e:
        logger.error(f"{logger_begin}执行获取 IPv6 命令出错")
        logger.error(f"{logger_begin}{e}")
        return None

    # 解析 IPv6 地址
    try:
        ipv6_address = re.findall(r"(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})", get_ipv6_process, re.I)[0][0]
    except Exception as e:
        logger.error(f"{logger_begin}解析 IPv6 地址出错")
        logger.error(f"{logger_begin}{e}")
        return None

    # 返回 IPv6 地址
    return ipv6_address
