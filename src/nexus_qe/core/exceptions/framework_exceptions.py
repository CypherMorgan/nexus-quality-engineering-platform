class FrameworkException(Exception):
    """Base framework exception."""


class ConfigurationError(FrameworkException):
    """Configuration-related exception."""


class ApiValidationError(FrameworkException):
    """API validation failure."""


class DatabaseValidationError(FrameworkException):
    """Database validation failure."""


class RetryExceededError(FrameworkException):
    """Raised when retry limit is exceeded."""