from game_object import GameObject


class Unit(GameObject):
    def __init__(self, id, name, x, y, hp):
        super().__init__(id, name, x, y)
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0 
