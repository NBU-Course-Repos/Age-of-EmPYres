import sys
import pygame
from Assets.Tile import Tile, TILE_SIZE
# TO DO: IMPLEMENT VARIABLES LIKE SCREEN SIZE AND TILE SIZE via XML file


def render_map(map_layout, tile_type):
    for row_index, row in enumerate(map_layout):
        for col_index, col in enumerate(row):
            x = col_index * TILE_SIZE;
            y = row_index * TILE_SIZE;
            if col == tile_type:
                Tile(pos=(x, y), group=tiles_group, tile_type=tile_type)

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 704
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Age of Empyres")

clock = pygame.time.Clock()
tiles_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    tiles_group.update()
    tiles_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
