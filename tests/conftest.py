import pytest
from app import create_app
from app.models.task import Task
from app.extensions.database import db

@pytest.fixture
def app():

    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False 
    }

    app = create_app(test_config=test_config)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def created_task(app):
    task = Task(
        title="Task",
        description="Testing",
        priority="LOW",
        status="PENDING"
    )

    db.session.add(task)
    db.session.commit()

    return task


@pytest.fixture
def valid_task_payload():
    return {
        "title": "Task",
        "description": "Testing",
        "priority": "LOW",
        "status": "PENDING"
    }
