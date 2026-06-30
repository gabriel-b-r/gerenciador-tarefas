from app.extensions.database import db
from app.models.task_enums import TaskPriority, TaskStatus

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(
        db.String(255)
    )

    priority = db.Column(
        db.String(50),
        default=TaskPriority.LOW.value
    )

    status = db.Column(
        db.String(50),
        default=TaskStatus.PENDING.value
    )


    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority
        }
