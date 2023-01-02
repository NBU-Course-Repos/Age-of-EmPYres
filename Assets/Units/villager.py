import pygame
from pygame.math import Vector2
from Assets.Units.unit import Unit
from Assets.Units.states import UnitState
from Assets.Buildings.states import BuildingState
from Assets.Resources.types import ResourceType
from Assets.Resources.states import ResourceStatus


class Villager(Unit):

    def __init__(self, group, pos=Vector2(0, 0), image="villager", hp=100, size=Vector2(30, 30)):
        super().__init__(group, pos, image, hp, size, damage=3, speed=5)
        self.name = "villager"
        self.gather_rate = 1  # What amount of resources can be gather per second.
        # Might re-do it as a dictionary for the different types of resources
        self.resource_capacity: dict = {
            ResourceType.STONE: 10,
            ResourceType.WOOD: 10,
            ResourceType.BRONZE: 10,
            ResourceType.IRON: 10,
            ResourceType.FOOD: 10,
            ResourceType.GOLD: 10
        }
        self.resource_carrying: dict = {
            ResourceType.STONE: 0,
            ResourceType.WOOD: 0,
            ResourceType.BRONZE: 0,
            ResourceType.IRON: 0,
            ResourceType.FOOD: 0,
            ResourceType.GOLD: 0
        }

    def _offload_resources(self):
        self.targetDestination = Vector2(500, 0)
        if not self._is_at_target():
            self._move()
        else:
            for resource in self.resource_carrying:
            #    print(self.resource_carrying[resource])  # TO BE SWITCHED WITH ADDITION TO THE PLAYER's resources
                self.resource_carrying[resource] = 0
            self.set_gather(self.task_object)

    #  If working on a self.task_object, stop
    def stop_working(self):
        if self.task_object is not None and self in self.task_object.get_workers():
            self.task_object.remove_worker(self)

    def select(self, ui_group, image="villager_selected"):
        if self.isSelected:
            return
        self.isSelected = True
        self.image = pygame.image.load(f"Assets/Textures/Units/{image}.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.pos)
        ui_group.render_villager_buttons()

    def deselect(self):
        if not self.isSelected:
            return
        self.isSelected = False
        self.image = pygame.image.load(f"Assets/Textures/Units/{self.name}.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.camera.ui_group.clear_buttons()

    def set_offload(self):
        self.state = UnitState.OFFLOADING
        self.stop_working()

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

    def set_gather(self, resource):
        self.state = UnitState.GATHERING
        self.stop_working()
        self.task_object = resource

    def _construct(self):
        if self.task_object.state != BuildingState.BUILT:
            self.targetDestination = self.task_object.get_position()
            if not self._is_at_target():
                self._move()
                self.task_object.add_worker(self)
        else:
            self.task_object.remove_worker(self)
            self.state == UnitState.STATE_IDLE

    def _gather(self):
        if self.task_object.state != ResourceStatus.DESTROYED:
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
        elif self.state == UnitState.GATHERING:
            self._gather()
        elif self.state == UnitState.OFFLOADING:
            self._offload_resources()
