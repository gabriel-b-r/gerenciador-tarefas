import pytest
from app.validators.task_validator import validate_content_type
from app.exceptions.task_exceptions import UnsupportedMediaTypeError
from unittest.mock import Mock

def test_validate_content_type_accepts_json():
    request = Mock()
    request.is_json = True
    
    validate_content_type(request)


def test_validate_content_type_raises_when_media_type_is_unsupported():
    request = Mock()
    request.is_json = False

    with pytest.raises(UnsupportedMediaTypeError):
        validate_content_type(request)
