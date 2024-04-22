class BaseError(Exception):
    """Base error"""

    message: str

    def __init__(self):
        super().__init__(self.message)

    def __str__(self):
        return self.message
