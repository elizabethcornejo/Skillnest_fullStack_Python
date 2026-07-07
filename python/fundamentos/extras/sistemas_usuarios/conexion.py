import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self, host, user, password, db, conexio,):
        self.host = "localhost"
        self.user = "root"       
        self.password = ""        
        self.db = "usuarios_db"
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db
            )
            return self.conexion
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None

    def cerrar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()