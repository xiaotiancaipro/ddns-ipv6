import flask_migrate


def init(app, db) -> None:
    flask_migrate.Migrate(app, db)
    return None
