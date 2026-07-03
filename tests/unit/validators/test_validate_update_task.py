import pytest
from app.validators.task_validator import validate_update_task
from app.exceptions.task_exceptions import ValidationError

def test_validate_update_task_accepts_valid_payload(valid_task_payload):
    validate_update_task(valid_task_payload)


def test_validate_update_task_raises_when_required_field_is_missing():
    PAYLOAD = {
        "description": "Testing",
        "priority": "LOW",
        "status": "PENDING"
    }

    with pytest.raises(ValidationError):
        validate_update_task(PAYLOAD)


def test_validate_update_task_raises_when_unknown_field_is_provided():
    PAYLOAD = {
        "title": "Task",
        "description": "Testing",
        "priority": "LOW",
        "status": "PENDING",
        "test": "Test"
    }

    with pytest.raises(ValidationError):
        validate_update_task(PAYLOAD)
