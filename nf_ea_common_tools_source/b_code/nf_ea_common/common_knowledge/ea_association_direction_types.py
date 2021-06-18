from enum import Enum
from enum import auto
from enum import unique


@unique
class EaAssociationDirectionTypes(
    Enum):
    NOT_SET = auto()
    FORWARD = auto()
    BACKWARD = auto()
