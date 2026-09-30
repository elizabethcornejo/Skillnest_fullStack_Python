from flask_app.config.mysqlconnection import connectToMySQL


class Usuario:

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = """
            SELECT *
            FROM usuarios
            ORDER BY nombre, apellido
        """

        resultados = connectToMySQL(
            "esquema_seguidores"
        ).query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios

    @classmethod
    def get_by_id(cls, id):
        query = """
            SELECT *
            FROM usuarios
            WHERE id = %(id)s
        """

        data = {
            "id": id
        }

        resultado = connectToMySQL(
            "esquema_seguidores"
        ).query_db(query, data)

        if resultado:
            return cls(resultado[0])

        return None

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios
            (nombre, apellido, email)
            VALUES
            (%(nombre)s, %(apellido)s, %(email)s)
        """

        return connectToMySQL(
            "esquema_seguidores"
        ).query_db(query, data)