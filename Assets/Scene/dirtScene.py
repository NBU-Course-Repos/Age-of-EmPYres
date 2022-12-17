from scene import Scene

MAP_LAYOUT = [['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt'],
              ['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt'],
              ['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt'],
              ['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt'],
              ['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt'],
              ['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt'],
              ['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt'],
              ['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt'],
              ['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt'],
              ['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt'],
              ['dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt','dirt']]


class DirtScene(Scene):

    def __init__(self):
        super().__init__(tile_type="dirt")


scene = DirtScene()

scene.print_scene()
