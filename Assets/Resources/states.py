from enum import Enum


class ResourceState(Enum):
    UNTOUCHED = 1   # No Villager is gathering this resource
    DESTROYED = 2  # A villager has gathered the entire content of the resource
    GATHERED = 3  # A village is gathering it

