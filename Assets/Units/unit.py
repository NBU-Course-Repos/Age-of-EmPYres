import os

import pygame
from pygame.math import Vector2
from Assets.Units.states import UnitState
from Assets.UserInterface.text import Text
from Assets.SaveSystem.savable_object import SavableObject


class Unit(pygame.sprite.Sprite):

    def __init__(self, group, player, pos=Vector2(0, 0),  image="", hp=100, size=Vector2(0, 0), speed=10, damage=0, name="", team=1):
        super().__init__()
        self.health_points = hp
        self.total_health = hp
        self.size = size
        self.pos = pos
        self.target_destination = pos
        self.name = ""
        self.movement_speed = speed
        self.image = pygame.image.load(f"{os.getcwd()}/Assets/Textures/Units/{image}.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.is_selected = False
        self.state = UnitState.STATE_IDLE
        self.name = name
        self.task_object = None
        self.damage = damage
        self.camera = group
        self.ui = []
        self.border = None
        self.team = team
        group.add(self)

    def update_rect(self, pos):
        self.pos = pos

    def _generate_ui(self):
        bottom_bar = self.camera.ui_group.bottom_bar
        return [Text(text=f"{self.name}", pos=Vector2(bottom_bar.rect.topleft) + (0, 10)),
                Text(text=f"Damage {self.damage}", pos=Vector2(bottom_bar.rect.topleft) + (0, 30)),
                Text(text=f"HP: {self.health_points}/{self.total_health}", pos=Vector2(bottom_bar.rect.topleft) + (0, 50))]

    def _hide_ui(self):
        self.camera.ui_group.remove(self.ui)

    def _display_ui(self):
        self._hide_ui()
        self.ui = self._generate_ui()
        self.camera.add(self.ui)

    def select(self):
        if self.is_selected:
            return
        self.is_selected = True
        self.draw_border()
        self.camera.ui_group.render_villager_buttons()

    def deselect(self):
        if not self.is_selected:
            return
        self.is_selected = False
        self.image = pygame.image.load(f"{os.getcwd()}/Assets/Textures/Units/{self.name}.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.camera.ui_group.clear_buttons()
        self._hide_ui()

    def draw_border(self):
        self.border = pygame.draw.rect(surface=self.image,
                                       color=(255, 255, 255),
                                       rect=[0, 0, self.image.get_width(), self.image.get_height()],
                                       width=1)

    def delete_border(self):
        self.image = pygame.image.load(f"{os.getcwd()}/Assets/Textures/{self.tile_type}.png")

    def set_move(self, pos: Vector2):
        self.target_destination = pos
        if not self._is_at_target():
            self.state = UnitState.MOVING
        else:
            self.state = UnitState.STATE_IDLE

    def _is_at_target(self):
        return self.pos == self.target_destination

    def _move(self):
        if not self._is_at_target():
            move_offset_x = move_offset_y = self.movement_speed
            if self.target_destination.x > self.pos.x:
                if move_offset_x > self.target_destination.x - self.pos.x:
                    move_offset_x = self.target_destination.x - self.pos.x
                self.rect.x += move_offset_x
                self.pos.x = self.rect.x
            elif self.target_destination.x < self.pos.x:
                if move_offset_x > self.pos.x - self.target_destination.x:
                    move_offset_x = self.pos.x - self.target_destination.x
                self.rect.x -= move_offset_x
                self.pos.x = self.rect.x

            if self.target_destination.y > self.pos.y:
                if move_offset_y > self.target_destination.y - self.pos.y:
                    move_offset_y = self.target_destination.y - self.pos.y
                self.rect.y += move_offset_y
                self.pos.y = self.rect.y
            elif self.target_destination.y < self.pos.y:
                if move_offset_y > self.pos.y - self.target_destination.y:
                    move_offset_y = self.pos.y - self.target_destination.y
                self.rect.y -= move_offset_y
                self.pos.y = self.rect.y
        else:
            self.state = UnitState.STATE_IDLE

    def custom_update(self):
        if self.is_selected:
            self._display_ui()
        if self.state == UnitState.STATE_IDLE:
            return
        elif self.state == UnitState.MOVING:
            self._move()


