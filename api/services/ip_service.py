from log import logger
from model.network import NetworkOperation
from utils.network_util import NetworkUtil


class IPService(object):

    @classmethod
    def get_ipv6_public(cls) -> str | None:
        """Get ipv6 address now"""
        ipv6_address = NetworkUtil.get_ipv6_address_public_one()
        if ipv6_address is None:
            logger.warning("The public ipv6 address was not obtained")
            return None
        logger.info(f"Successfully obtained the public ipv6 address, and the address is {ipv6_address}")
        return ipv6_address

    @classmethod
    def get_ipv6_db(cls) -> str | None:
        """Get ipv6 address from database"""
        ipv6_address_db = NetworkOperation.get_ip_addr_latest()
        if ipv6_address_db is None:
            return None
        if ipv6_address_db == "DIE":
            return "DIE"
        logger.info(f"Successfully obtained the ipv6 address in database, and the address is {ipv6_address_db}")
        return ipv6_address_db
