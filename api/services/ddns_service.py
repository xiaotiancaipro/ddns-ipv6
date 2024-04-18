from config import Config
from errors import ProviderCheckError
from log import logger
from services.ddns_providers import DDNS, Providers


class DDNSService(object):

    @staticmethod
    def get_provider() -> DDNS | None:
        if not Config.PROVIDER:
            return None
        if Config.PROVIDER not in Providers.PROVIDERS.keys():
            logger.error("Provider configuration error")
            raise ProviderCheckError
        return Providers.PROVIDERS[Config.PROVIDER]
