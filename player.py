class Player:
    name : str
    attack: int
    defense: int
    money: int

    def __init__(self, name, attack=1, defense=1, money=10) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense
        self.money = money

    def getDamage(self) -> int:
        return self.attack

    