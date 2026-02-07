from npc_classes import Goblin, Skeleton, prince
from locations import Location, Forest
from local import entrance, start_menu


def main() -> None:
    while True:
        if not entrance():
            break

if __name__ == "__main__":
    main()