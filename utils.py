from data_types import CoffeeInf, CoffeeKind
from typing import Sequence


def convert_to_coffeeinf(data: Sequence) -> CoffeeInf:
    if data[2] == "молотый":
        kind = CoffeeKind.GROUND
    else:
        kind = CoffeeKind.BEANS

    result = CoffeeInf(
        sort=data[0],
        degree_of_roasting=data[1],
        kind=kind,
        taste_description=data[3],
        price=int(data[4]),
        volume=float(data[5]),
    )
    return result
