import pytest
from app.services import task_service
from app.exceptions.task_exceptions import TaskNotFoundError

def test_get_task_or_404_returns_task(app, created_task):
    created_task
    
    task_service.get_task_or_404(1)


def test_get_task_or_404_raises_task_not_found(app):
    with pytest.raises(TaskNotFoundError):
        task_service.get_task_or_404(1)