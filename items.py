import abc

class Inventory:
    def __init__(self):
        self.items: dict[str, int] = {}

    def add(self, item, amount=1):
        if isinstance(item, dict):
            for key, value in item.items():
                self.items[key] = self.items.get(key, 0) + value
        elif isinstance(item, list):
            for i in item:
                self.items[i] = self.items.get(i, 0) + amount
        else:
            key = item.name if hasattr(item, "name") else item
            self.items[key] = self.items.get(key, 0) + amount

    def remove(self, item, amount=1):
        key = item.name if hasattr(item, "name") else item
        if key in self.items:
            self.items[key] -= amount
            if self.items[key] <= 0:
                del self.items[key]
        else:
            print(f"You don't have {key}!")

    def use(self, item, target=None):
        key = item.name if hasattr(item, "name") else item
        if self.items.get(key, 0) <= 0:
            print(f"You don't have {key}!")
            return

        self.items[key] -= 1
        if self.items[key] <= 0:
            del self.items[key]
        print(f"You used {key}!\n")

        if hasattr(item, "use"):
            if target is not None:
                item.use(target)
            else:
                item.use()

    def display(self):
        if not self.items:
            print("Inventory is empty.")
            return
        print("\nInventory:")
        for name, amount in self.items.items():
            print(f"  {name}: {amount}")

    def to_dict(self) -> dict[str, int]:
        return dict(self.items)

    @staticmethod
    def from_dict(data: dict) -> "Inventory":
        inv = Inventory()
        inv.items = {str(k): int(v) for k, v in data.items()}
        return inv

class item(abc.ABC):
    def __init__(self, name:str, description: str):
        self.name = name
        self.description = description

    @abc.abstractmethod
    def use(self):
        pass

    @abc.abstractmethod
    def read_description(self):
        pass

class HealingPotion(item):
    def __init__(self):
        super().__init__("healing potion", "Restores 20 HP")
        self.healthRes = 20

    def use(self, character):
        if character.health == 100:
            print("You have max health")
        else:
            character.health += self.healthRes
            print(f"Restored {self.healthRes} HP!\n")

    def read_description(self):
        print(self.description)

class Poison(item):
    def __init__(self):
        super().__init__("poison", "Deals 5 damage to enemy")
        self.damage = 5

    def use(self, enemy):
        enemy.health -= self.damage
        print(f"dealt {self.damage} hp to enemy, enemy health: {enemy.health}")

    def read_description(self):
        print(self.description)

class ValueItem(abc.ABC):
    def __init__(self, name:str, value: int, description: str):
        self.name = name
        self.description = description
        self.value = value

    @abc.abstractmethod
    def ReadValue(self):
        pass

    @abc.abstractmethod
    def read_description(self):
        pass

class Gold(ValueItem):
    def __init__(self):
        super().__init__("Gold", 5, "The universal currency of the realm. Traders, mercenaries, and kings all bow to its shine.")

    def ReadValue(self):
        print(f"Value: {self.value}")

    def read_description(self):
        print(self.description)

class Flesh(ValueItem):
    def __init__(self, health: int):
        super().__init__("Gold", 2, "A slab of raw meat. Spoils quickly but can be sold or eaten.")
        self.health = health

    def ReadValue(self):
        print(f"Value: {self.value}")

    def read_description(self):
        print(self.description)

    def eat(self, player):
        player.health += self.health

    def Trade(self, quantity, prince):
        gold_gained = quantity // self.value
        remaining_flesh = quantity % self.value
        print(f"Traded {quantity - remaining_flesh} Flesh for {gold_gained} Gold!")
        prince.inventory["Flesh"] -= (quantity - remaining_flesh)
        prince.inventory["Gold"] = prince.inventory.get("Gold", 0) + gold_gained

class Bones(ValueItem):
    def __init__(self):
        super().__init__("Gold", 4, "Remnants of creatures long dead. Weak in structure but sometimes useful to trade.")

    def ReadValue(self):
        print(f"Value: {self.value}")

    def read_description(self):
        print(self.description)

class WoldPelt(ValueItem):
    def __init__(self):
        super().__init__("Gold", 1, "Soft fur stripped from a wolf. Hunters value it for warmth and fine trade goods.")

    def ReadValue(self):
        print(f"Value: {self.value}")

    def read_description(self):
        print(self.description)

class Iron(ValueItem):
    def __init__(self):
        super().__init__("Gold", 2, "A sturdy metal prized by blacksmiths. Common, but essential for weapons and armor.")

    def ReadValue(self):
        print(f"Value: {self.value}")

    def read_description(self):
        print(self.description)