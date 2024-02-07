class Pirate:

    def __init__( self , name, weapon=0 ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.holdingWeapon = False
        self.currentWeapon = weapon
        self.hasScurvy = False

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")


    def attack( self , ninja):
        if self.holdingWeapon == False:
            ninja.health -= self.strength
        else:
            ninja.health -= (self.strength + self.currentWeapon.damage) * (self.currentWeapon.speed - self.currentWeapon.weight)
        return self
    
    def getWeapon(self, weapon):
        self.holdingWeapon = True
        self.currentWeapon = weapon