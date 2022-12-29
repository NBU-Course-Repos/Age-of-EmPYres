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
        self.task_object = None

    #  If working on a self.task_object, stop
    def stop_working(self):
        if self.task_object != None and self in self.task_object.get_workers():
            self.task_object.remove_worker(self)

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

    def set_move(self, pos: Vector2):
        self.targetDestination = pos
        self.stop_working()
        if not self._is_at_target():
            self.state = UnitState.MOVING
        else:
            self.state = UnitState.STATE_IDLE

    def set_construct(self, building):
        self.state = UnitState.CONSTRUCTING
        self.stop_working()
        self.task_object = building

    def _construct(self):
        if self.task_object.building_state != BuildingState.BUILT:
            self.targetDestination = self.task_object.get_position()
            if not self._is_at_target():
                self._move()
                self.task_object.add_worker(self)
        else:
            self.task_object.remove_worker(self)
            self.state == UnitState.STATE_IDLE

    def custom_update(self):
        if self.state == UnitState.STATE_IDLE:
            return
        elif self.state == UnitState.MOVING:
            self._move()
        elif self.state == UnitState.CONSTRUCTING:
            self._construct()
