from config import Config
from log import logger
from utils.smtp_server import SMTPServer


class EmailService(object):
    __smtp = SMTPServer()

    @classmethod
    def send_ipv6(cls, ipv6_address: str) -> bool:
        """Send an email when the database is null"""
        flag = cls.__smtp.send(
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

    @classmethod
    def send_ipv6_not_obtained(cls) -> bool:
        flag = cls.__smtp.send(
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
