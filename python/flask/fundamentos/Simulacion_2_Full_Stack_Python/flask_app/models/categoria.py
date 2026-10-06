from flask_app.config.mysqlconnection import MySQLConnection


class Categoria:

    @classmethod
    def todas(cls, usuario_id):

        query = """
            SELECT
                categorias.id,
                categorias.nombre,
                COUNT(tareas.id) AS cantidad_tareas
            FROM categorias
            LEFT JOIN tareas
                ON tareas.categoria_id = categorias.id
            WHERE categorias.usuario_id = %(usuario_id)s
            GROUP BY categorias.id, categorias.nombre
            ORDER BY categorias.nombre
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "usuario_id": usuario_id
            })

            categorias = cursor.fetchall()

        conn.close()

        return categorias

    @classmethod
    def crear(cls, data):

        query = """
            INSERT INTO categorias
            (nombre, usuario_id)
            VALUES
            (%(nombre)s, %(usuario_id)s)
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, data)

        conn.commit()
        conn.close()

    @classmethod
    def obtener(cls, id, usuario_id):

        query = """
            SELECT *
            FROM categorias
            WHERE id = %(id)s
            AND usuario_id = %(usuario_id)s
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "id": id,
                "usuario_id": usuario_id
            })

            categoria = cursor.fetchone()

        conn.close()

        return categoria

    @classmethod
    def actualizar(cls, data):

        query = """
            UPDATE categorias
            SET nombre = %(nombre)s
            WHERE id = %(id)s
            AND usuario_id = %(usuario_id)s
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, data)

        conn.commit()
        conn.close()

    @classmethod
    def eliminar(cls, id, usuario_id):

        query = """
            DELETE FROM categorias
            WHERE id = %(id)s
            AND usuario_id = %(usuario_id)s
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "id": id,
                "usuario_id": usuario_id
            })

        conn.commit()
        conn.close()