import pytest
from app.validators.task_validator import validate_patch_task
from app.exceptions.task_exceptions import ValidationError

def test_validate_patch_task_accepts_one_valid_field():
    PAYLOAD = {
        "title": "Task"
    }

    validate_patch_task(PAYLOAD)


def test_validate_patch_task_accepts_multiple_valid_fields():
    PAYLOAD = {
        "title": "Task",
        "description": "Testing"
    }

    validate_patch_task(PAYLOAD)


def test_validate_patch_task_raises_when_empty_body_is_provided():
    PAYLOAD = {}

    with pytest.raises(ValidationError):
        validate_patch_task(PAYLOAD)


def test_validate_patch_task_raises_when_unknown_field_is_provided():
    PAYLOAD = {
        "title": "Task",
        "description": "Testing",
        "test": "Test"
    }

    with pytest.raises(ValidationError):
        validate_patch_task(PAYLOAD)