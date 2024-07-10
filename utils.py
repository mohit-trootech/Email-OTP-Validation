"""Custom Utility Classes"""
from datetime import datetime, timedelta


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


def time_difference(time_obj: datetime) -> timedelta:
    """
    function to return the total seconds between two time object
    @param time_obj: datetime
    @return: timedelta
    """
    return (datetime.now().replace(microsecond=0) - time_obj).total_seconds()
