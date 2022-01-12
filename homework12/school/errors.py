class DeadlineError(Exception):
    """
    Error for homework tasks
    which have been expired.
    """
    pass


class AlreadyAcceptedError(Exception):
    """
    Error for already checked homework tasks
    to avoid unwanted changes in do_homework dict."""
    pass


class InstanceError(Exception):
    """My error for wrong input type."""
    pass


class DoesNotExistError(Exception):
    """If something does not exist in database."""
    pass
