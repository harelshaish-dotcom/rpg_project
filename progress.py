from npc_classes import Prince
from locations import Forest, Sky, Castle
from systems import BattleSystem
from items import HealingPotion

def Entrance():
    while True:
        player = Prince(input("What is your name?\n"))
        print(f"\nWelcome to Prince of Valhalla, {player.name}!\n")
        print("In this game, you'll explore Valhalla and counter ruthless enemies,")
        print("try to defeat those enemies to get their loot.\n")
        print("Every choice you make, will affect your advantage in the game.")
        print("Try to defeat every threat you encounter to reach the end.\n")
        print("May Valhalla gods be with you, good luck.\n")

        return Start_menu(player)

def Fight(player, place):
    battle = BattleSystem(player)
    if place == "Forest":
        location = Forest()
        location.welcome()
        print("\nYou search for valuable items..")
        location.ObtainableItems()
        print(f"\nAnd before you could ever notice - something jumps from the trees!\n")
        print(f"You encountered enemies!\n")
        enemies = location.spawn_enemies()
        battle.start_battle(enemies)
    elif place == "Sky":
        location = Sky()
        location.welcome()
        print(f'\n"This place looks like heaven!" you thought. Angles fly in the sky, peaceful music plays, everything seems so.. quite.\n')
        print("You search for valuable items..")
        location.ObtainableItems()
        print(f"\nYou look to the side, and you see a cute cabin. Maybe you can get answers there.")
        print("Knock knock knock.. no one answers, you decide to go in.")
        print("You see... enemies!\n")
        enemies = location.spawn_enemies()
        battle.start_battle(enemies)
    elif place == "Castle":
        location = Castle()
        location.welcome()
        enemies = location.spawn_enemies()
        battle.start_battle(enemies)
    return player


def Start_menu(player):
    while True:
        print("1. start a new game")
        print("2. view story")
        print("3. exit")
        choice = input("\nWhat do you want to do?\n")
        if choice == "1":
            part1(player)
        elif choice == "2":
            Entrance()
        elif choice == "3":
            return False
        else:
            print("Invalid choice!\n")

def part1(player):
    print("You wake up on the cold ground, surrounded by tall trees.")
    print("The air is quiet, but you can hear the wind move through the leaves.\n")
    print("Soft light shines between the branches, warm but weak.\n")
    print("Everything feels calm... yet something about this place isn’t right.\n")
    print("You take a deep breath — and feel like someone, or something, is watching you.\n\n")

    return Game_start(player)


def Game_start(player):
    Forest_Scene(player)

def Forest_Scene(player):
    print(f"You continue walking..")
    Fight(player, "Forest")
    post_forest(player)
    return player

def post_forest(player):
    print("You survived that, barely..\n")
    print("In here, these things happen all the time, so be careful.\n")
    print("Because you didn't know, your health has been restored,")
    print("no more gifts from now on.")
    player.health = 100
    print("\nEvery enemy you kill might drop their loot, so be aware.\n")
    print("Loot can be exchanged at the local store for goodies,")
    print("when an enemy drops loot, it will add to your Inventory.\n")
    player.display_inventory()
    decision1(player)

def decision1(player):
    print("\n1. Continue exploring.")
    print("2. (maybe add smth)")
    choice = input(f"\nso.. what do you want to do now, {player.name}?\n")
    if choice == "1":
        Sky_scene(player)
    elif choice == "2":
        pass

def Sky_scene(player):
    print("After that encounter, you know you need to be more carful.")
    print("You start walking to exit the Forest..\n")
    print("You've found the exit! but something catches your eye,")
    print("A big, long poll appears from no where, disappears in the clouds, and it seems to be leading somewhere...\n")
    print("You go check it out, and as soon as you climb to the top, big and bright sunlight hits your face.")
    Fight(player, "Sky")