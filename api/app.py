from flask import Flask
from flask import request
from werkzeug.exceptions import Unauthorized

from config import Config
from contorllers.ddns import ddns_pb
from extensions import ext_migrate, ext_database, ext_celery
from extensions.ext_database import db


class DDNSIPv6(Flask):
    pass


def create_app() -> Flask:
    app_ = DDNSIPv6(__name__)
    app_.config.from_object(Config)  # configuration
    initialize_extensions(app_)  # middleware
    register_blueprints(app_)  # interface
    return app_


def initialize_extensions(app_: Flask) -> None:
    ext_migrate.init(app_, db)  # database migrate
    ext_database.init_app(app_)  # database
    ext_celery.init_app(app_)  # celery
    return None


def register_blueprints(app_: Flask) -> None:
    app_.register_blueprint(ddns_pb, url_prefix="/v1/ddns")
    return None


app = create_app()
celery = app.extensions["celery"]


@app.before_request
def check_auth():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        raise Unauthorized("You Should Pass Authorization")
    auth_scheme, auth_token = auth_header.split(" ")
    if auth_scheme.lower() != 'bearer':
        raise Unauthorized("Invalid Authorization Format")
    if auth_token != Config.SYSTEM_SECRET_KEY:
        raise Unauthorized("Invalid Authorization Code")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6003)
