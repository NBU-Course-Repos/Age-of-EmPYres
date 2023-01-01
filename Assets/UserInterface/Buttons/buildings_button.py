import pygame
from pygame.math import Vector2
from pygame.sprite import AbstractGroup
from Assets.UserInterface.Buttons.button import Button
from Assets.Controls.controls import Controls
from Assets.Controls.states import ControlStates
from Assets.Buildings.house import House
from Assets.Buildings.mill import Mill
from Assets.Buildings.farm import Farm


class BuildingsButton(Button):
    def __init__(self, pos=Vector2(0, 0), group=AbstractGroup, dimensions=Vector2(40, 40), image="civil_building"):
        self.pos = pos
        super().__init__(pos=self.pos, group=group, image=image)

    def action(self, camera, group):
        hb = HouseButton(group=self.groups(), pos=self.pos)
        mb = MillButton(group=self.groups(), pos=hb.pos+Vector2(45, 0))
        if camera.has_mill:
            FarmButton(group=self.groups(), pos=hb.pos+Vector2(0, 45))
        self.group.remove(self)
        self.kill()


class HouseButton(Button):
    def __init__(self, pos=Vector2(0, 0), group=AbstractGroup, dimensions=Vector2(40, 40), image="house_building"):
        self.pos = pos
        super().__init__(pos=self.pos, group=group, image=image)

    def action(self, camera, group):
        Controls.building = House(camera)
        Controls.building.add(group)
        Controls.state = ControlStates.PLACING


class MillButton(Button):
    def __init__(self, pos=Vector2(0, 0), group=AbstractGroup, dimensions=Vector2(40, 40), image="mill_building"):
        self.pos = pos
        super().__init__(pos=self.pos, group=group, image=image)

    def action(self, camera, group):
        Controls.building = Mill(camera)
        Controls.building.add(group)
        Controls.state = ControlStates.PLACING


class FarmButton(Button):
    def __init__(self, pos=Vector2(0, 0), group=AbstractGroup, dimensions=Vector2(40, 40), image="farm_button"):
        self.pos = pos
        super().__init__(pos=self.pos, group=group, image=image)

    def action(self, camera, group):
        Controls.building = Farm(camera)
        Controls.building.add(group)
        Controls.state = ControlStates.PLACING
