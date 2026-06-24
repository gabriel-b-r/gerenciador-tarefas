class AppException(Exception):
    status_code = 500

    def __init__(self, message):
        self.message = message

        super().__init__(message)
        