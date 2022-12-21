import sys
import pygame
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.map import Map
from Assets.Tiles.groups import *
from Assets.Units.villager import Villager

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
villager = Villager(camera)

unit_group = pygame.sprite.Group()
villager.add(unit_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Turn on/off game pause
            ui_group.set_pause()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            print("Mouse_pos")
            print(mouse_pos)
            for unit in unit_group.sprites(): # Need to perform raycast somehow
                unit.select_unit()
                print("Unit Pos: ")
                print(unit.rect.center)
                if unit.rect.center == mouse_pos:
                    unit.select_unit()

    if not ui_group.isPaused:
        screen.fill((0, 204, 0))
        camera.update()
        camera.custom_draw()
    ui_group.update()
    ui_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
