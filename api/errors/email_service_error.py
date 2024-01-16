from . import BaseError


class ConnectError(BaseError):
    message = "ConnectError: Failed to connect to SMTP server"


class LoginError(BaseError):
    message = "LoginError: Failed to login"
