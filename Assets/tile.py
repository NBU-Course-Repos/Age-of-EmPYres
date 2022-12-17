import pygame
TILE_SIZE = 64


class Tile(pygame.sprite.Sprite):
    TILE_VARIATIONS = ['sand', 'dirt']

    def __init__(self, pos, group, tile_type, size=(TILE_SIZE, TILE_SIZE)):
        super().__init__(group)
        self.image = pygame.image.load(f"Assets/Textures/{tile_type}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=pos)
