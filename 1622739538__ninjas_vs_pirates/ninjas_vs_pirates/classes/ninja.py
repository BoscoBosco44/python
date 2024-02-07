from classes.gear import Weapon
class Ninja:

    def __init__( self , name, weapon=0 ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.holdingWeapon = False
        self.currentWeapon = Weapon("Fists", 3, 15, 4)
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate):
        pirate.health -= (self.strength + self.currentWeapon.damage) * (self.currentWeapon.speed - self.currentWeapon.weight)
        return self
    
    def getWeapon(self, weapon):
        self.holdingWeapon = True
        self.currentWeapon = weapon
    # def attckWithWeapon(self, pirate, weapon):
    #     self.weapon = weapon
    #     pirate.health -= self.holdingWeapon.damage