from enum import Enum


class JobStatus(Enum):
    APPLIED = 1
    NOT_APPLIED = 2
    NOT_QUALIFIED = 3
    AUTOMATION_NOT_SUPPORTED = 4
    AUTOMATION_NOT_SUPPORTED_OUTSIDE_INDEED = 5
    APPLICATION_ERROR = 6


    def __str__(self):
        return self.name
