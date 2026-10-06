from flask_app.config.mysqlconnection import MySQLConnection


class Comentario:

    @classmethod
    def todos_por_tarea(cls, tarea_id):
        query = """
            SELECT
                comentarios.id,
                comentarios.contenido,
                comentarios.created_at,
                usuarios.nombre,
                usuarios.apellido
            FROM comentarios
            INNER JOIN usuarios
                ON comentarios.usuario_id = usuarios.id
            WHERE comentarios.tarea_id = %(tarea_id)s
            ORDER BY comentarios.created_at DESC
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "tarea_id": tarea_id
            })
            comentarios = cursor.fetchall()

        conn.close()

        return comentarios

    @classmethod
    def crear(cls, data):
        query = """
            INSERT INTO comentarios
            (
                contenido,
                usuario_id,
                tarea_id
            )
            VALUES
            (
                %(contenido)s,
                %(usuario_id)s,
                %(tarea_id)s
            )
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, data)

        conn.commit()
        conn.close()