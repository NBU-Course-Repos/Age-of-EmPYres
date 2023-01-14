import pygame
from pygame.math import Vector2

from Assets.Buildings.states import BuildingState
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.Units.unit import Unit
from Assets.UserInterface.ui_group import UIGroup
from Assets.Buildings.building import Building


class CameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__(self)
        self.offset = pygame.math.Vector2(0, 0)
        self.offsetX = self.offsetY = 0
        self.ui_group = UIGroup()
        self.unit_group = pygame.sprite.Group()
        self.buildings_group = pygame.sprite.Group()
        self.resources = pygame.sprite.Group()
        self.has_mill = False
        self.groups = [self.unit_group, self.buildings_group, self.resources]  # To be used in custom draw

        # TO DO: Set Offset Limit based on map size
    def __update_offset(self):
        # By How much should the screen move
        offset_pixels = 15
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        # Left side of screen
        if mouse_x <= 3:
            self.offsetX += offset_pixels
        # Right side of screen
        elif mouse_x >= SCREEN_WIDTH - 3:
            self.offsetX -= offset_pixels
        # Top of the screen
        if mouse_y <= 3:
            self.offsetY += offset_pixels
        # Bottom of the screen
        elif mouse_y >= SCREEN_HEIGHT - 3:
            self.offsetY -= offset_pixels
        self.offset.update(self.offsetX, self.offsetY)

    def custom_draw(self):
        # To Do: Don't update unit sprite if in state moving
        self.__update_offset()
        for sprite in self.sprites():
            if issubclass(type(sprite), Building) and sprite.state == BuildingState.PLACING:
                offset_pos = sprite.rect.center = pygame.mouse.get_pos()
            else:
                offset_pos = sprite.pos = sprite.rect.topleft + self.offset
            sprite_coordinates = Vector2(sprite.pos)
            if SCREEN_WIDTH > sprite_coordinates.x > -100 and\
               SCREEN_HEIGHT > sprite_coordinates.y > -100:
                # Draw only the sprites withing the screen dimensions and a bit to the side
                pygame.display.get_surface().blit(sprite.image, offset_pos)
            if issubclass(type(sprite), Unit):
                sprite.update_rect(offset_pos)

    def get_state(self):
        for item in self.__dict__:
            item
        return self
