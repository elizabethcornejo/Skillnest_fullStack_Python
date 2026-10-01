from flask_app.config.mysqlconnection import MySQLConnection

class Libro:

    @classmethod
    def crear(cls, data):
        query = """
        INSERT INTO libros
        (titulo, autor, genero, fecha_publicacion, descripcion, usuario_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        conexion = MySQLConnection.connectToMySQL()
        cursor = conexion.cursor()

        cursor.execute(query, (
            data["titulo"],
            data["autor"],
            data["genero"],
            data["fecha_publicacion"],
            data["descripcion"],
            data["usuario_id"]
        ))

        nuevo_id = cursor.lastrowid

        cursor.close()
        conexion.close()

        return nuevo_id

    @classmethod
    def todos(cls):
        query = """
        SELECT libros.*,
        CONCAT(usuarios.nombre, ' ', usuarios.apellido) AS publicado_por,
        (
            SELECT COUNT(*)
            FROM favoritos
            WHERE favoritos.libro_id = libros.id
        ) AS favoritos
        FROM libros
        JOIN usuarios
        ON libros.usuario_id = usuarios.id
        ORDER BY libros.id DESC
        """

        conexion = MySQLConnection.connectToMySQL()
        cursor = conexion.cursor()

        cursor.execute(query)

        libros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return libros

    @classmethod
    def mis_libros(cls, usuario_id):
        query = """
        SELECT libros.*,
        (
            SELECT COUNT(*)
            FROM favoritos
            WHERE favoritos.libro_id = libros.id
        ) AS favoritos
        FROM libros
        WHERE usuario_id = %s
        ORDER BY id DESC
        """

        conexion = MySQLConnection.connectToMySQL()
        cursor = conexion.cursor()

        cursor.execute(query, (usuario_id,))

        libros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return libros

    @classmethod
    def buscar_por_id(cls, libro_id):
        query = """
        SELECT libros.*,
        CONCAT(usuarios.nombre, ' ', usuarios.apellido) AS publicado_por,
        (
            SELECT COUNT(*)
            FROM favoritos
            WHERE favoritos.libro_id = libros.id
        ) AS favoritos
        FROM libros
        JOIN usuarios
        ON libros.usuario_id = usuarios.id
        WHERE libros.id = %s
        """

        conexion = MySQLConnection.connectToMySQL()
        cursor = conexion.cursor()

        cursor.execute(query, (libro_id,))

        libro = cursor.fetchone()

        cursor.close()
        conexion.close()

        return libro

    @classmethod
    def actualizar(cls, data):
        query = """
        UPDATE libros
        SET titulo = %s,
            autor = %s,
            genero = %s,
            fecha_publicacion = %s,
            descripcion = %s
        WHERE id = %s
        AND usuario_id = %s
        """

        conexion = MySQLConnection.connectToMySQL()
        cursor = conexion.cursor()

        cursor.execute(query, (
            data["titulo"],
            data["autor"],
            data["genero"],
            data["fecha_publicacion"],
            data["descripcion"],
            data["id"],
            data["usuario_id"]
        ))

        resultado = cursor.rowcount

        cursor.close()
        conexion.close()

        return resultado

    @classmethod
    def eliminar(cls, libro_id, usuario_id):
        query = """
        DELETE FROM libros
        WHERE id = %s
        AND usuario_id = %s
        """

        conexion = MySQLConnection.connectToMySQL()
        cursor = conexion.cursor()

        cursor.execute(query, (libro_id, usuario_id))

        resultado = cursor.rowcount

        cursor.close()
        conexion.close()

        return resultado