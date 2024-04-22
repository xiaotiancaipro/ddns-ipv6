from errors.base import BaseError


class ProviderCheckError(BaseError):
    message = "ProviderCheckError: Provider configuration error"


class AliyunDDNSCheckKeyError(BaseError):
    message = "AliyunDDNSCheckKeyError: Alibaba Cloud key error"
