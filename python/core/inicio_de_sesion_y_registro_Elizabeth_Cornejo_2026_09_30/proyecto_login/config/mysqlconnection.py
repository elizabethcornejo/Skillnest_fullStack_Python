import pymysql

class MySQLConnection:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="proyecto_login"
        )

    def get_connection(self):
        return self.connection