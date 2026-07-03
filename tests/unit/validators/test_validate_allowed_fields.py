import pytest
from app.validators.task_validator import validate_allowed_fields
from app.exceptions.task_exceptions import ValidationError

ALLOWED_FIELDS = {
    "title",
    "description",
    "priority",
    "status"
}

def test_validate_allowed_fields_accepts_all_valid_fields(valid_task_payload):
    validate_allowed_fields(valid_task_payload, ALLOWED_FIELDS)


def test_validate_allowed_fields_raises_when_one_field_is_unknown():
    payload = {
        "title": "Task",
        "description": "Testing",
        "priority": "LOW",
        "status": "PENDING",
        "test": "Test"
    }

    with pytest.raises(ValidationError):
        validate_allowed_fields(payload, ALLOWED_FIELDS)


def test_validate_allowd_fields_raises_when_multiple_fields_is_unknown():
    payload = {
        "title": "Task",
        "test_1": "Test 1",
        "test_2": "Test 2",
        "test_3": "Test 3"
    }

    with pytest.raises(ValidationError):
        validate_allowed_fields(payload, ALLOWED_FIELDS)
