class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self, Pet):
        Pet.play()
        return self
    
    def feed(self, Pet):
        Pet.eat()
        return self
    
    def bathe(self, Pet):
        Pet.noise()
        return self
    

class Pet(Ninja):
    def __init_subclass__(cls):
        return super().__init_subclass__()

    def __init__(self, name,type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print("THE PET'S SOUND")

    def showPetStats(self):
        print("health: ", self.health)
        print("Energy: ", self.energy)

dog = Pet("Sahsa", "dog", "flip", 500, 10)
belle = Ninja("Belle", "Weiler", dog, "cookie", "chicken")


belle.walk(dog).feed(dog).bathe(dog)

dog.showPetStats()