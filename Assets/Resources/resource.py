import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.sprite import Group
from Assets.Resources.types import ResourceType
from Assets.Resources.states import ResourceStatus
from Assets.UserInterface.text import Text


class Resource(Sprite):
    def __init__(self, pos: Vector2, camera: Group, rtype: ResourceType, image_enum=1, amount=100, tile=None):
        super().__init__(camera)
        self.camera = camera
        self._workers = Group()     # Sprite.Group to store the workers gathering this resource
        self.pos = Vector2(pos)
        self.resource_type = rtype
        self.amount = amount
        self.tile = tile
        self.state = ResourceStatus.UNTOUCHED
        self._start_ticks = 0
        self._time_passed = 0
        self.is_selected = False

        try:
            self.image = pygame.image.load(f"{os.getcwd()}/Textures/Resources/{self.resource_type.value}_{image_enum}.png")
        except FileNotFoundError:
            self.image = pygame.image.load(f"{os.getcwd()}/Textures/Resources/{self.resource_type}_1.png")

        if self.resource_type == ResourceType.WOOD or self.resource_type == ResourceType.STONE:
            self.image = self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect(midbottom=tile.rect.center)
        self.mask = pygame.mask.from_surface(self.image, threshold=200)
        # self.add(group.resources)
        self.ui = []

    def get_workers(self):
        return self._workers.sprites()

    def get_position(self):
        return self.pos

    def add_worker(self, worker):
        if self._workers.has(worker):
            return
        else:
            self.state = ResourceStatus.GATHERED
            self._workers.add(worker)

    def remove_worker(self, worker):
        if self._workers.has(worker):
            self._workers.remove(worker)
        if not self._workers:
            self._start_ticks = 0
            self.deselect()
            self.state = ResourceStatus.UNTOUCHED

    def _generate_ui(self):
        bottom_bar = self.camera.ui_group.bottom_bar
        return [Text(text=f"{self.resource_type.value}", pos=Vector2(bottom_bar.rect.topleft) + (0, 10)),
                Text(text=f"Amount {self.amount}", pos=Vector2(bottom_bar.rect.topleft) + (0, 30))]

    def _display_ui(self):
        self.camera.ui_group.remove(self.ui)
        self.ui = self._generate_ui() # Updates the Amount text
        self.camera.ui_group.add(self.ui)

    def _hide_ui(self):
        for ui in self.ui:
            ui.kill()

    def select(self):
        self.tile.draw_border()
        self.is_selected = True

    def deselect(self):
        self.tile.delete_border()
        self.is_selected = False
        self._hide_ui()

    def _being_gathered(self):
        gather_rate = 0
        if self._start_ticks == 0:
            self._start_ticks = pygame.time.get_ticks()
        time_stamp = int((pygame.time.get_ticks() - self._start_ticks)/1000)
        if time_stamp - self._time_passed == 1:
            self._time_passed = time_stamp
            for worker in self._workers.sprites():
                if worker.resource_carrying[self.resource_type] == worker.resource_capacity[self.resource_type]:
                    worker.set_deposit()
                else:
                    gather_rate += worker.gather_rate
                    worker.resource_carrying[self.resource_type] += worker.gather_rate
            self.amount -= gather_rate
            print(self.amount)
        if self.amount == 0:
            self.deselect()
            self.kill()

    def custom_update(self):
        if self.is_selected:
            self._display_ui()
        if self.state == ResourceStatus.UNTOUCHED:
            return
        if self.state == ResourceStatus.GATHERED:
            self._being_gathered()

