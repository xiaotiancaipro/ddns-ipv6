from abc import ABC

from celery import Task, Celery
from flask import Flask

from config import Config
from extensions.ext_celery_beats_dev import dev_beats
from extensions.ext_celery_beats_prod import prod_beats


def init_app(app: Flask):
    """Celery initialization """

    class FlaskTask(Task, ABC):
        """Use flask app"""

        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    class CeleryBeatsConfig(object):
        """Celery beats configuration"""

        @staticmethod
        def get_beats():
            if Config.APP_ENV.lower() == "production":
                return prod_beats
            return dev_beats

        @staticmethod
        def get_task_module():
            return ["tasks.ip_task"]

    celery_app = Celery(
        app.name,
        task_cls=FlaskTask,
        broker=app.config["CELERY_BROKER_URL"],
        task_ignore_result=True,
        broker_connection_retry_on_startup=False,
        backend=app.config["CELERY_BACKEND_URL"],
        include=CeleryBeatsConfig.get_task_module()
    )

    config = {
        "result_expires": 3600,
        "timezone": 'Asia/Shanghai',
        "enable_utc": False,
        "beat_schedule": CeleryBeatsConfig.get_beats()
    }

    celery_app.conf.update(**config)
    celery_app.set_default()
    app.extensions["celery"] = celery_app
