from dataclasses import dataclass
from typing import List

from weapon import Product, Weapon


@dataclass
class NPC:
    name : str
    attack: int
    defense: int
    money: int
    life : int
    inventory : List
    
    isAlive: bool = True
    

class Player(NPC):
    
    def __init__(self, name) -> None:
        super()
        self.name = name
        self.attack = 1
        self.defense = 1
        self.money = 10
        self.isAlive = True
        self.life = 100
        self.vigor = 100
        self.weapon : Weapon = None
        self.shield = None
        self.inventory : List[Product] = []

    def getInfos(self) -> dict :
        return self.__dict__

    def getMoney(self):
        return self.money


    @property
    def getDamageValue(self) -> int:
        weapon_damage = 0
        if self.weapon:
            weapon_damage = self.weapon.attack
        return self.attack + weapon_damage

        @property
        def getDefense(self) -> int:
            return self.defense

    def goToHospital(self,):
        if self.isAlive:
            pass

    def die(self):
        self.isAlive = False
        self.life = 0

    def takeDamage(self, damage):
        if not damage:
            raise ValueError("O ataque não pode ser nulo")
        
        if damage > self.life:
            self.die()
            self.goToHospital()
        else:
            self.life -= damage

        return self.isAlive

    def takePercentageDamage(self,percentage=0):
        if 0:
            pass
        return self.isAlive 
    
    def getItem(self, name:str):
        for item in self.inventory:
            if item.name == name:
                return item

    def changeWeapon(self, weapon):
        self.inventory.remove(weapon)
        self.weapon = weapon

    def addItem(self, item):
        self.inventory.append(item)