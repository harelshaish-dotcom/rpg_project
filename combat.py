import abc

class weapon(abc.ABC):
    def __init__(self, name: str, attack_power: int, durability: int, description: str):
        self.name = name
        self.attack_power = attack_power
        self.durability = durability
        self.description = description

    @abc.abstractmethod
    def attack(self, enemy):
        pass

    @abc.abstractmethod
    def read_description(self):
        pass


class Sword(weapon):
    def __init__(self):
        super().__init__("Sword", 20, 10, "A legendary sword, forged in the depths of the world")

    def attack(self, enemy):
        enemy.health -= self.attack_power
        self.durability -= 1
        print(f"you dealt {self.attack_power} to {enemy.name}!")

    def read_description(self):
        print(self.description)


class Bow(weapon):
    def __init__(self):
        super().__init__("Bow", 12, 18, "Forged in moonlight, swift as the wind.")

    def attack(self, enemy):
        enemy.health -= self.attack_power
        self.durability -= 1
        print(f"you dealt {self.attack_power} to {enemy.name}!")

    def read_description(self):
        print(self.description)

class Dagger(weapon):
    def __init__(self):
        super().__init__("Dagger", 5, 7, "Dagger description")

    def attack(self, enemy):
        enemy.health -= self.attack_power
        self.durability -= 1
        print(f"you dealt {self.attack_power} to {enemy.name}!")

    def read_description(self):
        print(self.description) 

"""
temporary, unused functions ^
"""
