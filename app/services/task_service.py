from app.extensions.database import db
from app.models.task import Task
from app.models.task_enums import TaskPriority, TaskStatus
from app.exceptions.task_exceptions import ValidationError, TaskNotFoundError
from app.validators import task_validator

def create_task(data):
    task_validator.validate_create_task(data)

    task = Task(
        title = data["title"],
        description = data.get("description"),
        priority = data.get("priority", TaskPriority.LOW.value),
        status = data.get("status", TaskStatus.PENDING.value)
    )

    db.session.add(task)
    db.session.commit()

    return task.to_dict()


def get_tasks():
    tasks = Task.query.all()

    return [
        task.to_dict()
        for task in tasks
    ]


def get_task_by_id(task_id):
    
    task = get_task_or_404(task_id)

    return task.to_dict()


def delete_task(task_id):

    task = get_task_or_404(task_id)

    db.session.delete(task)
    db.session.commit()


def update_task(task_id, data):
    
    task = get_task_or_404(task_id)

    required_fields = [
    "title",
    "description",
    "priority",
    "status"
    ]

    for field in required_fields:
        if not data.get(field):
            raise ValidationError(f"{field.capitalize()} is required")


    task.title = data["title"]
    task.description = data["description"]
    task.priority = data["priority"]
    task.status = data["status"]

    db.session.commit()

    return task.to_dict()


def patch_task(task_id, data):

    task = get_task_or_404(task_id)

    allowed_fields = [
    "title",
    "description",
    "priority",
    "status"
    ]

    if not data:
        raise ValidationError("Request body cannot be empty")

    if not any(field in data for field in allowed_fields):
        raise ValidationError("At least one valid field must be provided") 

    if "title" in data:
        task.title = data["title"]

    if "description" in data:
        task.description = data["description"]

    if "priority" in data:
        task.priority = data["priority"]
    
    if "status" in data:
        task.status = data["status"]

    db.session.commit()

    return task.to_dict()


def get_task_or_404(task_id):
    task = db.session.get(Task, task_id)

    if task is None:

        raise TaskNotFoundError("Task not found")
    
    return task

