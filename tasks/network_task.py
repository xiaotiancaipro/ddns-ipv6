from celery import shared_task

from log import logger
from model.network import NetworkOperation
from services.email_service import EmailService
from utils.network_util import NetworkUtil


@shared_task
def get_ipv6():
    """Get IPv6 address task"""

    # Get ipv6 address now
    ipv6_address = NetworkUtil.get_ipv6_address_public_one()
    if ipv6_address is None:
        logger.warning("The public ipv6 address was not obtained")
        return
    logger.info(f"Successfully obtained the public ipv6 address, and the address is {ipv6_address}")

    # Get ipv6 address from database
    ipv6_address_db = NetworkOperation.get_ip_addr_latest()
    if ipv6_address_db is None:  # Insert into database and send an email first when the database is null
        NetworkOperation.insert(ipv6_address=ipv6_address)
        EmailService.send(ipv6_address=ipv6_address)
        return
    logger.info(f"Successfully obtained the ipv6 address in database, and the address is {ipv6_address_db}")

    # Do not send email when address has not changed
    if ipv6_address == ipv6_address_db:
        logger.info(f"The ipv6 address is not changed")
        return

    # If ipv6 address has changed, so insert it into the database and send an email
    NetworkOperation.insert(ipv6_address=ipv6_address)
    EmailService.send(ipv6_address=ipv6_address)

    return
