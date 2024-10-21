from building import Building
from unit import Unit
from attacker import Attacker


class Fort(Building, Attacker):
    def __init__(self, id, name, x, y, is_built, cannon_power):
        super().__init__(id, name, x, y, is_built)
        self.cannon_power = cannon_power

    def attack(self, unit: Unit):
        if isinstance(unit, Unit) and unit.is_alive():
            unit.receive_damage(self.cannon_power)
            print(f"{unit.get_name()} was hit by cannon fire for {self.cannon_power}")
        else:
            print(f"{unit.get_name()} cannot be attacked.")
