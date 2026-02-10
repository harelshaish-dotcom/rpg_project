from RPG_project.items import HealingPotion
from npc_classes import Prince
from locations import Forest, Sky, Castle
from systems import BattleSystem
from save_system import *

def pre_game():
    while True:
        print("\n1. Start a new game")
        print("2. Load an existing save")
        choice = input("\nWhat do you want to do?\n").lower()
        if choice == "1":
            entrance()
        elif choice == "2" or choice == "load":
            name = input("\nWhat is the name of the progress you want to load?\n")
            try:
                loaded_player = load_player(name)
                state = loaded_player.last_method or "start_menu"
                ROUTES[state](loaded_player)
                print("Save loaded!")
            except FileNotFoundError:
                print("No save found, please try again.")
        else:
            print("Invalid choice, please try again.")

def entrance():
    while True:
        player = Prince(input("What is your name?\n"))
        print(f"\nWelcome to Prince of Valhalla, {player.name}!\n")
        print("In this game, you'll explore Valhalla and counter ruthless enemies,")
        print("try to defeat those enemies to get their loot.\n")
        print("Every choice you make, will affect your advantage in the game.")
        print("Try to defeat every threat you encounter to reach the end.\n")
        print("May Valhalla gods be with you, good luck.\n")

        return start_menu(player)

def fight(player, place):
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
        print(f'\nGolden halls stretch endlessly before you, bathed in soft light, so calm and perfect it almost feels wrong.\n')
        print("You search for valuable items..")
        location.ObtainableItems()
        print(f"\nA strange door catches your eye, you go look..")
        print("You slightly open it..\n")
        print("You see... enemies!\n")
        enemies = location.spawn_enemies()
        battle.start_battle(enemies)
    return player


def start_menu(player):
    while True:
        print("1. Start a new game")
        print("2. View story")
        print("3. Exit")
        choice = input("\nWhat do you want to do?\n").lower()
        if choice == "1":
            part1(player)
        elif choice == "2":
            entrance()
        elif choice == "3" or choice == "exit":
            break
        else:
            print("Invalid choice!\n")

def part1(player):
    print("You wake up on the cold ground, surrounded by tall trees.")
    print("The air is quiet, but you can hear the wind move through the leaves.\n")
    print("Soft light shines between the branches, warm but weak.\n")
    print("Everything feels calm... yet something about this place isn’t right.\n")
    print("You take a deep breath — and feel like someone, or something, is watching you.\n\n")

    return forest_scene(player)

def forest_scene(player):
    print(f"You continue walking..")
    fight(player, "Forest")
    player.pickup_item("healing potion", 2)
    post_forest(player)
    return player

def post_forest(player):
    print("\nYou survived that, barely..\n")
    print("In here, these things happen all the time, so be careful.\n")
    print("Because you didn't know, your health has been restored, and you've been given two healing potions,")
    print("no more gifts from now on.")
    player.health = 100
    print("\nEvery enemy you kill might drop their loot, so be aware.\n")
    print("Loot can be exchanged at the local store for goodies,")
    print("when an enemy drops loot, it will add to your Inventory.\n")
    player.display_inventory()
    decision1(player)

def decision1(player):
    player.last_method = "post_forest"
    print("\n1. Continue exploring.")
    print("2. Save your progress")
    print("3. Quit the game.")
    choice = input(f"\nSo.. what do you want to do now, {player.name}?\n")
    if choice == "1":
        sky_scene(player)
    elif choice == "2":
        save_player(player)
        return
    elif choice == "3":
        return
    else:
        print("Invalid choice, please try again.")
        decision1(player)

def sky_scene(player):
    print("After that encounter, you know you need to be more carful.")
    print("You start walking to exit the Forest..\n")
    print("You've found the exit! but something catches your eye,")
    print("A big, long poll appears from no where, disappears in the clouds, and it seems to be leading somewhere...\n")
    print("You go check it out, and as soon as you climb to the top, big and bright sunlight hits your face.")
    fight(player, "Sky")
    post_sky(player)


def post_sky(player):
    print(f"\nWell done {player.name}, you're getting much better,")
    print("but dont let your guard down, not until you get out...\n")
    player.display_inventory()
    decision2(player)

def decision2(player):
    player.last_method = "post_sky"
    print("\n1. Continue exploring.")
    print("2. Save your progress and quit the game.")
    print("3. Quit the game.")
    choice = input(f"\nWhat's next, {player.name}?\n")
    if choice == "1":
        castle_scene(player)
    elif choice == "2":
        save_player(player)
        return
    elif choice == "3":
        return
    else:
        print("Invalid choice, please try again.")
        decision2(player)

def castle_scene(player):
    print("You got down from the pole, and continued walking..\n")
    print("After sometime, you see something in the distance,")
    print("you get closer.. it seems like.. a castle!")
    print("You stand before it, a radiant castle of heroes, echoing with voices that no longer exist.\n")
    print("Its towering walls shine with a faded brilliance, as if they remember battles long past.")
    print("The air feels heavy with honor and loss, silent yet filled with stories begging to be heard.\n")
    print("For a moment, it feels as though the castle is watching you… measuring whether you belong.")
    print(f"\nYou've entered the castle through the majestic doors.\n")
    fight(player, "Castle")
    post_castle(player)

def post_castle(player):
    print(f"\nWell done! {player.name}, you've done it!!")
    print("You slayed monsters, and survived every threat.\n")
    player.display_inventory()
    end_game(player)

def end_game(player):
    player.last_method = "post_castle"
    print("\n1. Save your progress and quit the game.")
    print("2. Quit without saving.")
    choice = input(f"\nWhat do you want to do, {player.name}?\n")
    if choice == "1":
        save_player(player)
        return
    elif choice == "2":
        return
    else:
        print("Invalid choice, please try again.")
        end_game(player)

ROUTES = {
    "post_forest": post_forest,
    "post_sky": post_sky,
    "post_castle": post_castle,
}