from enum import Enum


class UnitState(Enum):
    STATE_IDLE = 1
    MOVING = 2
    CONSTRUCTING = 3
    GATHERING = 4  # Gathering resources
    OFFLOADING = 5
