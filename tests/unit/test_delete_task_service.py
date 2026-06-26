import pytest
from app.services import task_service
from app.exceptions.task_exceptions import TaskNotFoundError

def test_delete_task_success(app, created_task):
    with app.app_context():
        created_task

        task_service.delete_task(1)

        
def test_delete_task_raises_task_not_found(app):
    with app.app_context():
        with pytest.raises(TaskNotFoundError):
            task_service.delete_task(1)