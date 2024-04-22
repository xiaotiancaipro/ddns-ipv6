from config import Config
from log import logger
from utils.smtp_server import SMTPServer
from utils.string_util import StringUtil

MESSAGE_1 = """\
Host: {{host}}
IPv6: {{ipv6_address}}\
"""

MESSAGE_2 = """\
Host: {{host}}
IPv6: Not Obtained\
"""


class EmailService(object):
    __smtp = SMTPServer(Config.SMTP_HOST, Config.SMTP_PORT, Config.SMTP_USER, Config.SMTP_PASSWORD)
    __smtp_config = {
        "sender": Config.EMAIL_SENDER,
        "receivers": [Config.EMAIL_RECEIVER],
        "From": Config.EMAIL_SENDER,
        "To": Config.EMAIL_RECEIVER,
        "Subject": "DDNS-IPv6"
    }

    @classmethod
    def send_ipv6(cls, ipv6_address: str) -> bool:
        """Send an email when the database is null"""
        cls.__smtp_config["Message"] = StringUtil.replace_(
            string=MESSAGE_1,
            old=["{{host}}", "{{ipv6_address}}"],
            new=[Config.HOSTNAME, ipv6_address]
        )
        if not cls.__smtp.send(**cls.__smtp_config):
            logger.error(f"Send an email failed, and the IPv6 address now is {ipv6_address}")
            return False
        logger.info("Send an email successfully")
        return True

    @classmethod
    def send_ipv6_not_obtained(cls) -> bool:
        cls.__smtp_config["Message"] = StringUtil.replace_(string=MESSAGE_2, old=["{{host}}"], new=[Config.HOSTNAME])
        if not cls.__smtp.send(**cls.__smtp_config):
            logger.error(f"Send an email failed")
            return False
        logger.info("Send an email successfully")
        return True
