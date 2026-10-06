from flask_app.config.mysqlconnection import MySQLConnection


class Tarea:

    @classmethod
    def todas_por_usuario(cls, usuario_id):
        query = """
            SELECT
                tareas.id,
                tareas.titulo,
                tareas.categoria_id,
                categorias.nombre AS categoria,
                tareas.prioridad,
                tareas.fecha_limite,
                tareas.estado,
                tareas.descripcion
            FROM tareas
            INNER JOIN categorias
                ON tareas.categoria_id = categorias.id
            WHERE tareas.usuario_id = %(usuario_id)s
            ORDER BY tareas.fecha_limite ASC
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "usuario_id": usuario_id
            })
            tareas = cursor.fetchall()

        conn.close()

        return tareas

    @classmethod
    def crear(cls, data):
        query = """
            INSERT INTO tareas
            (
                titulo,
                categoria_id,
                prioridad,
                fecha_limite,
                estado,
                descripcion,
                usuario_id
            )
            VALUES
            (
                %(titulo)s,
                %(categoria_id)s,
                %(prioridad)s,
                %(fecha_limite)s,
                %(estado)s,
                %(descripcion)s,
                %(usuario_id)s
            )
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, data)

        conn.commit()
        conn.close()

    @classmethod
    def obtener(cls, id, usuario_id):
        query = """
            SELECT
                tareas.id,
                tareas.titulo,
                tareas.categoria_id,
                categorias.nombre AS categoria,
                tareas.prioridad,
                tareas.fecha_limite,
                tareas.estado,
                tareas.descripcion,
                tareas.usuario_id
            FROM tareas
            INNER JOIN categorias
                ON tareas.categoria_id = categorias.id
            WHERE tareas.id = %(id)s
            AND tareas.usuario_id = %(usuario_id)s
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "id": id,
                "usuario_id": usuario_id
            })
            tarea = cursor.fetchone()

        conn.close()

        return tarea

    @classmethod
    def actualizar(cls, data):
        query = """
            UPDATE tareas
            SET
                titulo = %(titulo)s,
                categoria_id = %(categoria_id)s,
                prioridad = %(prioridad)s,
                fecha_limite = %(fecha_limite)s,
                estado = %(estado)s,
                descripcion = %(descripcion)s
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
            DELETE FROM tareas
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

    @classmethod
    def cambiar_estado(cls, id, estado, usuario_id):
        query = """
            UPDATE tareas
            SET estado = %(estado)s
            WHERE id = %(id)s
            AND usuario_id = %(usuario_id)s
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, {
                "id": id,
                "estado": estado,
                "usuario_id": usuario_id
            })

        conn.commit()
        conn.close()

    @classmethod
    def buscar(cls, usuario_id, texto="", estado=""):
        query = """
            SELECT
                tareas.id,
                tareas.titulo,
                tareas.categoria_id,
                categorias.nombre AS categoria,
                tareas.prioridad,
                tareas.fecha_limite,
                tareas.estado,
                tareas.descripcion
            FROM tareas
            INNER JOIN categorias
                ON tareas.categoria_id = categorias.id
            WHERE tareas.usuario_id = %(usuario_id)s
        """

        parametros = {
            "usuario_id": usuario_id
        }

        if texto:
            query += """
                AND tareas.titulo LIKE %(texto)s
            """
            parametros["texto"] = "%" + texto + "%"

        if estado:
            query += """
                AND tareas.estado = %(estado)s
            """
            parametros["estado"] = estado

        query += """
            ORDER BY tareas.fecha_limite ASC
        """

        conn = MySQLConnection.get_db()

        with conn.cursor() as cursor:
            cursor.execute(query, parametros)
            tareas = cursor.fetchall()

        conn.close()

        return tareas