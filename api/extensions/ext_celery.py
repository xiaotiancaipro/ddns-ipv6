from abc import ABC

from celery import Task, Celery
from flask import Flask

from config import Config
from extensions.ext_celery_beats_dev import dev_beats
from extensions.ext_celery_beats_prod import prod_beats


def init_app(app: Flask):
    class FlaskTask(Task, ABC):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    class CeleryConfig:
        result_expires = 3600
        timezone = "Asia/Shanghai"

    class CeleryBeatsConfig(object):
        @staticmethod
        def get_beats():
            if Config.APP_ENV.lower() == "prod":
                return prod_beats
            return dev_beats

    celery_app = Celery(
        app.name,
        task_cls=FlaskTask,
        broker=app.config["CELERY_BROKER_URL"],
        task_ignore_result=True,
        broker_connection_retry_on_startup=False,
        backend=app.config["CELERY_BACKEND_URL"],
        config_source=CeleryConfig,
        include=["tasks.news_tasks"]
    )

    celery_app.set_default()
    celery_app.conf.enable_utc = False
    celery_app.conf.beat_schedule = CeleryBeatsConfig.get_beats()
    app.extensions["celery"] = celery_app
