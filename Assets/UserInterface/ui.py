import pygame
from Assets.settings import SCREEN_HEIGHT,SCREEN_WIDTH
from pygame.math import Vector3 as Vector3
from pygame.math import Vector2 as Vector2


class UI(pygame.sprite.Sprite):
    def __init__(self, group, color_set=Vector3(255, 204, 153)):
        super().__init__(group)
        self.bb_dimensions = Vector2(SCREEN_WIDTH-SCREEN_WIDTH/3, SCREEN_HEIGHT/4.5)
        self.image = pygame.image.load("Assets//Textures//bottom_bar.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, self.bb_dimensions)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-75))

