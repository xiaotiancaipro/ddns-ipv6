import smtplib
from email.header import Header
from email.mime.text import MIMEText

from utils.logger import Logger

logger = Logger().get_logger()


class Email(object):

    def __init__(self, host, port, user, password):
        """
        配置 SMTP 服务器参数

        :param host: SMTP 服务器主机名
        :param port: SMTP 服务器端口号
        :param user: 用户名
        :param password: 密码(口令)
        """

        logger_begin = "[service.mail.Email.__init__] "

        self.__SMTP_object = smtplib.SMTP()

        try:
            self.__SMTP_object.connect(host=host, port=port)
        except Exception as e:
            logger.error(f"{logger_begin}连接 SMTP 服务器失败")
            logger.error(f"{logger_begin}{e}")
            raise Exception(f"{logger_begin}连接 SMTP 服务器失败")

        try:
            self.__SMTP_object.login(user=user, password=password)
        except Exception as e:
            logger.error(f"{logger_begin}SMTP 服务器用户登录失败")
            logger.error(f"{logger_begin}{e}")
            raise Exception(f"{logger_begin}SMTP 服务器用户登录失败")

    def send(self, sender, receivers, From, To, Subject, Massage):
        """
        发送邮件

        :param sender: 发送者
        :param receivers: 接收者, 这是一个列表类型
        :param From: 发送方描述
        :param To: 接收方描述
        :param Subject: 邮件主题
        :param Massage: 邮件内容
        """

        logger_begin = "[service.mail.Email.send] "

        massage_obj = MIMEText(Massage, _subtype="plain", _charset="utf-8")
        massage_obj["From"] = Header(From, charset="utf-8")
        massage_obj["To"] = Header(To, charset="utf-8")
        massage_obj["Subject"] = Header(Subject, charset="utf-8")

        try:
            self.__SMTP_object.sendmail(from_addr=sender, to_addrs=receivers, msg=massage_obj.as_string())
        except Exception as e:
            logger.error(f"{logger_begin}发送邮件失败")
            logger.error(f"{logger_begin}{e}")
            return None

        return not None
