import pytest
from app.validators.task_validator import validate_status
from app.exceptions.task_exceptions import ValidationError

def test_validate_status_accepts_pending():
    validate_status("PENDING")


def test_validate_status_accepts_in_progress():
    validate_status("IN PROGRESS")


def test_validate_status_accepts_completed():
    validate_status("COMPLETED")


def test_validate_status_accepts_none():
    validate_status(None)


def test_validate_status_raises_for_invalid_status():
    with pytest.raises(ValidationError):
        validate_status("Test")
