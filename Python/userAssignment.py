class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("Name: ", self.first_name)
        print("Last-name: ", self.last_name)
        print("Email: ", self.email)
        print("Age: ", self.age)
        print("Rewards Member: ", self.is_rewards_member)
        print("Points: ", self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if 0 < (self.gold_card_points - amount):
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("User needs ", (self.gold_card_points - amount) * (-1), " more points")
        return self
            

    

Peter = user("Peter", "Bosco", "email@email.com", 426).display_info().enroll().spend_points(50).display_info().enroll()
Sofi = user("Sofi", "Bosco", "sofi@email.com", 12).display_info()
Luca = user("Luca", "Bosco", "luca@gmail.com", 14).display_info().enroll().spend_points(80).display_info().spend_points(1000)


# Peter.display_info()
# Sofi.display_info()
# Luca.display_info()

# Peter.enroll()
# Peter.spend_points(50)

# Luca.enroll()
# Luca.spend_points(80)

# Peter.display_info()
# Luca.display_info()

# Peter.enroll()
# Luca.spend_points(1000)

