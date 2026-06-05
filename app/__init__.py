from flask import Flask
from app.extensions.database import db
from config.settings import DATABASE_URI

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.json.sort_keys = False

    from app.routes.task_routes import task_bp
    app.register_blueprint(task_bp)

    return app
