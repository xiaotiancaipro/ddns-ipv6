import os

import dotenv

dotenv.load_dotenv()


def get_env(key) -> str | None:
    return os.environ.get(key, None)


class Config(object):
    """Configuration for the application."""

    APP_ENV = get_env("APP_ENV")

    SYSTEM_SECRET_KEY = get_env("SYSTEM_SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = "sqlite://data/ipv6.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_size": 30, "pool_recycle": 3600}

    SMTP_HOST = get_env("SMTP_HOST")
    SMTP_PORT = get_env("SMTP_PORT")
    SMTP_USER = get_env("SMTP_USER")
    SMTP_PASSWORD = get_env("SMTP_PASSWORD")
    EMAIL_SENDER = get_env("EMAIL_SENDER")
    EMAIL_RECEIVERS = get_env("EMAIL_RECEIVERS")
