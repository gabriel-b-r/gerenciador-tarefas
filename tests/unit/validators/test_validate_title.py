import pytest
from app.validators.task_validator import validate_title
from app.exceptions.task_exceptions import ValidationError

def test_validate_title_accepts_valid_title():
    validate_title("Task")


def test_validate_title_raises_when_title_is_none():
    with pytest.raises(ValidationError):
        validate_title(None)


def test_validate_title_raises_when_title_is_not_string():
    with pytest.raises(ValidationError):
        validate_title(123)


def test_validate_title_raises_when_title_is_list():
    with pytest.raises(ValidationError):
        validate_title(["Test_1", "Test_2"])


def test_validate_title_raises_when_title_is_empty():
    with pytest.raises(ValidationError):
        validate_title("")


def test_validate_title_raises_when_title_contains_only_spaces():
    with pytest.raises(ValidationError):
        validate_title("       ")


def test_validate_title_raises_when_title_exceeds_max_length():
    TITLE = "Lorem ipsum dolor sit amet consectetur adipiscing elit quisque faucibus ex sapien vitae pellentesque sem placerat in id cursus mi pretium tellus duis convallis tempus leo eu aenean sed diam urna tempor pulvinar vivamus fringilla lacus nec metus bibendum eg"

    with pytest.raises(ValidationError):
        validate_title(TITLE)
    