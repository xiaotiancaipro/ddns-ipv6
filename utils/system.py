import socket
import sys


def get_hostname():
    """获取当前系统主机名"""
    return socket.gethostname()


def get_platform():
    """
    获取本机操作系统平台

    该函数返回一个字符串: Linux; MacOS; Windows
    """

    logger_begin = "[utils.other.get_platform] "

    platform_dict = {
        "linux": "Linux",
        "darwin": "MacOS",
        "win32": "Windows"
    }

    sys_platform = sys.platform
    if sys_platform not in platform_dict.keys():
        raise Exception(f"{logger_begin}获取本机操作系统平台失败")

    return platform_dict[sys_platform]
