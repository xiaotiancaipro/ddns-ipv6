import os

import dotenv

dotenv.load_dotenv()


def get_env(key) -> str | None:
    return os.environ.get(key, None)


class Config(object):
    """Configuration for the application."""

    APP_ENV = get_env("APP_ENV")

    SYSTEM_SECRET_KEY = get_env("SYSTEM_SECRET_KEY")

    # Redis
    REDIS_PASSWORD = get_env("REDIS_PASSWORD")
    REDIS_HOST = get_env("REDIS_HOST")
    REDIS_PORT = get_env("REDIS_PORT")
    REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"
    CELERY_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/1"
    CELERY_BACKEND_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/2"

    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///data/ipv6.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_size": 30, "pool_recycle": 3600}

    # Email Server
    SMTP_HOST = get_env("SMTP_HOST")
    SMTP_PORT = get_env("SMTP_PORT")
    SMTP_USER = get_env("SMTP_USER")
    SMTP_PASSWORD = get_env("SMTP_PASSWORD")
    EMAIL_SENDER = get_env("EMAIL_SENDER")
    EMAIL_RECEIVERS = get_env("EMAIL_RECEIVERS")
