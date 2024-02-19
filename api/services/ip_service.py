from log import logger
from model.ip_addr import IPAddr
from utils.ip_util import IPUtil


class IPService(object):

    @classmethod
    def get_ipv6_public(cls) -> str | None:
        """Get ipv6 address now"""
        ipv6_address = IPUtil.get_ipv6_address_public_one()
        if ipv6_address is None:
            logger.warning("The public ipv6 address was not obtained")
            return None
        logger.info(f"Successfully obtained the public ipv6 address, and the address is {ipv6_address}")
        return ipv6_address

    @classmethod
    def get_ipv6_db(cls) -> str | None:
        """Get ipv6 address from database"""
        ipv6_address_db = IPAddr.get_latest()
        if ipv6_address_db in [None, "DIE"]:
            return ipv6_address_db
        logger.info(f"Successfully obtained the ipv6 address in database, and the address is {ipv6_address_db}")
        return ipv6_address_db
