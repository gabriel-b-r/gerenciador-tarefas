from app.exceptions.task_exceptions import ValidationError

def validate_body(data):
    if not data:
        raise ValidationError("Request body cannot be empty")
    
    #validar content-type


def validate_title(title):
    if not title or title is None:
        raise ValidationError("Title is required")
    
    if type(title) is not str:
        raise ValidationError("Title must be a string") 
    
    if title.strip() == "":
        raise ValidationError("Title must have characters")
    
    if len(title) > 255:
        raise ValidationError("Title length must be less than 255 characters")

def validate_description(description):
    # Deve ser string
    if type(description) is not str:
        raise ValidationError("Description must be a string")

    # Tamanho limite


def validate_priority(priority):
    pass

    # Deve aceitar apenas LOW, MEDIUM, HIGH


def validate_status(status):
    pass
    # Deve aceitar apenas PENDING, IN PROGRESS, COMPLETED


def validate_create_task(data):
    validate_body(data)
    validate_title(data.get("title"))
    validate_description(data.get("description"))
