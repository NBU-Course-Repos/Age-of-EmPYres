import pygame
import sys
from pygame.math import Vector2
from Assets.Units.villager import Villager
from Assets.Buildings.house import House
from Assets.Controls.states import ControlStates
from Assets.Buildings.states import BuildingState


def is_clicked(obj, mouse_pos):
    if obj.pos.x + obj.rect.w > mouse_pos.x > obj.pos.x - obj.rect.w and \
       obj.pos.y + obj.rect.h > mouse_pos.y > obj.pos.y - obj.rect.h:
        return True
    return False


class Controls:
    selectedObjects = []
    building: House
    state = ControlStates.NOTHING

    @staticmethod
    def event_handler(camera):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Turn on/off game pause
                camera.ui_group.set_pause()
            # Check if left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if Controls.state == ControlStates.BUILDING:
                    Controls.building.construct()
                    Controls.state = ControlStates.UNIT
                    for unit in Controls.selectedObjects:
                        if type(unit) == Villager:
                            unit.set_construct(Controls.building)

                mouse_pos = Vector2(pygame.mouse.get_pos())
                selected_count = 0

                # Selected Units
                for unit in camera.unit_group.sprites():
                    if is_clicked(unit, mouse_pos):
                        Controls.state = ControlStates.UNIT
                        unit.select(camera.ui_group)
                        Controls.selectedObjects.append(unit)
                        selected_count += 1

                # If any of the ui is clicked, don't deselect the selected objects
                for ui in camera.ui_group.sprites():
                    if is_clicked(ui, mouse_pos):
                        selected_count += 1

                # If button has been clicked, perform its action
                for button in camera.ui_group.buttons:
                    if is_clicked(button, mouse_pos):
                        selected_count += 1
                        button.action(camera, camera.buildings_group)
                        break

                if selected_count == 0 and len(Controls.selectedObjects):
                    # if there aren't any selected object in the last left mouse click deselect
                    # the ones that were previously selected
                    for obj in Controls.selectedObjects:
                        obj.deselect(camera.ui_group)
                    Controls.selectedObjects.clear()

            # Check if right mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                mouse_pos = Vector2(pygame.mouse.get_pos())
                target = None
                # If a foundation is selected set it as a target
                for building in camera.buildings_group.sprites():
                    if is_clicked(building, mouse_pos) and building.state != BuildingState.BUILT:
                        target = building
                        building.highlight_foundation()
                        break
                if Controls.state == ControlStates.UNIT:
                    for obj in Controls.selectedObjects:
                        # if the Unit is a villager and there the target is a foundation,
                        # finish constructing it
                        if target is not None and type(obj) == Villager:
                            obj.set_construct(target)
                        else:
                            obj.set_move(mouse_pos)

                elif Controls.state == ControlStates.BUILDING:
                    Controls.building.kill()  # Stop placing the building

            # House building shortcut
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                Controls.state = ControlStates.BUILDING
                Controls.building = House(camera)
                Controls.building.add(camera.buildings_group)

