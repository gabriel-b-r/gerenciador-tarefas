import pytest
from app.validators.task_validator import validate_required_fields
from app.exceptions.task_exceptions import ValidationError

REQUIRED_FIELDS = {
    "title",
    "description",
    "priority",
    "status"
}

def test_validate_required_fields_accepts_all_required_fields(valid_task_payload):
    validate_required_fields(valid_task_payload, REQUIRED_FIELDS)
    

def test_validate_required_fields_raises_when_one_field_is_missing():
    payload = {
        "title": "Task",
        "description": "Testing",
        "priority": "LOW"
    }

    with pytest.raises(ValidationError):
        validate_required_fields(payload, REQUIRED_FIELDS)


def test_validate_required_fields_raises_when_multiple_fields_is_missing():
    payload = {
        "title": "Task"
    }

    with pytest.raises(ValidationError):
        validate_required_fields(payload, REQUIRED_FIELDS)
