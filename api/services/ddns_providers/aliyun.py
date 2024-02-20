from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models

from config import Config
from errors import AliyunDDNSCheckKeyError
from log import logger
from model.record import RecordDDNS
from . import DDNS


class AliyunDDNS(DDNS):

    def __init__(self):
        self.__check_key()
        self.__client = Alidns20150109Client(open_api_models.Config(
            access_key_id=Config.ALIYUN_ACCESSKEY_ID,
            access_key_secret=Config.ALIYUN_ACCESSKEY_SECRET
        ))

    def __check_key(self) -> None:
        if not (Config.ALIYUN_ACCESSKEY_ID and Config.ALIYUN_ACCESSKEY_SECRET):
            logger.error("Alibaba Cloud key error")
            raise AliyunDDNSCheckKeyError

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

    def add_records(self, domain_name: str, rr: str, value: str, type: str, ttl: int) -> bool:
        add_domain_record_request = alidns_20150109_models.AddDomainRecordRequest(
            domain_name=domain_name,
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
            logger.error("Unexpected status code {}".format(response_dict["statusCode"]))
            return False
        RecordDDNS.insert(provider="Aliyun", domain_name=domain_name, rr=rr, type=type, value=value, ttl=ttl)
        logger.info("Domain name resolution added successfully")
        return True

    def update_records(self, record_id: str, domain_name: str, rr: str, value: str, type: str, ttl: int) -> bool:
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
            logger.error("Unexpected status code {}".format(response_dict["statusCode"]))
            return False
        RecordDDNS.insert(provider="Aliyun", domain_name=domain_name, rr=rr, type=type, value=value, ttl=ttl)
        logger.info("Domain name resolution updated successfully")
        return True
