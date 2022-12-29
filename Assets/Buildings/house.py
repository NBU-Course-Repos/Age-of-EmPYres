from Assets.Buildings.building import Building
import pygame


class House(Building):
    def __init__(self, group):
        super().__init__(group, texture="house", ct=5)  # remove ct 5 after fixing building creation
        self._set_image("house")
        print("Initializing new House")
        print(self._remaining_build_time)