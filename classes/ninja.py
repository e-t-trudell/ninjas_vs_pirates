class Ninja:
    # strength = 10
    # speed = 5
    # health = 100
    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def attack( self , pirate ):
        pirate.health -= self.strength
        if (pirate.health <= 0):
            print("Fatality")
        else:
            print(f"{self.name}'s attack did {self.strength} damage!")
        return self
    # @classmethod
    # def gain_health(cls):
    #     cls.health = Ninja.health
    #     print(cls.health)
    #     Ninja.health += (ninja.strenth + 2)
    #     print(f"{Ninja.name}: {Ninja.health}")
class Kunoichi (Ninja):
    def __init__(self, name):
        super().__init__(self)
        self.strength = 20
        self.speed = 6
        self.health = 200
        self.name = name
    def attack (self, Ancient):
        super().attack(Ancient)
        # print(Ancient.health)
        # Ancient.health -= self.strength
        if (Ancient.health <= 0):
            print("Fatality")
        return self