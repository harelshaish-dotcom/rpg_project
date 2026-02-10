import json
from dataclasses import dataclass, field
from pathlib import Path
from progress import *
from npc_classes import *

SAVE_DIR = Path("saves")
SAVE_DIR.mkdir(exist_ok=True)

def log_and_save_position(player) -> None:
    """Sets player.last_method to the name of the function that called this."""
    import inspect
    player.last_method = inspect.currentframe().f_back.f_code.co_name


@dataclass
class Player:
    name: str
    current_hp: int = 100
    loot: dict[str, int] = field(default_factory=dict)
    last_method: str | None = None

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "current_hp": self.current_hp,
            "inventory": self.loot,
            "last_method": self.last_method,
        }

    @staticmethod
    def from_dict(data: dict) -> "Player":
        return Player(
            name=data["name"],
            current_hp=int(data.get("current_hp", 100)),
            loot=dict(data.get("loot", [])),
            last_method=data.get("last_method"),
        )


def save_player(player: Player) -> None:
    """Save to saves/<name>.json"""
    path = SAVE_DIR / f"{player.name}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(player.to_dict(), f, ensure_ascii=False, indent=2)


def load_player(name: str) -> Prince:
    path = SAVE_DIR / f"{name}.json"
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return Prince.from_dict(data)