import pygame
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.map import Map
from Assets.camera import CameraGroup
from Assets.Units.villager import Villager
from Assets.Controls.controls import Controls

# Generate the Map before the pygame windows is started
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Age of Empyres")
pygame.display.set_icon(pygame.image.load("Assets/Textures/grail.png"))
camera = CameraGroup()

world = Map(camera)

clock = pygame.time.Clock()
camera.custom_draw()
villager = Villager(camera)
villager.add(camera.unit_group)

start_ticks = pygame.time.get_ticks()
font = pygame.font.SysFont(None, 24)
img = font.render('hello', True, (0, 0, 0))

while True:
    new_ticks = pygame.time.get_ticks()
    Controls.event_handler(camera)
    if not camera.ui_group.isPaused:
        screen.blit(img, (20, 20))
        screen.fill((0, 204, 0))
        camera.update()
        camera.custom_draw()
        for unit in camera.unit_group.sprites():
            unit.custom_update()
        for building in camera.buildings_group:
            building.custom_update()
        for resource in camera.resources:
            resource.custom_update()
    camera.ui_group.custom_update()
    pygame.display.update()
    clock.tick(60)
