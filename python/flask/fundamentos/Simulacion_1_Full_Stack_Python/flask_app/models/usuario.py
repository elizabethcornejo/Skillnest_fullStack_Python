from flask_app.config.mysqlconnection import MySQLConnection

class Usuario:

    @classmethod
    def crear(cls, data):
        query = """
        INSERT INTO usuarios
        (nombre, apellido, email, password)
        VALUES (%s, %s, %s, %s)
        """

        conexion = MySQLConnection.connectToMySQL()
        cursor = conexion.cursor()

        cursor.execute(query, (
            data["nombre"],
            data["apellido"],
            data["email"],
            data["password"]
        ))

        nuevo_id = cursor.lastrowid

        cursor.close()
        conexion.close()

        return nuevo_id

    @classmethod
    def buscar_por_email(cls, email):
        query = """
        SELECT *
        FROM usuarios
        WHERE email = %s
        """

        conexion = MySQLConnection.connectToMySQL()
        cursor = conexion.cursor()

        cursor.execute(query, (email,))

        usuario = cursor.fetchone()

        cursor.close()
        conexion.close()

        return usuario

    @classmethod
    def buscar_por_id(cls, usuario_id):
        query = """
        SELECT *
        FROM usuarios
        WHERE id = %s
        """

        conexion = MySQLConnection.connectToMySQL()
        cursor = conexion.cursor()

        cursor.execute(query, (usuario_id,))

        usuario = cursor.fetchone()

        cursor.close()
        conexion.close()

        return usuario