from enum import Enum


class BuildingState(Enum):
    CONSTRUCTING = 1
    BUILT = 2
    PAUSE_CONSTRUCTION = 3
    PLACING = 4
