import pytest
from app.validators.task_validator import validate_description
from app.exceptions.task_exceptions import ValidationError

def test_validate_description_accepts_valid_description():
    validate_description("Testing")


def test_validate_description_accepts_none():
    validate_description(None)


def test_validate_description_raises_when_description_is_not_string():
    with pytest.raises(ValidationError):
        validate_description(123)


def test_validate_description_raises_when_description_exceeds_max_length():
    TITLE = "Lorem ipsum dolor sit amet consectetur adipiscing elit quisque faucibus ex sapien vitae pellentesque sem placerat in id cursus mi pretium tellus duis convallis tempus leo eu aenean sed diam urna tempor pulvinar vivamus fringilla lacus nec metus bibendum eg"

    with pytest.raises(ValidationError):
        validate_description(TITLE)
