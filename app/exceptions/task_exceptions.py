from app.exceptions.base import AppException

class ValidationError(AppException):
    status_code = 400

class TaskNotFoundError(AppException):
    status_code = 404