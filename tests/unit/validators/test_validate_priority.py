import pytest
from app.validators.task_validator import validate_priority
from app.exceptions.task_exceptions import ValidationError

def test_validate_priority_accepts_low():
    validate_priority("LOW")


def test_validate_priority_accepts_medium():
    validate_priority("MEDIUM")


def test_validate_priority_accepts_high():
    validate_priority("HIGH")


def test_validate_priority_accepts_none():
    validate_priority(None)


def test_validate_priority_raises_for_invalid_priority():
    with pytest.raises(ValidationError):
        validate_priority("Test")