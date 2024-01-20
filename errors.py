class BaseError(Exception):
    """Base error"""

    message: str

    def __init__(self):
        super().__init__(self.message)

    def __str__(self):
        return self.message


class BaseErrorCondition(Exception):
    """Base error by condition"""

    def __init__(self, message: str):
        self.__message = message
        super().__init__(self.__message)

    def __str__(self):
        return self.__message


class SMTPServerConnectError(BaseError):
    message = "SMTPServerConnectError: Failed to connect to SMTP server"


class SMTPServerLoginError(BaseError):
    message = "SMTPServerLoginError: Failed to login"


class NetworkTableIsNull(BaseError):
    message = "NetworkTableIsNull: The network table is null"
