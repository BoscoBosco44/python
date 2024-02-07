from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.gear import Weapon, BoxingGloves, Nunchucks, AK47, FlameSword

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

Gloves = BoxingGloves()
nunchucks = Nunchucks()
ak47 = AK47()
flamesword = FlameSword()

michelangelo.getWeapon(Gloves)

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

# roundCounter = 0


# def playGame():
#     while (michelangelo.health > 0 & jack_sparrow.health > 0):
#         print("Round: ", roundCounter)
#         weaponCounter = 0
#         michelangelo.getWeapon(nunchucks)
#         jack_sparrow.getWeapon(flamesword)

#         michelangelo.attack(jack_sparrow)
#         jack_sparrow.attack(michelangelo)

#         michelangelo.show_stats()
#         jack_sparrow.show_stats()

# print(playGame())