class Pirate:

    def __init__(self , name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def attack (self, ninja):
        ninja.health -= self.strength
        if (ninja.health <= 0):
            print("Fatality")
        else:
            print(f"{self.name}'s attack did {self.strength} damage!")
        return self

class Ancient(Pirate):
    def __init__(self, name):
        super().__init__(self)
        self.strength = 30
        self.speed = 6
        self.health = 200
        self.name = name
    def attack (self, Kunoichi):
        super().attack(Kunoichi)
        if (Kunoichi.health <= 0):
            print("Fatality")
        return self