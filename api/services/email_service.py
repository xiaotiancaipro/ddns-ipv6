from config import Config
from log import logger
from utils.email_util import SMTPServer


class EmailService(object):

    def __init__(self):
        self.__client = SMTPServer(
            host=Config.SMTP_HOST,
            port=Config.SMTP_PORT,
            user=Config.SMTP_USER,
            password=Config.SMTP_PASSWORD
        )

    def send_ipv6(self, ipv6_address: str) -> bool:
        """Send an email when the database is null"""
        flag = self.__client.send(
            sender=Config.EMAIL_SENDER,
            receivers=[Config.EMAIL_RECEIVER],
            From=Config.EMAIL_SENDER,
            To=Config.EMAIL_RECEIVER,
            Subject="IPv6 Address Acquisition",
            Message=f"The current IPv6 address of {Config.HOSTNAME} is {ipv6_address}."
        )
        if not flag:
            logger.error(f"Send an email failed, and the IPv6 address now is {ipv6_address}")
            return False
        logger.info("Send an email successfully")
        return True

    def send_ipv6_not_obtained(self) -> bool:
        flag = self.__client.send(
            sender=Config.EMAIL_SENDER,
            receivers=[Config.EMAIL_RECEIVER],
            From=Config.EMAIL_SENDER,
            To=Config.EMAIL_RECEIVER,
            Subject="The current IPv6 address was not obtained",
            Message=f"The current IPv6 address of {Config.HOSTNAME} was not obtained"
        )
        if not flag:
            logger.error(f"Send an email failed")
            return False
        logger.info("Send an email successfully")
        return True

    def send_ipv6_db_not_obtained(self) -> bool:
        flag = self.__client.send(
            sender=Config.EMAIL_SENDER,
            receivers=[Config.EMAIL_RECEIVER],
            From=Config.EMAIL_SENDER,
            To=Config.EMAIL_RECEIVER,
            Subject="The IPv6 address from database was not obtained",
            Message=f"The IPv6 address of {Config.HOSTNAME} from database was not obtained"
        )
        if not flag:
            logger.error(f"Send an email failed")
            return False
        logger.info("Send an email successfully")
        return True
