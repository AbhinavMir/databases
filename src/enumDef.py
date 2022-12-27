from enum import Enum

class dataTypes(enum):
    INT = 1
    STRING = 3

class commitStauts(Enum):
    COMMIT = 1
    ABORT = 2
    ACTIVE = 3

class xactAction(Enum):
    UPDATE = 1
    COMMIT = 2
    ABORT = 3
    CLR = 4
    END = 5