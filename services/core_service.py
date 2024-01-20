from log import logger
from utils.network_util import NetworkUtil


class CoreService(object):

    @staticmethod
    def ipv6_to_email():

        # Get ipv6 address
        ipv6_address = NetworkUtil.get_ipv6_address_public_one()
        if ipv6_address is None:
            logger.warning("The public ipv6 address was not obtained")
            return
        logger.info(f"Successfully obtained the public ipv6 address, and the address is {ipv6_address}")

        # # TODO
        #
        # # 判断 data 路径下是否有 IP 地址文件, 若有则获取该地址文件中的 IPv6 地址, 同时比较两个地址是否一致
        # flag = 0  # 0 表示 data 路径下没有 IP 地址文件
        # if ipv6_data_file in get_path_dirs_files(path=ipv6_data_path)[1]:
        #     try:  # 获取 IP 地址文件中的 IPv6 地址
        #         logger.info(f"{logger_begin}正在获取 IP 地址文件中的 IPv6 地址")
        #         file_ipv6_address = get_text_last_line(textfile=ipv6_data).decode("utf-8")
        #         logger.info(f"{logger_begin}已成功获取 IP 地址文件中的 IPv6 地址 -> {file_ipv6_address}")
        #     except Exception as e:
        #         logger.error(f"{logger_begin}获取 IP 地址文件中的 IPv6 地址失败")
        #         logger.error(f"{logger_begin}{e}")
        #         logger.info(f"{logger_begin}执行结束")
        #         return None
        #     flag = 1 if ipv6_address == file_ipv6_address else 2  # 对比两个 IPv6 地址是否一致
        #
        # # 若主机 IPv6 和 IP 地址文件中两个 IPv6 地址一致(flag == 1)则只生成日志
        # if flag == 1:
        #     logger.info(f"{logger_begin}当前系统 IPv6 地址无变化")
        #     logger.info(f"{logger_begin}执行结束")
        #     return not None
        #
        # # 若 IP 地址文件未创建(flag == 0)或者若主机 IPv6 和 IP 地址文件中两个 IPv6 地址不一致(flag == 2)则发送邮件
        #
        # # 将当前 IPv6 地址添加到 IP 地址文件中
        # try:
        #     logger.info(f"{logger_begin}正在将当前 IPv6 地址添加到 IP 地址文件中")
        #     textfile_create(path=os.path.join(ipv6_data_path, ipv6_data_file), text=f"{ipv6_address}\n")
        #     logger.info(f"{logger_begin}当前 IPv6 地址添加成功")
        # except Exception as e:
        #     logger.error(f"{logger_begin}当前 IPv6 地址添加失败")
        #     logger.error(f"{logger_begin}{e}")
        #     logger.info(f"{logger_begin}执行结束")
        #     return None
        #
        # # 发送邮件
        # try:
        #     logger.info(f"{logger_begin}{'正在发送邮件' if flag == 0 else '当前系统 IPv6 地址已变化, 正在发送邮件'}")
        #     email.send(
        #         sender=email_config.get_sender(),
        #         receivers=email_config.get_receivers(),
        #         From=get_hostname(),
        #         To="none",
        #         Subject=f"{get_hostname()} IPv6 地址",
        #         Massage=f"当前 {get_hostname()} 主机的 IPv6 地址为: {ipv6_address}"
        #     )
        #     logger.info(f"{logger_begin}邮件发送成功")
        # except Exception as e:
        #     logger.error(f"{logger_begin}邮件发送失败")
        #     logger.error(f"{logger_begin}{e}")
        #     logger.info(f"{logger_begin}执行结束")
        #     return None
        #
        # logger.info(f"{logger_begin}执行结束")
        # return not None
