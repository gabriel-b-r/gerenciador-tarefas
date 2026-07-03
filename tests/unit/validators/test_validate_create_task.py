import pytest
from app.validators.task_validator import validate_create_task
from app.exceptions.task_exceptions import ValidationError

def test_validate_create_task_accepts_valid_payload(valid_task_payload):
    validate_create_task(valid_task_payload)


def test_validate_create_task_raises_when_payload_is_empty():
    PAYLOAD = {}

    with pytest.raises(ValidationError):
        validate_create_task(PAYLOAD)


def test_validate_create_task_raises_when_title_is_missing():
    PAYLOAD = {
        "description": "Testing",
        "priority": "LOW",
        "status": "PENDING"
    }

    with pytest.raises(ValidationError):
        validate_create_task(PAYLOAD)


def test_validate_create_task_raises_when_unknown_field_is_provided():
    PAYLOAD = {
        "title": "Task",
        "description": "Testing",
        "priority": "LOW",
        "status": "PENDING",
        "Test": "Test"
    }

    with pytest.raises(ValidationError):
        validate_create_task(PAYLOAD)
