import pytest
from app.services import task_service
from app.exceptions.task_exceptions import TaskNotFoundError, ValidationError

def test_update_task_returns_task_dict(app, created_task):
    created_task

    payload = {
        "title": "Updated task",
        "description": "Testing update",
        "priority": "HIGH",
        "status": "COMPLETED"
    }

    response = task_service.update_task(1, payload)

    assert response == {
        "id": 1,
        "title": "Updated task",
        "description": "Testing update",
        "priority": "HIGH",
        "status": "COMPLETED"
    }


def test_update_task_raises_task_not_found(app, valid_task_payload):
    with pytest.raises(TaskNotFoundError):
        task_service.update_task(1, valid_task_payload)


def test_update_task_with_empty_body_raises_validationerror(app, created_task):
    created_task

    payload = {}

    with pytest.raises(ValidationError):
        task_service.update_task(1, payload)
        