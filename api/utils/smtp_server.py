import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from errors.utils import SMTPServerConnectError, SMTPServerLoginError
from log import logger
from model.record import RecordEmail


class SMTPServer(object):

    def __init__(
            self,
            host: str,
            port: int | str,
            user: str,
            password: str
    ):
        self.__client = smtplib.SMTP()
        try:
            self.__client.connect(host=host, port=int(port))
        except Exception as e:
            logger.error(f"Failed to connect to SMTP server, and the exception is {e}")
            raise SMTPServerConnectError
        try:
            self.__client.login(user=user, password=password)
        except Exception as e:
            logger.error(f"SMTP server user login failed, and the exception is {e}")
            raise SMTPServerLoginError

    def send(self, sender: str, receivers: list, From: str, To: str, Subject: str, Message: str) -> bool:
        """Send an email"""
        message_obj = MIMEText(Message, _subtype="plain", _charset="utf-8")
        message_obj["From"] = Header(From, charset="utf-8")
        message_obj["To"] = Header(To, charset="utf-8")
        message_obj["Subject"] = Header(Subject, charset="utf-8")
        try:
            self.__client.sendmail(from_addr=sender, to_addrs=receivers, msg=message_obj.as_string())
        except Exception as e:
            logger.error(f"Failed to send, and the exception is {e}")
            return False
        RecordEmail.insert(
            sender=sender,
            receiver=json.dumps(receivers, ensure_ascii=False),
            from_=From,
            to_=To,
            subject=Subject,
            message=Message
        )
        return True
