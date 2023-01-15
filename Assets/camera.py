import pygame
from pygame.math import Vector2
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.Units.unit import Unit
from Assets.UserInterface.ui_group import UIGroup
from Assets.Buildings.building import Building
from Assets.settings import MAP_SIZE, TILE_SIZE
from Assets.Resources.resource import Resource
from Assets.UserInterface.ui import UI
from Assets.UserInterface.Buttons.button import Button
from Assets.tile import Tile

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
        self.total_offset_x = self.total_offset_y = 0

    def __add_to_subgroup(self, sprite):
        try:
            if not issubclass(type(sprite), Tile) and self.__to_render(sprite):
                self.rendered_sprites.add(sprite)
            if issubclass(type(sprite), Building):
                sprite.add([self.building_group, self.mutable])
            elif issubclass(type(sprite), Unit):
                sprite.add([self.unit_group, self.mutable])
            elif issubclass(type(sprite), Resource):
                sprite.add([self.resource_group, self.mutable])
            elif issubclass(type(sprite), UI) or issubclass(type(sprite), Button):
                self.ui_group.add(sprite)
            elif issubclass(type(sprite), Tile):
                self.tile_group.add(sprite)
        except AttributeError:
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
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        # Left side of screen
        if mouse_x <= 3 and self.total_offset_x > -MAP_BORDER_X:
            self.total_offset_x -= offset_pixels
            self.offsetX += offset_pixels
        # Right side of screen
        elif mouse_x >= SCREEN_WIDTH - 3 and self.total_offset_x < MAP_BORDER_X - (SCREEN_WIDTH + 50):
            self.total_offset_x += offset_pixels
            self.offsetX -= offset_pixels
        # Top of the screen
        if mouse_y <= 3 and self.total_offset_y > -MAP_BORDER_Y:
            self.total_offset_y -= offset_pixels
            self.offsetY += offset_pixels
        # Bottom of the screen
        elif mouse_y >= SCREEN_HEIGHT - 3 and self.total_offset_y < MAP_BORDER_Y - (SCREEN_HEIGHT + 50):
            self.total_offset_y += offset_pixels
            self.offsetY -= offset_pixels
        self.offset.update(self.offsetX, self.offsetY)

    @staticmethod
    def __to_render(sprite):
        sprite_coordinates = Vector2(sprite.pos)
        return (SCREEN_WIDTH > sprite_coordinates.x > -100 and
                SCREEN_HEIGHT > sprite_coordinates.y > -100)

    def custom_draw(self):
        # To Do: Don't update unit sprite if in state moving
        self.__update_offset()
        for tile in self.tile_group:
            offset_pos = tile.pos = tile.rect.topleft + self.offset
            if self.__to_render(tile):
                pygame.display.get_surface().blit(tile.image, offset_pos)

        for sprite in self.mutable:
            offset_pos = sprite.pos = sprite.rect.topleft + self.offset
            if self.__to_render(sprite):
                self.rendered_sprites.add(sprite)
            elif self.rendered_sprites.has(sprite):
                self.rendered_sprites.remove(sprite)
            if issubclass(type(sprite), Unit):
                sprite.update_rect(offset_pos)

        for sprite in sorted(self.rendered_sprites, key=lambda sprite: sprite.rect.centery):
            pygame.display.get_surface().blit(sprite.image, sprite.pos)

    def update(self):
        for sprite in self.mutable:
            sprite.custom_update()

    def get_state(self):
        pass
        # TODO: Write a custom method to serialize the Class data
