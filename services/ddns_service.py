from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models

from config import Config
from log import logger
from abc import ABC, abstractmethod


class DDNS(ABC):

    @abstractmethod
    def describe_records(self) -> list | None:
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
    def add_records(self, rr: str, value: str, type: str, ttl: int) -> bool:
        pass

    @abstractmethod
    def update_records(self, record_id: str, rr: str, value: str, type: str, ttl: int) -> bool:
        pass

    def upgrade_records(self, rr: str, value: str, type: str, ttl: int) -> bool:
        records_list = self.describe_records()
        if records_list is None:
            logger.error("Get all records error")
            return False
        if len(records_list) <= 0:
            return self.add_records(rr=rr, value=value, type=type, ttl=ttl)
        records_list = [record["RR"] for record in records_list if record["RecordId"] and record["RR"]]
        if rr not in records_list:
            return self.add_records(rr=rr, value=value, type=type, ttl=ttl)
        upgrade_id = None
        for record in records_list:
            if record["RR"] == rr:
                upgrade_id = record["RecordId"]
                break
        if upgrade_id is None:
            return self.add_records(rr=rr, value=value, type=type, ttl=ttl)
        return self.update_records(record_id=upgrade_id, rr=rr, value=value, type=type, ttl=ttl)


class AliyunDDNS(DDNS):

    def __init__(self):
        self.__client = None
        self.__init_client()

    def __init_client(self) -> None:
        aliyun_config = open_api_models.Config(
            access_key_id=Config.ALIYUN_ACCESSKEY_ID,
            access_key_secret=Config.ALIYUN_ACCESSKEY_SECRET
        )
        self.__client = Alidns20150109Client(aliyun_config)

    def describe_records(self) -> list | None:
        describe_domain_records_request = alidns_20150109_models.DescribeDomainRecordsRequest(
            domain_name=Config.DOMAIN_NAME
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = self.__client.describe_domain_records_with_options(describe_domain_records_request, runtime)
        except Exception as e:
            logger.error(e)
            return None
        response_dict = response.to_map()
        if response_dict["statusCode"] != 200:
            logger.error("Unexpected status code {}".format(response_dict["statusCode"]))
            return None
        if response_dict["body"]["TotalCount"] <= 0:
            return list()
        return [{
            "RecordId": record["RecordId"],
            "DomainName": record["DomainName"],
            "RR": record["RR"],
            "TTL": record["TTL"],
            "Type": record["Type"],
            "Value": record["Value"],
            "Status": record["Status"] == "ENABLE"
        } for record in response_dict["body"]["DomainRecords"]["Record"]]

    def add_records(self, rr: str, value: str, type: str, ttl: int) -> bool:
        add_domain_record_request = alidns_20150109_models.AddDomainRecordRequest(
            domain_name=Config.DOMAIN_NAME,
            rr=rr,
            value=value,
            type=type,
            ttl=ttl
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = self.__client.add_domain_record_with_options(add_domain_record_request, runtime)
        except Exception as e:
            logger.error(e)
            return False
        response_dict = response.to_map()
        if response_dict["statusCode"] != 200:
            return False
        return True

    def update_records(self, record_id: str, rr: str, value: str, type: str, ttl: int) -> bool:
        update_domain_record_request = alidns_20150109_models.UpdateDomainRecordRequest(
            record_id=record_id,
            rr=rr,
            value=value,
            type=type,
            ttl=ttl
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = self.__client.update_domain_record_with_options(update_domain_record_request, runtime)
        except Exception as e:
            logger.error(e)
            return False
        response_dict = response.to_map()
        if response_dict["statusCode"] != 200:
            return False
        return True
