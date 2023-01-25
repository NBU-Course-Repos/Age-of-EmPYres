from Assets.Buildings.building import Building
from pygame.math import Vector2


class House(Building):
    def __init__(self, group, pos=Vector2(0, 0)):
        super().__init__(group, texture="house", ct=5, pos=pos)  # remove ct 5 after fixing building creation
        self._set_image("house")
        print("Initializing new House")