import pygame
from pygame.math import Vector2
from Assets.UserInterface.ui import UI
from Assets.Units.states import UnitState


class Unit(pygame.sprite.Sprite):

    def __init__(self, group, pos=Vector2(0, 0), image="", hp=100, size=Vector2(0, 0), speed=10, name=""):
        super().__init__(group)
        self.health_points = hp
        self.size = size
        self.pos = pos
        self.targetDestination = pos
        self.name = ""
        self.movement_speed = speed
        self.image = pygame.image.load(f"Assets/Textures/Units/{image}.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.isSelected = False
        self.state = UnitState.STATE_IDLE
        self.name = name
        self.task_object = None

    def update_rect(self, pos):
        self.pos = pos

    def select(self, image=""):
        if self.isSelected:
            return
        self.isSelected = True
        self.image = pygame.image.load(f"Assets/Textures/Units/{image}.png")
        self.image = pygame.transform.scale(self.image, self.size)

    def deselect(self):
        if not self.isSelected:
            return
        self.isSelected = False
        self.image = pygame.image.load(f"Assets/Textures/Units/{self.name}.png")
        self.image = pygame.transform.scale(self.image, self.size)

    def set_move(self, pos: Vector2):
        self.targetDestination = pos
        if not self._is_at_target():
            self.state = UnitState.MOVING
        else:
            self.state = UnitState.STATE_IDLE

    def _is_at_target(self):
        return self.pos == self.targetDestination

    def _move(self):
        if not self._is_at_target():
            move_offset_x = move_offset_y = self.movement_speed
            if self.targetDestination.x > self.pos.x:
                if move_offset_x > self.targetDestination.x - self.pos.x:
                    move_offset_x = self.targetDestination.x - self.pos.x
                self.rect.x += move_offset_x
                self.pos.x = self.rect.x
            elif self.targetDestination.x < self.pos.x:
                if move_offset_x > self.pos.x - self.targetDestination.x:
                    move_offset_x = self.pos.x - self.targetDestination.x
                self.rect.x -= move_offset_x
                self.pos.x = self.rect.x

            if self.targetDestination.y > self.pos.y:
                if move_offset_y > self.targetDestination.y - self.pos.y:
                    move_offset_y = self.targetDestination.y - self.pos.y
                self.rect.y += move_offset_y
                self.pos.y = self.rect.y
            elif self.targetDestination.y < self.pos.y:
                if move_offset_y > self.pos.y - self.targetDestination.y:
                    move_offset_y = self.pos.y - self.targetDestination.y
                self.rect.y -= move_offset_y
                self.pos.y = self.rect.y
        else:
            self.state = UnitState.STATE_IDLE

    # def _construct(self):

    def custom_update(self):
        if self.state == UnitState.STATE_IDLE:
            return
        elif self.state == UnitState.MOVING:
            self._move()


