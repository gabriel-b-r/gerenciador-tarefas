import pytest
from app.services import task_service
from app.exceptions.task_exceptions import ValidationError

def test_create_task_with_all_fields_returns_task_dict(app, valid_task_payload):
    response = task_service.create_task(valid_task_payload)

    assert response == {
        "id": 1,
        "title": "Task",
        "description": "Testing",
        "priority": "LOW",
        "status": "PENDING"
        }


def test_create_task_with_default_values_returns_task_dict(app):
    payload = {
        "title": "Task"
    }

    response = task_service.create_task(payload)

    assert response == {
        "id": 1,
        "title": "Task",
        "description": None,
        "priority": "LOW",
        "status": "PENDING"
    }


