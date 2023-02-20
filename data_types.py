from enum import Enum
from typing import NamedTuple


class CoffeeKind(Enum):
    GROUND = "молотый"
    BEANS = "в зёрнах"


class CoffeeInf(NamedTuple):
    sort: str
    degree_of_roasting: str
    kind: CoffeeKind
    taste_description: str
    price: int
    volume: float
