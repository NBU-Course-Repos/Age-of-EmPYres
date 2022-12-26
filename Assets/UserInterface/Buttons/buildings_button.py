import pygame
from pygame.math import Vector2
from pygame.sprite import AbstractGroup
from Assets.UserInterface.Buttons.button import Button
from Assets.Buildings.house import House
from Assets.Controls.controls import Controls
from Assets.Controls.states import ControlStates


class BuildingsButton(Button):
    def __init__(self, pos=Vector2(0, 0), group=AbstractGroup, dimensions=Vector2(40, 40), image="civil_building"):
        self.pos = pos
        super().__init__(pos=self.pos, group=group, image=image)

    def action(self, camera, group):
        HouseButton(group=self.groups(), pos=self.pos)
        self.group.remove(self)
        self.kill()


class HouseButton(Button):
    def __init__(self, pos=Vector2(0, 0), group=AbstractGroup, dimensions=Vector2(40, 40), image="house_building"):
        self.pos = pos
        super().__init__(pos=self.pos, group=group, image=image)

    def action(self, camera, group):
        Controls.building = House(camera)
        Controls.building.add(group)
        Controls.state = ControlStates.BUILDING


