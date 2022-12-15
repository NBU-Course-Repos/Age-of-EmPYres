from Assets.Tile import TILE_SIZE
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 704


class Scene:
    predefined_layout = [[]]

    def __init__(self, tile_type="", layout=[[]]):
        if len(layout) == 1:
            for row in range(0, int(SCREEN_WIDTH/TILE_SIZE)):
                for col in range(0, int(SCREEN_HEIGHT/TILE_SIZE)):
                    self.predefined_layout[row][col] = tile_type
        else:
            self.predefined_layout = layout

    def print_scene(self):
        print("Printing\n")
        for row in range(0, len(self.predefined_layout)):
            for col in range(0, len(self.predefined_layout[row])):
                print(self.predefined_layout[row][col])
            print('\n')


scene = Scene("dirt")
Scene.print_scene()