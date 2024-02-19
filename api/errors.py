class BaseError(Exception):
    """Base error"""

    message: str

    def __init__(self):
        super().__init__(self.message)

    def __str__(self):
        return self.message


class SMTPServerConnectError(BaseError):
    message = "SMTPServerConnectError: Failed to connect to SMTP server"


class SMTPServerLoginError(BaseError):
    message = "SMTPServerLoginError: Failed to login"


class ProviderCheckError(BaseError):
    message = "ProviderCheckError: Provider configuration error"


class AliyunDDNSCheckKeyError(BaseError):
    message = "AliyunDDNSCheckKeyError: Alibaba Cloud key error"
