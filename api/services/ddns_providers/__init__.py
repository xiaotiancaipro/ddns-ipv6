from abc import ABC, abstractmethod

from log import logger


class DDNS(ABC):

    @abstractmethod
    def describe_records(self, domain_name: str) -> list | None:
        """
        [
            {
                "RecordId": str,
                "DomainName": str,
                "RR": str,
                "TTL": int,
                "Type": str,
                "Value": str,
                "Status": bool
            },
        ]
        """
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
        for RecordId, DomainName, RR, TTL, Type, Value, Status in self.__to_tuple(describe_records=records_list):
            if (
                    (DomainName == domain_name) and
                    (RR == rr) and
                    (Value == value) and
                    (Type == type) and
                    (TTL == ttl)
            ):
                logger.info("The DNS record already exists")
                return True
            if (DomainName == domain_name) and (RR == rr):
                upgrade_id = RecordId
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

    def __to_tuple(self, describe_records: list):
        return [
            (item["RecordId"], item["DomainName"], item["RR"], item["TTL"], item["Type"], item["Value"], item["Status"])
            for item in describe_records
        ]
