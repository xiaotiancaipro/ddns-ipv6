import smtplib
from email.header import Header
from email.mime.text import MIMEText

from errors import SMTPServerConnectError, SMTPServerLoginError
from log import logger


class SMTPServer(object):

    def __init__(self, host, port, user, password):
        self.__SMTP_object = self.__init_client(host=host, port=port, user=user, password=password)

    def __init_client(self, host: str, port: str | int, user: str, password: str):
        client = smtplib.SMTP()
        try:
            client.connect(host=host, port=int(port))
        except Exception as e:
            logger.error(f"Failed to connect to SMTP server, and the exception is {e}")
            raise SMTPServerConnectError
        try:
            client.login(user=user, password=password)
        except Exception as e:
            logger.error(f"SMTP server user login failed, and the exception is {e}")
            raise SMTPServerLoginError
        return client

    def send(self, sender: str, receivers: list, From: str, To: str, Subject: str, Massage: str) -> bool:
        """Send an email"""
        massage_obj = MIMEText(Massage, _subtype="plain", _charset="utf-8")
        massage_obj["From"] = Header(From, charset="utf-8")
        massage_obj["To"] = Header(To, charset="utf-8")
        massage_obj["Subject"] = Header(Subject, charset="utf-8")
        try:
            self.__SMTP_object.sendmail(from_addr=sender, to_addrs=receivers, msg=massage_obj.as_string())
        except Exception as e:
            logger.error(f"Failed to send, and the exception is {e}")
            return False
        logger.info("Send successfully")
        return True
