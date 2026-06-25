import pytest
from app.services import task_service
from app.exceptions.task_exceptions import ValidationError

def test_create_task_returns_task_dict(app, valid_task_payload):
    with app.app_context():
        response = task_service.create_task(valid_task_payload)

        assert response == {
            "id": 1,
            "title": "Task",
            "description": "Testing",
            "priority": "LOW",
            "status": "PENDING"
            }

def test_create_task_without_title_raises_validationerror(app):
    with app.app_context():
        payload = {}

        with pytest.raises(ValidationError):
            task_service.create_task(payload)

