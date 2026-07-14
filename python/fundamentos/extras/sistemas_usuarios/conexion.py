import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        # Almacenamos los datos técnicos en las propiedades internas del objeto
        self.host = "localhost"
        self.user = "root"
        self.password = "1234"      # Modifica este valor con tu contraseña de MySQL
        self.db = "usuarios_db"
        self.conexion = None

    def conectar(self):
        """Genera y retorna un puente de comunicación activo hacia la base de datos."""
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db
            )
            return self.conexion
        except Error as e:
            print(f" Error crítico en el módulo de conexión a MySQL: {e}")
            return None

    def cerrar(self):
        """Clausura el estado de comunicación si la conexión se mantiene levantada."""
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()