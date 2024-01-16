from flask import Flask
from flask import request
from werkzeug.exceptions import Unauthorized

from config import Config
from extensions import ext_database, ext_celery


def create_app() -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)
    ext_database.init_app(flask_app)
    ext_celery.init_app(flask_app)
    return flask_app


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
    app.run(host='0.0.0.0', port=6001)
