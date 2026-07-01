from app.exceptions.task_exceptions import ValidationError, UnsupportedMediaTypeError
from app.models.task_enums import TaskPriority, TaskStatus

TASK_FIELDS = {
    "title",
    "description",
    "priority",
    "status"
}

CREATE_REQUIRED_FIELDS = {
    "title"
}

UPDATE_REQUIRED_FIELDS = {
    "title",
    "description",
    "priority",
    "status"
}

def validate_content_type(request):
    if not request.is_json:
        raise UnsupportedMediaTypeError("Unsupported Media Type")


def validate_body(data):
    if data is None:
        raise ValidationError("Request body must be provided")
    
    if not data:
        raise ValidationError("Request body cannot be empty")


def validate_allowed_fields(data, allowed_fields):
    received_fields = set(data.keys())
    unknown_fields = received_fields - allowed_fields

    if unknown_fields:
        unknown_fields_message = ", ".join(sorted(unknown_fields))
        raise ValidationError(f"Unknown fields: {unknown_fields_message}")
                                        

def validate_required_fields(data, required_fields):
    received_fields = set(data.keys())
    missing_fields = required_fields - received_fields

    if missing_fields:
        missing_fields_message = ", ".join(sorted(missing_fields))
        raise ValidationError(f"Missing fields: {missing_fields_message}")
    

def validate_title(title):
    if title is None:
        raise ValidationError("Title is required")
    
    if not isinstance(title, str):
        raise ValidationError("Title must be a string") 
    
    if title.strip() == "":
        raise ValidationError("Title cannot be empty")
    
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
    validate_allowed_fields(data, TASK_FIELDS)
    validate_required_fields(data,CREATE_REQUIRED_FIELDS)

    validate_title(data.get("title"))
    validate_description(data.get("description"))
    validate_priority(data.get("priority"))
    validate_status(data.get("status"))


def validate_update_task(data):
    validate_body(data)
    validate_allowed_fields(data, TASK_FIELDS)
    validate_required_fields(data, UPDATE_REQUIRED_FIELDS)

    validate_title(data.get("title"))
    validate_description(data.get("description"))
    validate_priority(data.get("priority"))
    validate_status(data.get("status"))


def validate_patch_task(data):
    validate_body(data)
    validate_allowed_fields(data, TASK_FIELDS)

    if not any(field in data for field in TASK_FIELDS):
        raise ValidationError("At least one valid field must be provided") 

    if "title" in data:
        validate_title(data.get("title"))
    
    if "description" in data:
        validate_description(data.get("description"))

    if "priority" in data:
        validate_priority(data.get("priority"))
    
    if "status" in data:
        validate_status(data.get("status"))
