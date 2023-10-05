import os

from config import SMTPConfig, EmailConfig
from service.email import Email
from service.ipv6 import get_global_ipv6_address
from utils.file import textfile_create, get_text_last_line
from utils.logger import Logger
from utils.other import get_hostname, get_project_abspath
from utils.path import get_path_dirs_files

logger = Logger().get_logger()
smtp_config = SMTPConfig()
email_config = EmailConfig()
email = Email(host=smtp_config.host, port=int(smtp_config.port), user=smtp_config.user, password=smtp_config.password)


def ipv6_to_email():
    """
    获取本主机 IPv6 地址并通过邮件发送到指定收件人

    该函数会检查 data 路径的 IP 地址文件内容,
    当且仅当该文件的最后一行内容与当前主机的 IPv6 地址不一致时才会发送邮件

    该函数适合主机已经开机后使用定时任务执行
    """

    # 自定义日志头部
    logger_begin = "[view.ipv6_to_email] "

    logger.info(f"{logger_begin}执行开始")

    # 判断 data 路径下是否有 IP 地址文件, 若没有则进行创建
    ipv6_data_path, ipv6_data_file = f"{get_project_abspath()}/data", "ipv6.data"
    if ipv6_data_file not in get_path_dirs_files(path=ipv6_data_path)[1]:
        try:
            logger.info(f"{logger_begin}当前 data 路径下无 IP 地址文件, 正在创建中")
            textfile_create(path=os.path.join(ipv6_data_path, ipv6_data_file), text="ipv6_address")
            logger.info(f"{logger_begin}IP 地址文件创建成功")
        except Exception as e:
            logger.error(f"{logger_begin}IP 地址文件创建失败")
            logger.error(f"{logger_begin}{e}")
            return None

    # 获取本主机 IPv6 地址
    logger.info(f"{logger_begin}正在获取本主机 IPv6 地址")
    ipv6_address = get_global_ipv6_address()
    if ipv6_address is None:
        logger.error(f"{logger_begin}无法获取本主机 IPv6 地址")
        return None
    logger.info(f"{logger_begin}已成功获取本主机 IPv6 地址 -> {ipv6_address}")

    # 获取 IP 地址文件中的 IPv6 地址
    try:
        logger.info(f"{logger_begin}正在获取 IP 地址文件中的 IPv6 地址")
        file_ipv6_address = get_text_last_line(textfile=os.path.join(ipv6_data_path, ipv6_data_file)).decode("utf-8")
        logger.info(f"{logger_begin}已成功获取 IP 地址文件中的 IPv6 地址 -> {file_ipv6_address}")
    except Exception as e:
        logger.error(f"{logger_begin}获取 IP 地址文件中的 IPv6 地址失败")
        logger.error(f"{logger_begin}{e}")
        return None

    # 对比两个 IPv6 地址是否一致
    flag = True if ipv6_address == file_ipv6_address else False

    # 若一致则生成一条日志;
    # 若不一致则生成一条日志并发送邮件"当前系统IPv6地址为: XXXXXXXXXX"
    if flag:
        logger.info(f"{logger_begin}当前系统 IPv6 地址无变化")
    if not flag:
        logger.info(f"{logger_begin}当前系统 IPv6 地址已变化, 正在发送邮件")
        send_flag = email.send(
            sender=email_config.sender,
            receivers=email_config.receivers,
            From=get_hostname(),
            To="none",
            Subject=f"{get_hostname()} IPv6地址",
            Massage=get_hostname() + " 当前系统IPv6地址为: " + ipv6_address
        )
        if not send_flag:
            logger.info(f"{logger_begin}邮件发送失败")
            return None
        logger.info(f"{logger_begin}邮件发送成功")
        try:
            logger.info(f"{logger_begin}正在将当前 IPv6 地址添加到 IP 地址文件中")
            textfile_create(path=os.path.join(ipv6_data_path, ipv6_data_file), text=f"\n{ipv6_address}")
            logger.info(f"{logger_begin}当前 IPv6 地址添加成功")
        except Exception as e:
            logger.error(f"{logger_begin}当前 IPv6 地址添加失败")
            logger.error(f"{logger_begin}{e}")
            return None

    logger.info(f"{logger_begin}执行结束")


def ipv6_to_email_anyway():
    """
    获取本主机 IPv6 地址并通过邮件发送到指定收件人

    该函数不会检查 data 路径的 IP 地址文件内容,
    而是直接获取该主机的 IPv6 地址，并且写入到 data 路径下的 IP 地址文件中，同时发送邮件

    该函数适合主机开机时执行
    """
    # 自定义日志头部
    logger_begin = "[view.ipv6_to_email_anyway] "

    logger.info(f"{logger_begin}执行开始")
