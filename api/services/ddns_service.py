from config import Config
from errors import ProviderCheckError
from log import logger
from services.ddns_providers import DDNS
from services.ddns_providers.aliyun import AliyunDDNS

PROVIDERS = {
    "Aliyun": AliyunDDNS()
}


class DDNSService(object):

    @staticmethod
    def get_provider() -> DDNS | None:
        if Config.PROVIDER not in PROVIDERS.keys():
            logger.error("Provider configuration error")
            raise ProviderCheckError
        return PROVIDERS[Config.PROVIDER]
