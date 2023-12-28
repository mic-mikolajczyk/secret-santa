from dataclasses import dataclass, field
from models.gift import Gift


@dataclass
class Player:
    name: str = None
    email: str = None
    gift_to_buy: Gift = None
    drawn_name = None
    whish_list: list[Gift] = field(default_factory=list)

    def append_whish_list(self):
        ...

    def set_gift_to_buy(self):
        ...
