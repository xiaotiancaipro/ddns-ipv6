from abc import ABC
from typing import List

from celery import Task, Celery
from flask import Flask

from config import Config
from extensions.ext_celery_beats_dev import dev_beats
from extensions.ext_celery_beats_prod import prod_beats


def init_app(app: Flask) -> None:
    """Celery initialization """

    class FlaskTask(Task, ABC):
        """Use flask app"""

        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    class CeleryBeatsConfig(object):
        """Celery beats configuration"""

        @staticmethod
        def get_beats() -> dict:
            if Config.APP_ENV.lower() == "production":
                return prod_beats
            return dev_beats

        @staticmethod
        def get_task_module() -> List[str]:
            return ["tasks.ip_task"]

    celery_app = Celery(
        main=app.name,
        loader=None,
        backend=app.config["CELERY_BACKEND_URL"],
        amqp=None,
        events=None,
        log=None,
        control=None,
        set_as_current=True,
        tasks=None,
        broker=app.config["CELERY_BROKER_URL"],
        include=CeleryBeatsConfig.get_task_module(),
        changes=None,
        config_source=None,
        fixups=None,
        task_cls=FlaskTask,
        autofinalize=True,
        namespace=None,
        strict_typing=True,
        task_ignore_result=True,
        broker_connection_retry_on_startup=False,
        result_expires=3600,
        timezone="Asia/Shanghai",
        enable_utc=False,
        beat_schedule=CeleryBeatsConfig.get_beats()
    )

    celery_app.set_default()
    app.extensions["celery"] = celery_app

    return None
