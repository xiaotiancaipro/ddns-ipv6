from config import Config
from ddns_providers import DDNS, PROVIDERS
from errors.services import ProviderCheckError
from log import logger


class DDNSService(object):

    @staticmethod
    def get_provider() -> DDNS | None:
        if not Config.PROVIDER:
            return None
        if Config.PROVIDER not in PROVIDERS.keys():
            logger.error("Provider configuration error")
            raise ProviderCheckError
        return PROVIDERS[Config.PROVIDER]
