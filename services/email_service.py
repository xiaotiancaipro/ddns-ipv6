from config import Config
from log import logger
from utils.email_util import SMTPServer


class EmailService(object):

    @classmethod
    def send(cls, ipv6_address: str) -> bool:
        """Send an email when the database is null"""
        smtp_server = SMTPServer(
            host=Config.SMTP_HOST,
            port=Config.SMTP_PORT,
            user=Config.SMTP_USER,
            password=Config.SMTP_PASSWORD
        )
        flag = smtp_server.send(
            sender=Config.EMAIL_SENDER,
            receivers=[Config.EMAIL_RECEIVERS],
            From=Config.EMAIL_SENDER,
            To=Config.EMAIL_RECEIVERS,
            Subject="IPv6 Address Acquisition",
            Massage=f"The current IPv6 address of {Config.HOSTNAME} is {ipv6_address}."
        )
        if not flag:
            logger.error(f"Send an email failed, and the IPv6 address now is {ipv6_address}")
            return False
        logger.info("Send an email successfully")
        return True
