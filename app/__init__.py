def create_app():
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def inicio():
        return '<h1>Olá, mundo!</h1>'

    return app