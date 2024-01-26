import sqlite3

class DataBaseController:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def get_account(self, id):
        query = """
        SELECT money FROM Player_money
        WHERE ID = ?
        """
        return int(self.cur.execute(query, (str(id), )).fetchone()[0])

    def add_money(self, id, money):
        query = """UPDATE  Player_money  
                SET money =  ?
                WHERE ID = ?"""
        self.cur.execute(query, (money, id))
        self.con.commit()