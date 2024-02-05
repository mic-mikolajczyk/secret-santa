from dataclasses import dataclass


@dataclass
class Gift:
    name: str = None
    description = None
    price = None

    def set_description(self):
        ...

    def set_price(self):
        ...
