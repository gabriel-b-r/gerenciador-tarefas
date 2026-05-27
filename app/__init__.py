def create_app():
    from flask import Flask
    app = Flask(__name__)

    from app.routes.task_routes import task_bp
    app.register_blueprint(task_bp)

    return app
