from dataclasses import dataclass
import easygui

class Game():
    pass

class GUI():
    
    def demo(self):
        return easygui.egdemo()

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

if __name__ == "__main__":
    view = GUI()
    view.loginOrRegisterWindow()
    user, password = view.createLoginWindow()
    print()
    register = LoginRegister((user, password))

    logged = register.login()
    if not logged:
        logged = register.create_user()

    game = Game()
    game.start_game(logged.credentials)

    
