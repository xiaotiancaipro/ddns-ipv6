import datetime

from sqlalchemy.exc import SQLAlchemyError

from extensions.ext_database import db
from log import logger


class IPDDNS(db.Model):
    __tablename__ = "ip_ddns"
    __table_args__ = (db.PrimaryKeyConstraint("id", name="ip_ddns_pkey"))

    id = db.Column(db.BigInteger)
    ip_addr_id = db.Column(db.BigInteger)
    domain_name = db.Column(db.String(255), nullable=False)
    rr = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    value = db.Column(db.String(255), nullable=False)
    ttl = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))

    @classmethod
    def insert(cls, ip_addr_id: str, domain_name: str, rr: str, type: str, value: str, ttl: int) -> bool:
        """Inserts a new IPv6 address into the database"""
        new_ip_ddns = cls(
            ip_addr_id=ip_addr_id,
            domain_name=domain_name,
            rr=rr,
            type=type,
            value=value,
            ttl=ttl,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        try:
            db.session.add(new_ip_ddns)
            db.session.commit()
        except SQLAlchemyError as e:
            logger.error(f"Domain name resolution insertion into ip_ddns table failed, and the exception is {e}")
            db.session.rollback()
            return False
        return True
