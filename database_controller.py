import sqlite3
import logging

def checkDBErrors(func):
    def wrapper():
        try:
            func()
        except Exception as err:
            logging.getLogger("DatabaseController").exception(msg="Erro na execução do banco de dados", exc_info=err)
    return wrapper
    


class DatabaseController:

    @checkDBErrors
    def connect(self,):
        return sqlite3.connect("joguim.db").cursor()
