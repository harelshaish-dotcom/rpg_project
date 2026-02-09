import abc
import random
from items import Inventory

class Entity(abc.ABC):
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self._health = health
        self.attack_power = attack_power
        self.defense = defense

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    def attack(self, entity):
        pass

class Enemy(Entity):
    def __init__(self, name, health, attack_power, defense):
        super().__init__(name, health, attack_power, defense)
        self.loot = {}

    def attack(self, character):
        damage = max(0, self.attack_power - character.defense)
        character.health -= damage
        print(f"{self.name} dealt {character.name} {damage} damage!")
        print(f"{self.name}: {self.health} hp\n{character.name}: {character.health} hp")

    @abc.abstractmethod
    def drop_loot(self):
        pass

class Prince(Entity):
    def __init__(self, name, health=100, attack_power=18, defense=5):
        super().__init__(name, health, attack_power, defense)
        self.inventory = Inventory()
        

    def attack(self, enemy):
        pass

    def use_item(self, item):
        self.inventory.use(item)

    def pickup_item(self, item, amount=1):
        self.inventory.add(item, amount)

    def display_inventory(self):
        self.inventory.show()

    def view_stats(self):
        print(f"\n{self.name} stats:")
        print(f"  health: {self.health}")
        print(f"  attack power: {self.attack_power}")
        print(f"  defense: {self.defense}")


class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", health=27, attack_power=8, defense=3)
        self.loot = {}

    def attack(self, enemy):
        pass

    def drop_loot(self, enemy):
        self.loot["gold"] = random.randint(1, 3)

        if random.random() < 0.2:
            self.loot["Healing Potion"] = 1

        drops = [f"{qty} {item}" for item, qty in self.loot.items()]
        print(f"{self.name} dropped " + " and ".join(drops) + "!")
        enemy.pickup_item(self.loot)

    def view_stats(self):
        print(f"\n{self.name} stats:")
        print(f"  health: {self.health}")
        print(f"  attack power: {self.attack_power}")
        print(f"  defense: {self.defense}")

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", health=35, attack_power=10, defense=2)
        self.loot = {}


    def attack(self, enemy):
        pass



    def drop_loot(self, enemy):
        self.loot["bones"] = random.randint(1, 3)

        if random.random() < 0.15:
            self.loot["Healing Potion"] = 1

        drops = [f"{qty} {item}" for item, qty in self.loot.items()]
        print(f"{self.name} dropped " + " and ".join(drops) + "!")
        enemy.pickup_item(self.loot)

    def view_stats(self):
        print(f"\n{self.name} stats:")
        print(f"  health: {self.health}")
        print(f"  attack power: {self.attack_power}")
        print(f"  defense: {self.defense}")


class Zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie", health=15, attack_power=27, defense=5)
        self.loot = {}

    def attack(self, enemy):
        pass

    def drop_loot(self, enemy):
        self.loot["flesh"] = random.randint(1, 3)

        if random.random() < 0.15:
            self.loot["gold"] = 1

        drops = [f"{qty} {item}" for item, qty in self.loot.items()]
        print(f"{self.name} dropped " + " and ".join(drops) + "!")
        enemy.pickup_item(self.loot)

    def view_stats(self):
        print(f"\n{self.name} stats:")
        print(f"  health: {self.health}")
        print(f"  attack power: {self.attack_power}")
        print(f"  defense: {self.defense}")
