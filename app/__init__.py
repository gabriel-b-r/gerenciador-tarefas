from flask import Flask
from app.extensions.database import db
from app.extensions.migrate import migrate
from config.settings import DATABASE_URI

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.json.sort_keys = False

    from app.models.task import Task

    from app.routes.task_routes import task_bp
    app.register_blueprint(task_bp)

    return app
