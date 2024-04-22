from errors.base import BaseError


class SMTPServerConnectError(BaseError):
    message = "SMTPServerConnectError: Failed to connect to SMTP server"


class SMTPServerLoginError(BaseError):
    message = "SMTPServerLoginError: Failed to login"


class TypeError1(BaseError):
    message = "TypeError1: Type is not same"


class SizeError(BaseError):
    message = "SizeError: Length is not same"
