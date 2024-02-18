import datetime

from sqlalchemy import BigInteger, Text, DateTime
from sqlalchemy import desc
from sqlalchemy.sql import func

from extensions.ext_database import db
from log import logger


class Network(db.Model):
    __tablename__ = "network"

    id = db.Column(BigInteger, primary_key=True, autoincrement=True)
    ip_addr = db.Column(Text, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.current_timestamp())


class NetworkOperation(object):

    @classmethod
    def insert(cls, ipv6_address: str) -> bool:
        new_network = Network(
            ip_addr=ipv6_address,
            created_at=datetime.datetime.now()
        )
        try:
            db.session.add(new_network)
            db.session.commit()
        except Exception as e:
            logger.error(f"The ipv6 address {ipv6_address} insert into network table failed, and the exception is {e}")
            return False
        return True

    @classmethod
    def get_ip_addr_latest(cls) -> str | None:
        try:
            network = db.session.query(Network).order_by(desc(Network.created_at)).first()
        except Exception as e:
            logger.error(f"Get ipv6 address latest is failed, and the exception is {e}")
            return None
        if not network:
            logger.info("Database is empty")
            return "DIE"
        return network.ip_addr
