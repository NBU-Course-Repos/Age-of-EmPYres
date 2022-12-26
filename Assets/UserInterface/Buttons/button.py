import pygame
from pygame.math import Vector2


class Button(pygame.sprite.Sprite):
    def __init__(self, pos=Vector2(0, 0), group=pygame.sprite.AbstractGroup(), dimensions=Vector2(40,40), image=""):
        super().__init__(group)
        self.border_dimensions = dimensions
        self.pos = pos
        self.image = pygame.image.load(f"Assets//Textures//Icons//{image}.png")
        self.image = pygame.transform.scale(self.image, self.border_dimensions)
        self.rect = self.image.get_rect(topleft=self.pos)

    def action(self):
        return
        # Do something