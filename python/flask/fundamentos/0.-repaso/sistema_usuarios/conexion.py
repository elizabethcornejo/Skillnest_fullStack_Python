import pymysql


class Conexion:

    def __init__(self):
        self.conexion = None

    def abrir(self):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="usuarios_db"
        )
        return self.conexion

    def obtener(self):
        return self.conexion

    def cerrar(self):
        if self.conexion:
            self.conexion.close()
            self.conexion = None