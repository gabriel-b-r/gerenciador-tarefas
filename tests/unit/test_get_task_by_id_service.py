import pytest
from app.services import task_service
from app.exceptions.task_exceptions import TaskNotFoundError


def test_get_task_by_id_returns_task_dict(app, created_task):
    created_task

    response = task_service.get_task_by_id(1)

    assert response == {
        "id": 1,
        "title": "Task",
        "description": "Testing",
        "priority": "LOW",
        "status": "PENDING"
    }


def test_get_task_by_id_raises_task_not_found(app):
    with pytest.raises(TaskNotFoundError):
        task_service.get_task_by_id(1)
