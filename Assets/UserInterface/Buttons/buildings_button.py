import pygame
from pygame.math import Vector2
from Assets.UserInterface.Buttons.button import Button
from pygame.sprite import AbstractGroup


class BuildingsButton(Button):
    def __init__(self, group=AbstractGroup, dimensions=Vector2(40, 40),image="civil_building"):
        self.pos = group.bottom_left_bar.pos + Vector2(20,20)
        super().__init__(pos=self.pos, group=group, image=image)




