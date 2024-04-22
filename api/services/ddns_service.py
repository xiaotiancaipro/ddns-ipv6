from config import Config
from errors.services import ProviderCheckError
from log import logger
from services.ddns_providers import DDNS, PROVIDERS


class DDNSService(object):

    @staticmethod
    def get_provider() -> DDNS | None:
        if not Config.PROVIDER:
            return None
        if Config.PROVIDER not in PROVIDERS.keys():
            logger.error("Provider configuration error")
            raise ProviderCheckError
        return PROVIDERS[Config.PROVIDER]
