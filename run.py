from app import create_app
from app.extensions.database import db
from app.models.task import Task

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)