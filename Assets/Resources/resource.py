import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.sprite import Group
from Assets.Resources.types import ResourceType


class Resource(Sprite):
    def __init__(self, pos: Vector2, group: Group, rtype: ResourceType, image_enum=1, amount=100, tile=None):
        super().__init__(group)
        self.pos = Vector2(pos)
        self.resource_type = rtype
        self.amount = amount
        self.tile = tile
        try:
            self.image = pygame.image.load(f"Assets/Textures/Resources/{self.resource_type.value}_{image_enum}.png")
        except FileNotFoundError:
            self.image = pygame.image.load(f"Assets/Textures/Resources/{self.resource_type}_1.png")
        if self.resource_type == ResourceType.WOOD:
            self.image = self.image = pygame.transform.scale(self.image, (64, 100))
        self.rect = self.image.get_rect(midbottom=tile.rect.center)
        # pygame.draw.rect(surface=self.image,
        #                  color=(255, 255, 255),
        #                  rect=[0, 0, self.rect.x, self.rect.y],
        #                  width=1)

    def select(self):
        self.tile.draw_border()
        # print(self)
        # print(self.amount)
        # To do: Give information on self.amount

    def deselect(self):
        self.tile.delete_border()

