import pytest
from app.services import task_service
from app.exceptions.task_exceptions import TaskNotFoundError, ValidationError

def test_patch_task_returns_task_dict(app, created_task):
    with app.app_context():
        created_task

    payload = {"title": "Test"}

    response = task_service.patch_task(1, payload)

    assert response == {
        "id": 1,
        "title": "Test",
        "description": "Testing",
        "priority": "LOW",
        "status": "PENDING"
    }


def test_patch_task_raises_task_not_found(app, valid_task_payload):
    with app.app_context():
        with pytest.raises(TaskNotFoundError):
            task_service.patch_task(1, valid_task_payload)


def test_patch_task_with_empty_body_raises_validationerror(app, created_task):
    with app.app_context():
        created_task

        payload = {}

        with pytest.raises(ValidationError):
            task_service.patch_task(1, payload)


def test_patch_task_without_valid_fields_raises_validationerror(app, created_task):
    with app.app_context():
        created_task

        payload = {"not valid": "test"}

        with pytest.raises(ValidationError):
            task_service.patch_task(1, payload)
