from config import Config
from log import logger
from services.ddns_suppliers import DDNS
from services.ddns_suppliers.aliyun import AliyunDDNS

PROVIDERS = {
    "aliyun": AliyunDDNS()
}


class DDNSService(object):

    @staticmethod
    def get_supplier() -> DDNS | None:
        provider = Config.PROVIDER
        if provider not in PROVIDERS.keys():
            logger.error()
            return None
        return PROVIDERS[provider]
