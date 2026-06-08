from app.extensions.database import db
from app.models.task import Task

def create_task(data):

    if not data.get("title"):
        raise ValueError("Title is required")

    task = Task(
        title = data["title"],
        description = data.get("description"),
        priority = data.get("priority", "LOW"),
        status = data.get("status", "PENDING")
    )

    db.session.add(task)
    db.session.commit()

    return task


def get_tasks():

    try:

        tasks = Task.query.all()

        return [
            task.to_dict()
            for task in tasks
        ]

    except Exception as error:

        raise error


def get_task_by_id(task_id):

    task = db.session.get(Task, task_id)
    
    if task is None:

        raise Exception("Task not found")

    return task.to_dict()


def delete_task(task_id):

    task = db.session.get(Task, task_id)

    if task is None:

        raise Exception("Task not found")
    
    db.session.delete(task)
    db.session.commit()


def update_task(task_id, data):
    
    task = db.session.get(Task, task_id)

    if task is None:

        raise Exception("Task not found")
    
    task.title = data["title"]
    task.description = data["description"]
    task.priority = data["priority"]
    task.status = data["status"]

    db.session.commit()

    return task.to_dict()


def patch_task(task_id, data):

    task = db.session.get(Task, task_id)

    if task is None:

        raise Exception("Task not found")

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