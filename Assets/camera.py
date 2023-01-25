import pygame
from pygame.math import Vector2

from Assets.AOESprite.aoe_sprite import AOESprite
from Assets.Buildings.states import BuildingState
from Assets.Units.states import UnitState
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.Units.unit import Unit
from Assets.UserInterface.ui_group import UIGroup
from Assets.Buildings.building import Building
from Assets.settings import MAP_SIZE, TILE_SIZE
from Assets.Resources.resource import Resource
from Assets.UserInterface.ui import UI
from Assets.UserInterface.Buttons.button import Button
from Assets.tile import Tile
from Assets.UserInterface.text import Text

MAP_BORDER_Y = (MAP_SIZE.elementwise()*TILE_SIZE).y/2
MAP_BORDER_X = (MAP_SIZE.elementwise()*TILE_SIZE).x/2


class Camera:

    def __init__(self):
        self.offset = pygame.math.Vector2(0, 0)
        self.offsetX = self.offsetY = 0
        self.ui_group = UIGroup()
        self.unit_group = pygame.sprite.Group()
        self.building_group = pygame.sprite.Group()
        self.resource_group = pygame.sprite.Group()
        self.mutable = pygame.sprite.Group()
        self.tile_group = pygame.sprite.Group()
        self.rendered_sprites = pygame.sprite.Group()
        self.has_mill = False
        self.screen_offset_x = self.screen_offset_y = 0

    def __add_to_subgroup(self, sprite):
        try:
            if issubclass(type(sprite), AOESprite) and self.__to_render(sprite):
                self.rendered_sprites.add(sprite)
            if issubclass(type(sprite), Building):
                sprite.add([self.building_group, self.mutable])
            elif issubclass(type(sprite), Unit):
                sprite.add([self.unit_group, self.mutable])
            elif issubclass(type(sprite), Resource):
                sprite.add([self.resource_group, self.mutable])
            elif issubclass(type(sprite), UI) or issubclass(type(sprite), Button) or issubclass(type(sprite), Text):
                self.ui_group.add(sprite)
            elif issubclass(type(sprite), Tile):
                self.tile_group.add(sprite)
        except AttributeError as E:
            print(E)
            for item in sprite:
                self.__add_to_subgroup(item)

    def add(self, sprites):
        try:
            for sprite in sprites:
                self.__add_to_subgroup(sprite)
        except TypeError:
            self.__add_to_subgroup(sprites)
        else:
            pass
            # TODO Log error message

    def __update_offset(self):
        # By How much should the screen move
        offset_pixels = 15
        mouse_pos = pygame.mouse.get_pos()
        total_offset_y = total_offset_x = 0
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        # Left side of screen
        if mouse_x <= 3 and self.screen_offset_x > -MAP_BORDER_X:
            total_offset_x -= offset_pixels
            self.screen_offset_x -= offset_pixels
            self.offsetX += offset_pixels
        # Right side of screen
        elif mouse_x >= SCREEN_WIDTH - 3 and self.screen_offset_x < MAP_BORDER_X - (SCREEN_WIDTH + 50):
            total_offset_x += offset_pixels
            self.screen_offset_x += offset_pixels
            self.offsetX -= offset_pixels
        # Top of the screen
        if mouse_y <= 3 and self.screen_offset_y > -MAP_BORDER_Y:
            total_offset_y -= offset_pixels
            self.screen_offset_y -= offset_pixels
            self.offsetY += offset_pixels
        # Bottom of the screen
        elif mouse_y >= SCREEN_HEIGHT - 3 and self.screen_offset_y < MAP_BORDER_Y - (SCREEN_HEIGHT + 50):
            total_offset_y += offset_pixels
            self.screen_offset_y += offset_pixels
            self.offsetY -= offset_pixels
        self.offset = Vector2(self.offsetX, self.offsetY)
        # Don't touch, this fixed the player offset for out of screen movement
        for unit in self.unit_group:
            if unit.state == UnitState.MOVING:
                unit.update_target_offset((total_offset_x, total_offset_y))

    @staticmethod
    def __to_render(sprite):
        sprite_coordinates = Vector2(sprite.pos)
        return (SCREEN_WIDTH > sprite_coordinates.x > -100 and
                SCREEN_HEIGHT > sprite_coordinates.y > -100)

    def custom_draw(self):
        # To Do: Don't update unit sprite if in state moving
        for tile in self.tile_group:
            offset_pos = tile.pos = tile.rect.topleft + self.offset
            if self.__to_render(tile):
                pygame.display.get_surface().blit(tile.image, offset_pos)

        for sprite in sorted(self.rendered_sprites, key=lambda sprite: sprite.rect.centery):
            sprite.draw(pygame.display.get_surface(), sprite.pos)

    def update(self):
        self.__update_offset()
        for sprite in self.mutable:
            sprite.custom_update()
            if issubclass(type(sprite), Building) and sprite.state == BuildingState.PLACING:
                pass
            else:
                sprite.pos = sprite.rect.topleft + self.offset
            if self.__to_render(sprite):        # If the sprite pos is inside the screen dimensions add it to group
                self.rendered_sprites.add(sprite)
            elif self.rendered_sprites.has(sprite):   # If not in screen dimensions and inside the group, remove it
                self.rendered_sprites.remove(sprite)
            if issubclass(type(sprite), Unit):
                sprite.update_rect(sprite.pos)

    def get_state(self):
        pass
        # TODO: Write a custom method to serialize the Class data
