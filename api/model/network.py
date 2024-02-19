import datetime

from sqlalchemy import BigInteger, Text, DateTime
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func

from extensions.ext_database import db
from log import logger


class Network(db.Model):
    __tablename__ = "network"

    id = db.Column(BigInteger, primary_key=True, autoincrement=True)
    ip_addr = db.Column(Text, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.current_timestamp())

    @classmethod
    def insert(cls, ipv6_address: str) -> bool:
        """Inserts a new IPv6 address into the database"""
        new_network = cls(
            ip_addr=ipv6_address,
            created_at=datetime.datetime.now()
        )
        try:
            db.session.add(new_network)
            db.session.commit()
        except SQLAlchemyError as e:
            logger.error(f"The ipv6 address {ipv6_address} insert into network table failed, and the exception is {e}")
            db.session.rollback()
            return False
        return True

    @classmethod
    def get_ip_addr_latest(cls) -> str | None:
        """Retrieves the latest IPv6 address from the database"""
        try:
            network = db.session.query(cls).order_by(desc(cls.created_at)).first()
        except SQLAlchemyError as e:
            logger.error(f"Get ipv6 address latest is failed, and the exception is {e}")
            return None
        return network.ip_addr if network else "DIE"  # "DIE" -> Database is empty
