import datetime

from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError

from extensions.ext_database import db
from log import logger


class IPAddr(db.Model):
    __tablename__ = "ip_addr"
    __table_args__ = (db.PrimaryKeyConstraint("id", name="ip_addr_pkey"),)

    id = db.Column(db.BigInteger, autoincrement=True)
    addr = db.Column(db.String(39), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))

    @classmethod
    def insert(cls, ipv6_address: str) -> bool:
        """Inserts a new IPv6 address into the database"""
        new_ip_addr = cls(
            addr=ipv6_address,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        try:
            db.session.add(new_ip_addr)
            db.session.commit()
        except SQLAlchemyError as e:
            logger.error(f"The ipv6 address {ipv6_address} insert into ip_addr table failed, and the exception is {e}")
            db.session.rollback()
            return False
        return True

    @classmethod
    def get_latest(cls) -> str | None:
        """Retrieves the latest IPv6 address from the database"""
        try:
            network = db.session.query(cls).order_by(desc(cls.created_at)).first()
        except SQLAlchemyError as e:
            logger.error(f"Get ipv6 address latest is failed, and the exception is {e}")
            return None
        return network.addr if network else "DIE"  # "DIE" -> Database is empty
