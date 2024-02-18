from config import Config
from log import logger
from utils.email_util import SMTPServer


class EmailService(object):
    """Email service"""

    smtp_server = SMTPServer(
        host=Config.SMTP_HOST,
        port=Config.SMTP_PORT,
        user=Config.SMTP_USER,
        password=Config.SMTP_PASSWORD
    )

    @classmethod
    def send_ipv6(cls, ipv6_address: str) -> bool:
        """Send an email when the database is null"""

        flag = cls.smtp_server.send(
            sender=Config.EMAIL_SENDER,
            receivers=[Config.EMAIL_RECEIVERS],
            From=Config.EMAIL_SENDER,
            To=Config.EMAIL_RECEIVERS,
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
        flag = cls.smtp_server.send(
            sender=Config.EMAIL_SENDER,
            receivers=[Config.EMAIL_RECEIVERS],
            From=Config.EMAIL_SENDER,
            To=Config.EMAIL_RECEIVERS,
            Subject="The current IPv6 address was not obtained",
            Message=f"The current IPv6 address of {Config.HOSTNAME} was not obtained"
        )
        if not flag:
            logger.error(f"Send an email failed")
            return False
        logger.info("Send an email successfully")
        return True

    @classmethod
    def send_ipv6_db_not_obtained(cls) -> bool:
        flag = cls.smtp_server.send(
            sender=Config.EMAIL_SENDER,
            receivers=[Config.EMAIL_RECEIVERS],
            From=Config.EMAIL_SENDER,
            To=Config.EMAIL_RECEIVERS,
            Subject="The IPv6 address from database was not obtained",
            Message=f"The IPv6 address of {Config.HOSTNAME} from database was not obtained"
        )
        if not flag:
            logger.error(f"Send an email failed")
            return False
        logger.info("Send an email successfully")
        return True
