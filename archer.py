from unit import Unit
from moveable import Moveable
from attacker import Attacker


class Archer(Unit, Moveable, Attacker):
    def __init__(self, id, name, x, y, hp, attack_power):
        super().__init__(id, name, x, y, hp)
        self.attack_power = attack_power

    def attack(self, unit: Unit):
        if isinstance(unit, Unit) and unit.is_alive():
            damage = self.attack_power * 0.9  # Calculate damage
            unit.receive_damage(damage)
            print(f"{unit.get_name()} received damage: {damage}")
        else:
            print(f"{unit.get_name()} cannot be attacked.")

    def move(self, x, y):
        print(f"{self.get_name()} moves to: {x}, {y}")
        self.set_x(x)
        self.set_y(y)
