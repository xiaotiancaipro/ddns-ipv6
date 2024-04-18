from abc import ABC
from typing import List

from . import DDNS, DDNSRecord


class BaiduDDNS(DDNS, ABC):

    def describe_records(self, domain_name: str) -> List[DDNSRecord] | None:
        pass

    def add_records(self, domain_name: str, rr: str, value: str, type: str, ttl: int) -> bool:
        pass

    def upgrade_records(self, domain_name: str, rr: str, value: str, type: str, ttl: int) -> bool:
        pass
