import pygame
from pygame.math import Vector2
from Assets.Units.unit import Unit
from Assets.Units.states import UnitState


class Villager(Unit):
    def __init__(self, group, pos=Vector2(0, 0), image="villager", hp=100, size=Vector2(30, 30)):
        super().__init__(group, pos, image, hp, size)
        self.name = "villager"

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

    def _build(self):
        return
        # TO DO

    def custom_update(self):
        if self.state == UnitState.STATE_IDLE:
            return
        elif self.state == UnitState.MOVING:
            self._move()
