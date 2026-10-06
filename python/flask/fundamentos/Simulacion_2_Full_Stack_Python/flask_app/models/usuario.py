from flask_app.config.mysqlconnection import MySQLConnection


class Usuario:

    @classmethod
    def crear(cls, data):
        query = """
            INSERT INTO usuarios
            (nombre, apellido, email, password)
            VALUES
            (%(nombre)s, %(apellido)s, %(email)s, %(password)s)
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, data)

        conn.commit()
        conn.close()

    @classmethod
    def obtener_por_email(cls, email):
        query = """
            SELECT *
            FROM usuarios
            WHERE email = %(email)s
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "email": email
            })

            usuario = cursor.fetchone()

        conn.close()

        return usuario

    @classmethod
    def obtener(cls, id):
        query = """
            SELECT *
            FROM usuarios
            WHERE id = %(id)s
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "id": id
            })

            usuario = cursor.fetchone()

        conn.close()

        return usuario

    @classmethod
    def estadisticas(cls, id):
        query = """
            SELECT
                COUNT(tareas.id) AS total,
                COALESCE(SUM(tareas.estado = 'Pendiente'), 0) AS pendientes,
                COALESCE(SUM(tareas.estado = 'En progreso'), 0) AS progreso,
                COALESCE(SUM(tareas.estado = 'Completada'), 0) AS completadas
            FROM tareas
            WHERE tareas.usuario_id = %(id)s
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "id": id
            })

            estadisticas = cursor.fetchone()

        conn.close()

        if estadisticas is None:
            estadisticas = {
                "total": 0,
                "pendientes": 0,
                "progreso": 0,
                "completadas": 0
            }

        return estadisticas

    @classmethod
    def cantidad_categorias(cls, id):
        query = """
            SELECT COUNT(*) AS total
            FROM categorias
            WHERE usuario_id = %(id)s
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "id": id
            })

            resultado = cursor.fetchone()

        conn.close()

        if resultado is None:
            resultado = {
                "total": 0
            }

        return resultado