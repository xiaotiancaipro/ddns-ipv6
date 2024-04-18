from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app) -> None:
    db.init_app(app)
    return None
