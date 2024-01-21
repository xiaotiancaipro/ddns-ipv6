import os

import dotenv

dotenv.load_dotenv()


def get_env(key) -> str | None:
    return os.environ.get(key, None)


class Config(object):
    """Configuration for the application."""

    APP_ENV = get_env("APP_ENV")

    # Redis
    REDIS_PASSWORD = get_env("REDIS_PASSWORD")
    REDIS_HOST = get_env("REDIS_HOST")
    REDIS_PORT = get_env("REDIS_PORT")
    REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/3"
    CELERY_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/4"
    CELERY_BACKEND_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/5"

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

    # Hostname
    HOSTNAME = get_env("HOSTNAME")

    # Email Server
    SMTP_HOST = get_env("SMTP_HOST")
    SMTP_PORT = get_env("SMTP_PORT")
    SMTP_USER = get_env("SMTP_USER")
    SMTP_PASSWORD = get_env("SMTP_PASSWORD")
    EMAIL_SENDER = get_env("EMAIL_SENDER")
    EMAIL_RECEIVERS = get_env("EMAIL_RECEIVERS")
