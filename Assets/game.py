import sys
import pygame
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.map import Map
from Assets.Tiles.groups import *

# Generate the Map before the pygame windows is started
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Age of Empyres")
pygame.display.set_icon(pygame.image.load("Assets/Textures/grail.png"))
camera = CameraGroup()
ui_group = UIGroup()

world = Map(camera)

clock = pygame.time.Clock()
camera.custom_draw()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Turn on/off game pause
            ui_group.set_pause()
    if not ui_group.isPaused:
        screen.fill((0, 204, 0))
        camera.update()
        camera.custom_draw()
    ui_group.update()
    ui_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
