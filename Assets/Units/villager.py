import pygame
from pygame.math import Vector2
from Assets.Units.unit import Unit
from Assets.Units.states import UnitState
from Assets.Buildings.building import Building
from Assets.Buildings.states import BuildingState


class Villager(Unit):

    def __init__(self, group, pos=Vector2(0, 0), image="villager", hp=100, size=Vector2(30, 30)):
        super().__init__(group, pos, image, hp, size)
        self.name = "villager"
        self.taskObj = None

    def select(self, ui_group, image="villager_selected"):
        if self.isSelected:
            return
        self.isSelected = True
        self.image = pygame.image.load(f"Assets/Textures/Units/{image}.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.pos)
        ui_group.render_villager_buttons()

    def deselect(self, ui_group):
        if not self.isSelected:
            return
        self.isSelected = False
        self.image = pygame.image.load(f"Assets/Textures/Units/{self.name}.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.pos)
        ui_group.clear_buttons()

    def set_construct(self, building):
        self.state = UnitState.CONSTRUCTING
        self.taskObj = building

    def _construct(self):
        if self.taskObj.building_state != BuildingState.BUILT:
            self.targetDestination = self.taskObj.get_position()
            if not self._is_at_target():
                self._move()
                self.taskObj.add_worker(self)
        else:
            self.taskObj.remove_worker(self)
            self.state == UnitState.STATE_IDLE

    def custom_update(self):
        if self.state == UnitState.STATE_IDLE:
            return
        elif self.state == UnitState.MOVING:
            self._move()
        elif self.state == UnitState.CONSTRUCTING:
            self._construct()
