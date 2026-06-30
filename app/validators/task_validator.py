from app.exceptions.task_exceptions import ValidationError
from app.models.task_enums import TaskPriority, TaskStatus

def validate_body(data):
    if data is None:
        raise ValidationError("Request body must be provided")
    
    if not data:
        raise ValidationError("Request body cannot be empty")


def validate_title(title):
    if not title or title is None:
        raise ValidationError("Title is required")
    
    if not isinstance(title, str):
        raise ValidationError("Title must be a string") 
    
    if title.strip() == "":
        raise ValidationError("Title must have characters")
    
    if len(title) > 255:
        raise ValidationError("Title length must be less than 255 characters")


def validate_description(description):
    if description is None:
        return

    if not isinstance(description, str):
        raise ValidationError("Description must be a string")

    if len(description) > 255:
        raise ValidationError("Description length must be less than 255 characters")


def validate_priority(priority):
    if priority is None:
        return

    try:
        TaskPriority(priority)
    except ValueError:
        raise ValidationError("Priority must be LOW, MEDIUM or HIGH")


def validate_status(status):
    if status is None:
        return

    try:
        TaskStatus(status)
    except ValueError:
        raise ValidationError("Status must be PENDING, IN PROGRESS or COMPLETED")


def validate_create_task(data):
    validate_body(data)
    validate_title(data.get("title"))
    validate_description(data.get("description"))
    validate_priority(data.get("priority"))
    validate_status(data.get("status"))


def validate_update_task(data):
    validate_body(data)

    required_fields = [
    "title",
    "description",
    "priority",
    "status"
    ]

    for field in required_fields:
        if not data.get(field):
            raise ValidationError(f"{field.capitalize()} is required")

    validate_title(data.get("title"))
    validate_description(data.get("description"))
    validate_priority(data.get("priority"))
    validate_status(data.get("status"))


def validate_patch_task(data):
    validate_body(data)

    allowed_fields = [
    "title",
    "description",
    "priority",
    "status"
    ]

    if not any(field in data for field in allowed_fields):
        raise ValidationError("At least one valid field must be provided") 

    if "title" in data:
        validate_title(data.get("title"))
    
    if "description" in data:
        validate_description(data.get("description"))

    if "priority" in data:
        validate_priority(data.get("priority"))
    
    if "status" in data:
        validate_status(data.get("status"))
