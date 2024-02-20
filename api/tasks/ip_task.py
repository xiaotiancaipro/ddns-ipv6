from celery import shared_task

from config import Config
from log import logger
from model.ip_addr import IPAddr
from services.ddns_service import DDNSService
from services.email_service import EmailService
from services.ip_service import IPService


@shared_task
def update_ipv6():
    """Update IPv6 address task"""

    # Get current and database addresses
    ipv6_address, ipv6_address_db = IPService.get_current(), IPService.get_database()
    if not (ipv6_address and ipv6_address_db):
        return

    # Do not send email when address has not changed
    if ipv6_address == ipv6_address_db:
        logger.info(f"The ipv6 address is not changed")
        return

    # Perform domain name resolution
    if Config.DOMAIN_NAME and Config.RR and Config.ALIYUN_ACCESSKEY_ID and Config.ALIYUN_ACCESSKEY_SECRET:
        provider = DDNSService.get_provider()
        flag = provider.upgrade_records(
            domain_name=Config.DOMAIN_NAME,
            rr=Config.RR,
            value=ipv6_address,
            type="AAAA",
            ttl=Config.TTL if Config.TTL else 600
        )
        if not flag:
            return

    # Send an email
    flag = EmailService().send_ipv6(ipv6_address=ipv6_address)
    if not flag:
        return

    # Update database
    IPAddr.insert(ipv6_address=ipv6_address)

    return


@shared_task
def schedule_ipv6():
    """Get regularly IPv6 address task"""
    ipv6_address = IPService.get_current()  # Get current
    if ipv6_address is None:
        EmailService().send_ipv6_not_obtained()
        return
    EmailService().send_ipv6(ipv6_address=ipv6_address)  # Send an email
    return
