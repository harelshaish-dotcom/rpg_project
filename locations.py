import abc
import random
from collections import Counter
from npc_classes import Goblin, Skeleton, Enemy, Entity, Zombie

class Location(abc.ABC):
    def __init__(self, name: str, description: str, obtainable_items: dict, enemies: dict):
        self.name = name
        self.description = description
        self.enemies = enemies
        self.obtainable_items = obtainable_items

    @abc.abstractmethod
    def welcome(self):
        pass

    @abc.abstractmethod
    def spawn_enemies(self):
        pass

    @abc.abstractmethod
    def ReadDescription(self):
        pass

    @abc.abstractmethod
    def ObtainableItems(self):
        pass

class Forest(Location):
    def __init__(self):
        super().__init__(name="Aurora Vale", description="A serene forest bathed in eternal dawn, where light drifts between the trees like living breath.", obtainable_items = {}, enemies = {})

    def welcome(self):
        print(f"You have entered {self.name}.")

    def spawn_enemies(self):
        self.enemies[Skeleton()] = random.randint(1, 2)
        self.enemies[Zombie()] = random.randint(1, 2)

        return self.enemies

    def ReadDescription(self):
        print(self.description)

    def ObtainableItems(self):
        drops = []
        self.obtainable_items["Flesh"] = random.randint(1, 2)
        self.obtainable_items["Wolf Pelt"] = random.randint(0, 1)

        if random.random() < 0.2:
            self.obtainable_items["Iron"] = 1

        for item, qty in self.obtainable_items.items():
            if qty > 0:
                drop_string = f"{qty} {item}"
                drops.append(drop_string)
        if drops:
            print(f"You found " + " and ".join(drops) + "!")
        else:
            print("You have not found any items.")

class Castle(Location):
    def __init__(self):
        super().__init__(name="Hall of Glory", description="A radiant castle of heroes, echoing with voices that no longer exist.", obtainable_items = {}, enemies = {})

    def welcome(self):
        print(f"You have entered {self.name}.")

    def spawn_enemies(self):
        self.enemies[Goblin()] = random.randint(1, 2)
        self.enemies[Skeleton()] = random.randint(1, 2)

        return self.enemies

    def ReadDescription(self):
        print(self.description)

    def ObtainableItems(self):
        drops = []
        self.obtainable_items["Gold"] = random.randint(1, 3)
        self.obtainable_items["Iron"] = random.randint(0, 2)

        if random.random() < 0.1:
            self.obtainable_items["Healing Potion"] = 1

        for item, qty in self.obtainable_items.items():
            if qty > 0:
                drop_string = f"{qty} {item}"
                drops.append(drop_string)
        if drops:
            print(f"You found " + " and ".join(drops) + "!")
        else:
            print("You have not found any items.")

class Sky(Location):
    def __init__(self):
        super().__init__(name="Celestial Garden", description="A floating haven above the clouds, peaceful… yet uneasy beneath its perfection.", obtainable_items = {}, enemies = {})

    def welcome(self):
        print(f"You have entered {self.name}.")

    def spawn_enemies(self):
        self.enemies[Goblin()] = random.randint(1, 2)
        self.enemies[Zombie()] = random.randint(1, 2)

        return self.enemies

    def ReadDescription(self):
        print(self.description)

    def ObtainableItems(self):
        drops = []
        self.obtainable_items["Iron"] = random.randint(1, 3)
        self.obtainable_items["Healing potion"] = random.randint(0, 2)

        if random.random() < 0.15:
            self.obtainable_items["Gold"] = 1

        for item, qty in self.obtainable_items.items():
            if qty > 0:
                drop_string = f"{qty} {item}"
                drops.append(drop_string)
        if drops:
            print(f"You found " + " and ".join(drops) + "!")
        else:
            print("You have not found any items.")
