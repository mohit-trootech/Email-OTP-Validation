"""Custom Utility Classes"""


class EmailInvalid(Exception):
    """
    Custom Exception to Throw Email Validation Error
    """

    def __init__(self, msg: str) -> None:
        """
        custom error class to throw Email Invalidation Error
        @param msg: str
        """
        self.msg = msg
