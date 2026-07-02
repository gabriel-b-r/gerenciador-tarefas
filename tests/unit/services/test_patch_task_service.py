import pytest
from app.services import task_service
from app.exceptions.task_exceptions import TaskNotFoundError, ValidationError

def test_patch_task_update_1_value_returns_task_dict(app, created_task):
    created_task

    payload = {"title": "Test patch"}

    response = task_service.patch_task(1, payload)

    assert response == {
        "id": 1,
        "title": "Test patch",
        "description": "Testing",
        "priority": "LOW",
        "status": "PENDING"
    }


def test_patch_task_update_2_values_returns_task_dict(app, created_task):
    created_task

    payload = {
        "title": "Test patch",
        "priority": "HIGH"
    }

    response = task_service.patch_task(1, payload)

    assert response == {
        "id": 1,
        "title": "Test patch",
        "description": "Testing",
        "priority": "HIGH",
        "status": "PENDING"
    }


def test_patch_task_raises_task_not_found(app, valid_task_payload):
    with pytest.raises(TaskNotFoundError):
        task_service.patch_task(1, valid_task_payload)

