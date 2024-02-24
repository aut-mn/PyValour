__all__ = (
    'ValourError',
    'InvalidAuthorization'
)


class ValourError(Exception):
    """A base error class for all exceptions raised by PyValour."""
    pass


class InvalidAuthorization(ValourError):
    """Raised when access to the authorized resource was denied."""
    pass
