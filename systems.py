from npc_classes import Skeleton, Zombie, Goblin
from items import  HealingPotion


class TradeSystem:
    def __init__(self):
        self.exchange_rates = {
            "Bone": 4,
            "Iron": 2,
            "Wolf Pelt": 1,
            "Flesh": 2
        }

    def trade_to_gold(self, inventory):
        total_gold = 0
        print("Trading items for gold...\n")

        for item_name, quantity in inventory.items():
            if item_name in self.exchange_rates and quantity > 0:
                rate = self.exchange_rates[item_name]
                gold_from_item = quantity // rate
                if gold_from_item > 0:
                    print(f"Traded {gold_from_item * rate} {item_name}(s) for {gold_from_item} gold.")
                    total_gold += gold_from_item
                    inventory[item_name] -= gold_from_item * rate

        inventory["Gold"] = inventory.get("Gold", 0) + total_gold
        print(f"\nYou earned {total_gold} gold!")
        print("Updated inventory:", inventory)

    """ unused func ^ """

class BattleSystem:
    def __init__(self, player):
        self.player = player

    def start_battle(self, enemies_dict):
        summary = []
        for npc, count in enemies_dict.items():
            summary.append(f"{count} {npc.name}{'s' if count > 1 else ''}")
        print(" and ".join(summary) + " appeared!\n")

        print("Battle begins!\n")

        for npc, count in enemies_dict.items():
            for i in range(count):
                enemy = self.create_enemy(npc.name)
                print(f"You're facing a {enemy.name}!")
                enemy.view_stats()
                self.player.view_stats()
                self.fight(enemy)

                """ showing every hostile npc ^ """

                if self.player.health <= 0:
                    print(f"\n{self.player.name} was defeated...")
                    return

        print("\nAll enemies defeated!\n")

    def create_enemy(self, name):
        mapping = {
            "Skeleton": Skeleton,
            "Zombie": Zombie,
            "Goblin": Goblin
        }
        return mapping[name]()

    def fight(self, enemy):
        while self.player.health > 0 and enemy.health > 0:
            self.show_stats(enemy)

            action = input("Choose action (1. Attack / 2. Heal / 3. View stats): ").lower()
            if action == "attack" or action == "1":
                damage = max(0, self.player.attack_power - enemy.defense)
                enemy.health -= damage
                print(f"\nYou hit {enemy.name} for {damage} damage!")

            elif action == "heal" or action == "2":
                self.player.inventory.use(HealingPotion(), self.player)

            elif action == "view stats" or action == "3":
                enemy.view_stats()
                self.player.view_stats()
                continue

            else:
                print("\nInvalid action!")
                continue

            """ attack menu ^ """


            if enemy.health > 0:
                damage = max(0, enemy.attack_power - self.player.defense)
                self.player.health -= damage
                print(f"{enemy.name} attacks you for {damage} damage!\n")

        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!\n")
            enemy.drop_loot(self.player)
            self.player.inventory.show()

        """ battle calculations ^ """

    def show_stats(self, enemy):
        print(f"\n{self.player.name}: {self.player.health} HP")
        print(f"{enemy.name}: {enemy.health} HP\n")
