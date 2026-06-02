from flask import Flask

def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False

    from app.routes.task_routes import task_bp
    app.register_blueprint(task_bp)

    return app
