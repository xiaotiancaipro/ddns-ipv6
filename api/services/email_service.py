from config import Config
from log import logger
from utils.smtp_server import SMTPServer


class EmailService(object):
    __smtp = SMTPServer(Config.SMTP_HOST, Config.SMTP_PORT, Config.SMTP_USER, Config.SMTP_PASSWORD)
    __smtp_config = {
        "sender": Config.EMAIL_SENDER,
        "receivers": [Config.EMAIL_RECEIVER],
        "From": Config.EMAIL_SENDER,
        "To": Config.EMAIL_RECEIVER,
    }

    @classmethod
    def send_ipv6(cls, ipv6_address: str) -> bool:
        """Send an email when the database is null"""
        cls.__smtp_config["Subject"] = "IPv6 Address Acquisition"
        cls.__smtp_config["Message"] = "\n".join([
            f"Host: {Config.HOSTNAME}"
            f"IPv6 Address: {ipv6_address}"
        ])
        if not cls.__smtp.send(**cls.__smtp_config):
            logger.error(f"Send an email failed, and the IPv6 address now is {ipv6_address}")
            return False
        logger.info("Send an email successfully")
        return True

    @classmethod
    def send_ipv6_not_obtained(cls) -> bool:
        cls.__smtp_config["Subject"] = "The current IPv6 address was not obtained"
        cls.__smtp_config["Message"] = f"The current IPv6 address of {Config.HOSTNAME} was not obtained"
        if not cls.__smtp.send(**cls.__smtp_config):
            logger.error(f"Send an email failed")
            return False
        logger.info("Send an email successfully")
        return True
