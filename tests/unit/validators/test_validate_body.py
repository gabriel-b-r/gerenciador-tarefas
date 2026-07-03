import pytest
from app.validators.task_validator import validate_body
from app.exceptions.task_exceptions import ValidationError

def test_validate_body_accepts_valid_data(valid_task_payload):
    validate_body(valid_task_payload)


def test_validate_body_raises_when_body_is_none():
    with pytest.raises(ValidationError):
        validate_body(None)


def test_validate_body_raises_when_body_is_empty():
    payload = {}

    with pytest.raises(ValidationError):
        validate_body(payload)
