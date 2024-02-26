from abc import ABC, abstractmethod
from typing import List

from log import logger


class DDNSRecord(object):
    RecordId: str
    DomainName: str
    RR: str
    TTL: int
    Type: str
    Value: str
    Status: bool


class DDNS(ABC):

    @abstractmethod
    def describe_records(self, domain_name: str) -> List[DDNSRecord] | None:
        pass

    @abstractmethod
    def add_records(self, domain_name: str, rr: str, value: str, type: str, ttl: int) -> bool:
        pass

    @abstractmethod
    def update_records(self, record_id: str, domain_name: str, rr: str, value: str, type: str, ttl: int) -> bool:
        pass

    def upgrade_records(self, domain_name: str, rr: str, value: str, type: str, ttl: int) -> bool:

        records_list = self.describe_records(domain_name=domain_name)
        if records_list is None:
            logger.error("Get all DNS records error")
            return False
        if len(records_list) <= 0:
            return self.add_records(domain_name=domain_name, rr=rr, value=value, type=type, ttl=ttl)

        upgrade_id = None
        for record in records_list:
            if (
                    (record.DomainName == domain_name) and
                    (record.RR == rr) and
                    (record.Value == value) and
                    (record.Type == type) and
                    (record.TTL == ttl)
            ):
                logger.info("The DNS record already exists")
                return True
            if (record.DomainName == domain_name) and (record.RR == rr):
                upgrade_id = record.RecordId
                break
        if upgrade_id is None:
            return self.add_records(domain_name=domain_name, rr=rr, value=value, type=type, ttl=ttl)
        return self.update_records(
            record_id=upgrade_id,
            domain_name=domain_name,
            rr=rr,
            value=value,
            type=type,
            ttl=ttl
        )
