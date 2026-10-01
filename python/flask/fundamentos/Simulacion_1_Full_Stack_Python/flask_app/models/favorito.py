from flask_app.config.mysqlconnection import MySQLConnection


class Favorito:

    def __init__(self, data):
        self.id = data.get("id")
        self.usuario_id = data.get("usuario_id")
        self.libro_id = data.get("libro_id")

    @classmethod
    def agregar(cls, data):
        query = """
            INSERT INTO favoritos (usuario_id, libro_id)
            VALUES (%(usuario_id)s, %(libro_id)s)
        """

        return MySQLConnection("bookhub").query_db(query, data)

    @classmethod
    def eliminar(cls, data):
        query = """
            DELETE FROM favoritos
            WHERE usuario_id = %(usuario_id)s
            AND libro_id = %(libro_id)s
        """

        return MySQLConnection("bookhub").query_db(query, data)

    @classmethod
    def obtener_favorito(cls, data):
        query = """
            SELECT *
            FROM favoritos
            WHERE usuario_id = %(usuario_id)s
            AND libro_id = %(libro_id)s
        """

        resultado = MySQLConnection("bookhub").query_db(query, data)

        if resultado:
            return cls(resultado[0])

        return None