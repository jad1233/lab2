from game_object import GameObject


class Building(GameObject):
    def __init__(self, id, name, x, y, is_built):
        super().__init__(id, name, x, y)
        self.is_built = is_built
