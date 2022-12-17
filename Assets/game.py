import sys
import pygame
from Assets.camera import CameraGroup
from Assets.tile import Tile, TILE_SIZE
from Assets.Scene.baseScene import MAP_LAYOUT
from Assets.settings import  SCREEN_WIDTH, SCREEN_HEIGHT
# TO DO: IMPLEMENT VARIABLES LIKE SCREEN SIZE AND TILE SIZE via XML file

#
# def render_map(map_layout, tile_type):
#     for row_index, row in enumerate(map_layout):
#         for col_index, col in enumerate(row):
#             x = col_index * TILE_SIZE;
#             y = row_index * TILE_SIZE;
#             if col == tile_type:
#                 Tile(pos=(x, y), group=tiles_group, tile_type=tile_type)

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Age of Empyres")

clock = pygame.time.Clock()
camera = CameraGroup()
group = pygame.sprite.Group()

for row_index, row in enumerate(MAP_LAYOUT):
    for col_index, col in enumerate(row):
        x = col_index * TILE_SIZE;
        y = row_index * TILE_SIZE;
        Tile(pos=(x, y), group=camera, tile_type="sand")

camera.print()

while True:
    print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 204, 0))

    camera.update()
    camera.custom_draw()
    pygame.display.update()
    clock.tick(60)
