from dataclasses import dataclass
from datetime import datetime
from typing import List

from player import NPC, Player
from weapon import Product, Weapon

class Game():
    pass

class GUI():

    def window():
        layout = [  [sg.Text("What's your name?")],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

        # Create the Window
        window = sg.Window('Hello Example', layout)

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()

            # if user closes window or clicks cancel
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            print('Hello', values[0], '!')

        window.close()
    
    def loginOrRegisterWindow(self):
        LOGIN = "LOGIN"
        REGISTER = "CADASTRAR"
        choice = easygui.indexbox(title="Bem-vindo", msg="Escolha se fará um novo cadastro ou login", choices=[LOGIN, REGISTER])
        if choice == LOGIN:
            self.createLoginWindow()
        else:
            self.createRegisterWindow()

    def createLoginWindow(self,):
        return easygui.multpasswordbox(title="Login", msg="Faça o login", fields=["Usuário", "Senha"], )

    def createRegisterWindow(self,):
        return easygui.multpasswordbox(title="Cadastro", msg="Faça o seu cadastro", fields=["Usuário", "Senha"], )


@dataclass
class User:
    username: str
    password: str

    def getCredentials(self,):
        return (self.username, self.password)


class LoginRegister:
    def login():
        return User()
        

    def create_user():
        return User()

@dataclass
class Message:
    value:str
    date_time : datetime = datetime.now()

class Battle:
    def playerAttackNPC(self, playerOfender:Player, defender:NPC):
        realDamage = playerOfender.getDamageValue - defender.defense
        print(realDamage)
        if realDamage == 0:
            return Message("Vocês ficaram se encarando, porque ninguém conseguiu bater em ninguém")
        elif realDamage < 0:
            playerOfender.takeDamage(abs(realDamage)) #*(-1) para trocar o sinal
            return Message(value="Tentou bater e acabou apanhando kkkk")
        else:
            #roubou dinheiro e produtos
            return Message(f"Você deu um pau em: {defender.name}. Causou {realDamage} de dano")

    def playerAttackPlayer(self, ofender:Player, defender:Player):
        #ofenderDamage = ofender.getDamageValue()
        #   #defender.takePercentageDamage(percentage=100)
        realDamage = ofender.getDamageValue - defender.getDefense
        print(realDamage)
        if realDamage == 0:
            return Message("Vocês ficaram se encarando, porque ninguém conseguiu bater em ninguém")
        elif realDamage < 0:
            ofender.takeDamage(abs(realDamage)) #*(-1) para trocar o sinal
            return Message(value="Tentou bater e acabou apanhando kkkk")
        else:
            defender.takeDamage(realDamage)
            return Message(f"Você deu um pau em: {defender.name}. Causou {realDamage} de dano")
        

def old():
    view = GUI()
    view.window()
    view.loginOrRegisterWindow()
    user, password = view.createLoginWindow()
    print()
    register = LoginRegister((user, password))

    logged = register.login()
    if not logged:
        logged = register.create_user()

    game = Game()
    game.start_game(logged.credentials)


class Shop:
    def __init__(self, products=None) -> None:
        self.products : List[Product] = products if not None else []

    def addProduct(self, product: Product):
        self.products.append(product)

    def getInvetory(self,):
        return self.products
    
    def findItem(self, name) -> Product:
        for item in self.products:
            if item.name == name:
                return item

    def buyProduct(self,buyer: Player, product_name: str):
        product = self.findItem(product_name)
        if buyer.getMoney() < product.price:
            return Message("Saldo insuficiente")
        
        p1.addItem(product)
                

if __name__ == "__main__":
    npcs = [NPC(name="Velhinha", attack=1, defense=1, money=1, life=2, inventory=None)]
    shop1 = Shop(products=[Weapon(name="faca", attack=1,defense=0, price=10)])
    p1 = Player(name="maratte")
    p2 = Player(name="zeca")
    
    shop1.buyProduct(p1, "faca")

    p1.changeWeapon(p1.getItem("faca"))

    result = Battle().playerAttackPlayer(p1, p2)
    print(result)
    print(p1.getInfos())
    print(p2.getInfos())

    result = Battle().playerAttackNPC(p1, npcs[0])
    print(result)
    print(p1.getInfos())