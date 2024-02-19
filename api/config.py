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
    DB_USERNAME = get_env("DB_USERNAME")
    DB_PASSWORD = get_env("DB_PASSWORD")
    DB_HOST = get_env("DB_HOST")
    DB_PORT = get_env("DB_PORT")
    DB_DATABASE = get_env("DB_DATABASE")
    SQLALCHEMY_DATABASE_URI = "postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}".format(
        USERNAME=DB_USERNAME,
        PASSWORD=DB_PASSWORD,
        HOST=DB_HOST,
        PORT=DB_PORT,
        DATABASE=DB_DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_size": 30, "pool_recycle": 3600}

    # Email Server
    SMTP_HOST = get_env("SMTP_HOST")
    SMTP_PORT = get_env("SMTP_PORT")
    SMTP_USER = get_env("SMTP_USER")
    SMTP_PASSWORD = get_env("SMTP_PASSWORD")
    EMAIL_SENDER = get_env("EMAIL_SENDER")
    EMAIL_RECEIVER = get_env("EMAIL_RECEIVER")

    # Hostname
    HOSTNAME = get_env("HOSTNAME")

    # DDNS
    DOMAIN_NAME = get_env("DOMAIN_NAME")
    RR = get_env("RR")
    TTL = int(get_env("TTL"))

    # Provider
    PROVIDER = get_env("PROVIDER")

    # Aliyun
    ALIYUN_ACCESSKEY_ID = get_env("ALIYUN_ACCESSKEY_ID")
    ALIYUN_ACCESSKEY_SECRET = get_env("ALIYUN_ACCESSKEY_SECRET")
