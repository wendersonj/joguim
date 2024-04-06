import logging

from database_controller import DatabaseController, checkDBErrors


class PlayerController:
    def __init__(self,):
        self.db = DatabaseController()

    @checkDBErrors
    def create_user(self,username):
        cur = self.db.connect()
        #precisa fazer o escape para evitar sql inject
        res = cur.execute("Select * from players where username=username")
        if res.fetchone():
            return (False, "username já existe")
        