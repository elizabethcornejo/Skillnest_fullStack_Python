from config.mysqlconnection import MySQLConnection


class Usuario:

    @classmethod
    def crear(cls, datos):
        conexion = MySQLConnection().get_connection()

        cursor = conexion.cursor()

        query = """
            INSERT INTO usuarios (nombre, apellido, email, password)
            VALUES (%s, %s, %s, %s)
        """

        valores = (
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["password"]
        )

        cursor.execute(query, valores)
        conexion.commit()

        id_usuario = cursor.lastrowid

        cursor.close()
        conexion.close()

        return id_usuario

    @classmethod
    def buscar_por_email(cls, email):
        conexion = MySQLConnection().get_connection()

        cursor = conexion.cursor()

        query = """
            SELECT id, nombre, apellido, email, password
            FROM usuarios
            WHERE email = %s
        """

        cursor.execute(query, (email,))

        usuario = cursor.fetchone()

        cursor.close()
        conexion.close()

        return usuario

    @classmethod
    def buscar_por_id(cls, id_usuario):
        conexion = MySQLConnection().get_connection()

        cursor = conexion.cursor()

        query = """
            SELECT id, nombre, apellido, email
            FROM usuarios
            WHERE id = %s
        """

        cursor.execute(query, (id_usuario,))

        usuario = cursor.fetchone()

        cursor.close()
        conexion.close()

        return usuario