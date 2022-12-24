import pygame
import sys
from pygame.math import Vector2
import Assets.Units.unit
sys.setrecursionlimit(1500)


class Controls:
    selectedObjects = []

    @staticmethod
    def event_handler(unit_group, ui_group):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Turn on/off game pause
                ui_group.set_pause()
            # Check if left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                mouse_pos = Vector2(pygame.mouse.get_pos())
                print("Mouse_pos")
                print(mouse_pos)
                print("Unit pos")
                selected_count = 0
                for unit in unit_group.sprites():  # Need to perform ray-cast somehow
                    print(unit.pos)
                    if unit.pos.x + unit.rect.w > mouse_pos.x > unit.pos.x - unit.rect.w and \
                       unit.pos.y + unit.rect.h > mouse_pos.y > unit.pos.y - unit.rect.h:
                        unit.select_unit()
                        __class__.selectedObjects.append(unit)
                        selected_count += 1
            # Check if right mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                mouse_pos = Vector2(pygame.mouse.get_pos())
                print(mouse_pos)
                for obj in __class__.selectedObjects:
                    obj.set_move(mouse_pos)
                    print("")
                    print(obj.pos)

