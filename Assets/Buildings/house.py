from Assets.Buildings.building import Building
import pygame


class House(Building):
    def __init__(self, group):
        super().__init__(group, texture="house")
        self._set_image("house")