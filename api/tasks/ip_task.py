from celery import shared_task

from config import Config
from log import logger
from model.ip_addr import IPAddr
from services.ddns_service import AliyunDDNS
from services.email_service import EmailService
from services.ip_service import IPService


@shared_task
def update_ipv6():
    """Update IPv6 address task"""

    # Get current and database addresses
    ipv6_address, ipv6_address_db = IPService.get_ipv6_public(), IPService.get_ipv6_db()
    if not (ipv6_address and ipv6_address_db):
        return

    # Do not send email when address has not changed
    if ipv6_address == ipv6_address_db:
        logger.info(f"The ipv6 address is not changed")
        return

    # If ipv6 address has changed, so insert it into the database, send an email and auto-ddns
    flag = EmailService().send_ipv6(ipv6_address=ipv6_address)
    if not flag:
        return
    if Config.DOMAIN_NAME and Config.RR and Config.ALIYUN_ACCESSKEY_ID and Config.ALIYUN_ACCESSKEY_SECRET:
        flag = AliyunDDNS().upgrade_records(
            rr=Config.RR,
            value=ipv6_address,
            type="AAAA",
            ttl=Config.TTL if Config.TTL else 600
        )
        if not flag:
            return
    IPAddr.insert(ipv6_address=ipv6_address)

    return


@shared_task
def schedule_ipv6():
    """Get regularly IPv6 address task"""
    ipv6_address = IPService.get_ipv6_public()  # Get current
    if ipv6_address is None:
        EmailService().send_ipv6_not_obtained()
        return
    EmailService().send_ipv6(ipv6_address=ipv6_address)  # Send an email
    return
