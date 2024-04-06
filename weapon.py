from dataclasses import dataclass
from uuid import UUID, uuid1

@dataclass(kw_only=True)
class Product:
    uuid : UUID  = uuid1
    name: str

@dataclass(kw_only=True)
class Weapon(Product):
    attack: int
    defense: int
    price : int