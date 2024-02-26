from typing import List

from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models

from config import Config
from errors import AliyunDDNSCheckKeyError
from log import logger
from model.record import RecordDDNS
from . import DDNS, DDNSRecord


class AliyunDDNSConfig(object):

    def __init__(self):
        self.__access_key_id = Config.ALIYUN_ACCESSKEY_ID
        self.__access_key_secret = Config.ALIYUN_ACCESSKEY_SECRET
        self.__init_check()

    def __init_check(self):
        if not (self.__access_key_id and self.__access_key_secret):
            logger.error("Alibaba Cloud key error")
            raise AliyunDDNSCheckKeyError

    def access_key_id(self) -> str:
        return self.__access_key_id

    def access_key_secret(self) -> str:
        return self.__access_key_secret


class AliyunDDNS(DDNS):

    def __init__(self):
        self.__aliyun_ddns_config = AliyunDDNSConfig()
        self.__client = Alidns20150109Client(open_api_models.Config(
            access_key_id=self.__aliyun_ddns_config.access_key_id(),
            access_key_secret=self.__aliyun_ddns_config.access_key_secret()
        ))

    def describe_records(self, domain_name: str) -> List[DDNSRecord] | None:
        describe_domain_records_request = alidns_20150109_models.DescribeDomainRecordsRequest(domain_name=domain_name)
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
        result_list = list()
        for record in response_dict["body"]["DomainRecords"]["Record"]:
            ddns_record = DDNSRecord()
            ddns_record.RecordId = record["RecordId"]
            ddns_record.DomainName = record["DomainName"]
            ddns_record.RR = record["RR"]
            ddns_record.TTL = record["TTL"]
            ddns_record.Type = record["Type"]
            ddns_record.Value = record["Value"]
            ddns_record.Status = record["Status"] == "ENABLE"
            result_list.append(ddns_record)
        return result_list

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
