class Weapon:
    weapons = []
    def __init__(self, name, damage, speed, weight):
        self.name = name
        self.damage = damage
        self.speed = speed
        self.weight = weight
        Weapon.weapons.append(self)

    def quickAttack(self):
        self.damage = 3


class BoxingGloves(Weapon):
    def __init__(self, name="Boxing Gloves", damage=6, speed=15, weight=8):
        super().__init__(name, damage, speed, weight)
        # self.pound
        Weapon.weapons.append(self)
    
    def hayMaker(self):
        self.damage = 10
    

class AK47(Weapon):
    def __init__(self, name="AK-47", damage=2, speed=30, weight=15):
        super().__init__(name, damage, speed, weight)
        Weapon.weapons.append(self)
    
    def burst(self):
        self.damage = 6
        self.speed = 15

class Nunchucks(Weapon):
    def __init__(self, name="nunchucks", damage=8, speed=20, weight=5):
        super().__init__(name, damage, speed, weight)
        Weapon.weapons.append(self)

    def whip(self):
        self.damage = 7

    def helicopter_spin(self):
        self.speed = self.speed + 2

class FlameSword(Weapon):
    def __init__(self, name = "Flame Sword", damage = 8, speed = 10, weight = 5):
        super().__init__(name, damage, speed, weight)
        Weapon.weapons.append(self)

    def fire(self):
        self.damage = 10
        self.speed = 15