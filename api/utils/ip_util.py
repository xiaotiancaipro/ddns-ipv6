import socket

import psutil

from log import logger


class IPUtil(object):

    @classmethod
    def get_ipv6_address_list(cls) -> list:
        """Get all ipv6 address"""
        interfaces = psutil.net_if_addrs()
        ipv6_addresses_list = list()
        for _, addresses in interfaces.items():
            ipv6_addresses_list += [addr.address for addr in addresses if addr.family == socket.AF_INET6]
        return list(set(ipv6_addresses_list))

    @classmethod
    def get_ipv6_address_public_list(cls) -> list | None:
        """Get all public ipv6 addresses"""
        ipv6_address_list = cls.get_ipv6_address_list()
        if len(ipv6_address_list) <= 0:
            logger.warning("IPv6 list is none")
            return None
        ipv6_addresses_public_list = [
            addr
            for addr in ipv6_address_list
            if all(key not in addr[:4] for key in ["fe80", "::1"])
        ]
        if len(ipv6_addresses_public_list) <= 0:
            logger.warning("No public IP exists")
            return None
        return ipv6_addresses_public_list

    @classmethod
    def get_ipv6_address_public_one(cls) -> str | None:
        """Get a public ipv6 address"""
        ipv6_addresses_public_list = cls.get_ipv6_address_public_list()
        if not isinstance(ipv6_addresses_public_list, list):
            return None
        return ipv6_addresses_public_list[0]
