import pytest
from app.services import task_service
from app.exceptions.task_exceptions import TaskNotFoundError
from app.extensions.database import db
from app.models.task import Task

def test_get_task_or_404_returns_task(app):
        with app.app_context():
            task = Task(
                title="Task 1",
                description="Testing task 1",
                priority="HIGH",
                status="PENDING"
            )

            db.session.add(task)
            db.session.commit()
        
        task_service.get_task_or_404(1)




def test_get_task_or_404_returns_404(app):
    with app.app_context():

        with pytest.raises(TaskNotFoundError):
            task_service.get_task_or_404(1)