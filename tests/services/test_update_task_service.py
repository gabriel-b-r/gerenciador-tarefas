import pytest
from app.services import task_service
from app.exceptions.task_exceptions import TaskNotFoundError, ValidationError

def test_update_task_returns_task_dict(app, created_task, valid_task_payload):
    with app.app_context():
        created_task
    
        response = task_service.update_task(1, valid_task_payload)

        assert response == {
            "id": 1,
            "title": "Task",
            "description": "Testing",
            "priority": "LOW",
            "status": "PENDING"
        }


def test_update_task_raises_task_not_found(app, valid_task_payload):
    with app.app_context():
        with pytest.raises(TaskNotFoundError):
            task_service.update_task(1, valid_task_payload)


def test_update_task_without_title_raises_validationerror(app, created_task):
    with app.app_context():
        created_task

        payload = {
            "description": "Testing",
            "priority": "LOW",
            "status": "PENDING"
        }

        with pytest.raises(ValidationError):
            task_service.update_task(1, payload)
    