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

