from config.mysqlconnection import connectToMySQL

class Estudiante:
    @classmethod
    def obtener_todos(cls):
        query = "SELECT * FROM estudiantes;"
        return connectToMySQL('esquema_estudiantes').query_db(query)

    @classmethod
    def actualizar(cls, datos):
        query = """
        UPDATE estudiantes
        SET nombre = %(nombre)s, email = %(email)s
        WHERE id_estudiante = %(id)s;
        """
        return connectToMySQL('esquema_estudiantes').query_db(query, datos)

    @classmethod
    def eliminar(cls, datos):
        query = """
        DELETE FROM estudiantes
        WHERE id_estudiante = %(id)s;
        """
        return connectToMySQL('esquema_estudiantes').query_db(query, datos)