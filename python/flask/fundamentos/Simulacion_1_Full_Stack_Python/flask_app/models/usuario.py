from flask_app.config.mysqlconnection import MySQLConnection


class Usuario:

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]

    @classmethod
    def crear(cls, data):

        query = """
        INSERT INTO usuarios
        (
            nombre,
            apellido,
            email,
            password
        )
        VALUES
        (
            %(nombre)s,
            %(apellido)s,
            %(email)s,
            %(password)s
        )
        """

        return MySQLConnection("bookhub").query_db(query, data)

    @classmethod
    def buscar_por_email(cls, email):

        query = """
        SELECT *
        FROM usuarios
        WHERE email = %(email)s
        """

        data = {
            "email": email
        }

        resultado = MySQLConnection("bookhub").query_db(query, data)

        if resultado:
            return cls(resultado[0])

        return None

    @classmethod
    def buscar_por_id(cls, id):

        query = """
        SELECT *
        FROM usuarios
        WHERE id = %(id)s
        """

        data = {
            "id": id
        }

        resultado = MySQLConnection("bookhub").query_db(query, data)

        if resultado:
            return cls(resultado[0])

        return None