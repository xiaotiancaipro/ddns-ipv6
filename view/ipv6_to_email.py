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

ipv6_data_path = f"{get_project_abspath()}/data"
ipv6_data_file = "ipv6.data"
ipv6_data = os.path.join(ipv6_data_path, ipv6_data_file)


def ipv6_to_email():
    """
    获取本主机 IPv6 地址并通过邮件发送到指定收件人

    该函数会检查 data 路径的 IP 地址文件内容,
    当且仅当该文件的最后一行内容与当前主机的 IPv6 地址不一致时才会发送邮件

    该函数适合主机已经开机后使用定时任务执行, 建议十分钟执行一次
    """

    # 自定义日志头部
    logger_begin = "[view.ipv6_to_email] "

    logger.info(f"{logger_begin}执行开始")

    # 获取本主机 IPv6 地址
    logger.info(f"{logger_begin}正在获取本主机 IPv6 地址")
    ipv6_address = get_global_ipv6_address()
    if ipv6_address is None:
        logger.error(f"{logger_begin}无法获取本主机 IPv6 地址")
        logger.info(f"{logger_begin}执行结束")
        return None
    logger.info(f"{logger_begin}已成功获取本主机 IPv6 地址 -> {ipv6_address}")

    # 判断 data 路径下是否有 IP 地址文件, 若有则获取该地址文件中的 IPv6 地址, 同时比较两个地址是否一致
    flag = 0  # 0 表示 data 路径下没有 IP 地址文件
    if ipv6_data_file in get_path_dirs_files(path=ipv6_data_path)[1]:
        try:  # 获取 IP 地址文件中的 IPv6 地址
            logger.info(f"{logger_begin}正在获取 IP 地址文件中的 IPv6 地址")
            file_ipv6_address = get_text_last_line(textfile=ipv6_data).decode("utf-8")
            logger.info(f"{logger_begin}已成功获取 IP 地址文件中的 IPv6 地址 -> {file_ipv6_address}")
        except Exception as e:
            logger.error(f"{logger_begin}获取 IP 地址文件中的 IPv6 地址失败")
            logger.error(f"{logger_begin}{e}")
            logger.info(f"{logger_begin}执行结束")
            return None
        flag = 1 if ipv6_address == file_ipv6_address else 2  # 对比两个 IPv6 地址是否一致

    # 若主机 IPv6 和 IP 地址文件中两个 IPv6 地址一致则只生成日志(flag == 1)
    if flag == 1:
        logger.info(f"{logger_begin}当前系统 IPv6 地址无变化")
        logger.info(f"{logger_begin}执行结束")
        return not None

    # 若 IP 地址文件未创建(flag == 0)或者若主机 IPv6 和 IP 地址文件中两个 IPv6 地址不一致则发送邮件(flag == 2)

    # 将当前 IPv6 地址添加到 IP 地址文件中
    try:
        logger.info(f"{logger_begin}正在将当前 IPv6 地址添加到 IP 地址文件中")
        textfile_create(path=os.path.join(ipv6_data_path, ipv6_data_file), text=f"{ipv6_address}\n")
        logger.info(f"{logger_begin}当前 IPv6 地址添加成功")
    except Exception as e:
        logger.error(f"{logger_begin}当前 IPv6 地址添加失败")
        logger.error(f"{logger_begin}{e}")
        logger.info(f"{logger_begin}执行结束")
        return None

    # 发送邮件
    try:
        logger.info(f"{logger_begin}{'正在发送邮件' if flag == 0 else '当前系统 IPv6 地址已变化, 正在发送邮件'}")
        email.send(
            sender=email_config.sender,
            receivers=email_config.receivers,
            From=get_hostname(),
            To="none",
            Subject=f"{get_hostname()} IPv6 地址",
            Massage=f"当前 {get_hostname()} 主机的 IPv6 地址为: {ipv6_address}"
        )
        logger.info(f"{logger_begin}邮件发送成功")
    except Exception as e:
        logger.info(f"{logger_begin}邮件发送失败")
        logger.info(f"{logger_begin}{e}")
        logger.info(f"{logger_begin}执行结束")
        return None

    logger.info(f"{logger_begin}执行结束")
    return not None


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

    # 获取本主机 IPv6 地址
    logger.info(f"{logger_begin}正在获取本主机 IPv6 地址")
    ipv6_address = get_global_ipv6_address()
    if ipv6_address is None:
        logger.error(f"{logger_begin}无法获取本主机 IPv6 地址")
        logger.info(f"{logger_begin}执行结束")
        return None
    logger.info(f"{logger_begin}已成功获取本主机 IPv6 地址 -> {ipv6_address}")

    # 判断 data 路径下是否有 IP 地址文件, 若有则获取该地址文件中的 IPv6 地址, 同时比较两个地址是否一致
    flag = 0  # 0 表示 data 路径下没有 IP 地址文件
    if ipv6_data_file in get_path_dirs_files(path=ipv6_data_path)[1]:
        try:  # 获取 IP 地址文件中的 IPv6 地址
            logger.info(f"{logger_begin}正在获取 IP 地址文件中的 IPv6 地址")
            file_ipv6_address = get_text_last_line(textfile=ipv6_data).decode("utf-8")
            logger.info(f"{logger_begin}已成功获取 IP 地址文件中的 IPv6 地址 -> {file_ipv6_address}")
        except Exception as e:
            logger.error(f"{logger_begin}获取 IP 地址文件中的 IPv6 地址失败")
            logger.error(f"{logger_begin}{e}")
            logger.info(f"{logger_begin}执行结束")
            return None
        flag = 1 if ipv6_address == file_ipv6_address else 2  # 对比两个 IPv6 地址是否一致

    # 若 IP 地址文件未创建(flag == 0)或者若主机 IPv6 和 IP 地址文件中两个 IPv6 地址不一致(flag == 2)则将当前 IPv6 地址添加到 IP 地址文件中
    if (flag == 0) or (flag == 2):
        try:
            logger.info(f"{logger_begin}正在将当前 IPv6 地址添加到 IP 地址文件中")
            textfile_create(path=os.path.join(ipv6_data_path, ipv6_data_file), text=f"{ipv6_address}\n")
            logger.info(f"{logger_begin}当前 IPv6 地址添加成功")
        except Exception as e:
            logger.error(f"{logger_begin}当前 IPv6 地址添加失败")
            logger.error(f"{logger_begin}{e}")
            logger.info(f"{logger_begin}执行结束")
            return None

    # 发送邮件
    try:
        logger.info(f"{logger_begin}{'正在发送邮件' if flag == 0 else '当前系统 IPv6 地址已变化, 正在发送邮件'}")
        email.send(
            sender=email_config.sender,
            receivers=email_config.receivers,
            From=get_hostname(),
            To="none",
            Subject=f"{get_hostname()} IPv6 地址",
            Massage=f"当前 {get_hostname()} 主机的 IPv6 地址为: {ipv6_address}"
        )
        logger.info(f"{logger_begin}邮件发送成功")
    except Exception as e:
        logger.info(f"{logger_begin}邮件发送失败")
        logger.info(f"{logger_begin}{e}")
        logger.info(f"{logger_begin}执行结束")
        return None

    logger.info(f"{logger_begin}执行结束")
    return not None
