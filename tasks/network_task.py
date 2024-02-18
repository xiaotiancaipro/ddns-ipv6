from celery import shared_task

from log import logger
from model.network import NetworkOperation
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

    # If ipv6 address has changed, so insert it into the database and send an email
    NetworkOperation.insert(ipv6_address=ipv6_address)
    EmailService.send_ipv6(ipv6_address=ipv6_address)

    return


@shared_task
def schedule_ipv6():
    """Get regularly IPv6 address task"""

    # Get current and database addresses
    ipv6_address, ipv6_address_db = IPService.get_ipv6_public(), IPService.get_ipv6_db()
    if ipv6_address is None:
        EmailService.send_ipv6_not_obtained()
        return
    if ipv6_address_db is None:
        EmailService.send_ipv6_db_not_obtained()
        return

    # Insert into database when the ipv6 address has changed
    if ipv6_address != ipv6_address_db:
        NetworkOperation.insert(ipv6_address=ipv6_address)

    # Send an email
    EmailService.send_ipv6(ipv6_address=ipv6_address)

    return
