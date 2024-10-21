from building import Building
from moveable import Moveable


class MobileHouse(Building, Moveable):
    def move(self, x, y):
        print(f"{self.get_name()} moves to: {x}, {y}")
        self.set_x(x)
        self.set_y(y)
