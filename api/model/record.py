import datetime

from sqlalchemy.exc import SQLAlchemyError

from extensions.ext_database import db
from log import logger


class RecordDDNS(db.Model):
    __tablename__ = "record_ddns"
    __table_args__ = (db.PrimaryKeyConstraint("id", name="record_ddns_pkey"),)

    id = db.Column(db.BigInteger, autoincrement=True)
    provider = db.Column(db.String(20), nullable=False)
    domain_name = db.Column(db.String(255), nullable=False)
    rr = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    value = db.Column(db.String(255), nullable=False)
    ttl = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))

    @classmethod
    def insert(cls, provider: str, domain_name: str, rr: str, type: str, value: str, ttl: int) -> int | None:
        new_record_ddns = cls(
            provider=provider,
            domain_name=domain_name,
            rr=rr,
            type=type,
            value=value,
            ttl=ttl,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        try:
            db.session.add(new_record_ddns)
            db.session.commit()
        except SQLAlchemyError as e:
            logger.error(f"DDNS record failed, and the exception is {e}")
            db.session.rollback()
            return None
        return new_record_ddns.id


class RecordEmail(db.Model):
    __tablename__ = "record_email"
    __table_args__ = (db.PrimaryKeyConstraint("id", name="record_email_pkey"),)

    id = db.Column(db.BigInteger, autoincrement=True)
    sender = db.Column(db.String(255), nullable=False)
    receiver = db.Column(db.String(255), nullable=False)
    from_ = db.Column(db.String(255), nullable=False)
    to_ = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.Text, nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))

    @classmethod
    def insert(cls, sender: str, receiver: str, from_: str, to_: str, subject: str, message: str) -> int | None:
        new_record_email = cls(
            sender=sender,
            receiver=receiver,
            from_=from_,
            to_=to_,
            subject=subject,
            message=message,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        try:
            db.session.add(new_record_email)
            db.session.commit()
        except SQLAlchemyError as e:
            logger.error(f"Email record failed, and the exception is {e}")
            db.session.rollback()
            return None
        return new_record_email.id
