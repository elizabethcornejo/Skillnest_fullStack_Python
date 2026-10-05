from flask_app.config.mysqlconnection import MySQLConnection



class Libro:



    @classmethod
    def crear(cls,data):


        query = """

        INSERT INTO libros

        (
        titulo,
        autor,
        genero,
        fecha_publicacion,
        descripcion,
        usuario_id
        )


        VALUES

        (
        %(titulo)s,
        %(autor)s,
        %(genero)s,
        %(fecha_publicacion)s,
        %(descripcion)s,
        %(usuario_id)s
        )

        """

        return MySQLConnection("bookhub").query_db(query,data)




    @classmethod
    def mis_libros(cls,usuario_id):


        query = """

        SELECT libros.*,

        (
        SELECT COUNT(*)

        FROM favoritos

        WHERE favoritos.libro_id = libros.id

        ) AS favoritos


        FROM libros


        WHERE usuario_id = %(usuario_id)s


        ORDER BY id DESC


        """

        data={

            "usuario_id":usuario_id

        }


        return MySQLConnection("bookhub").query_db(query,data)





    @classmethod
    def todos(cls):


        query = """

        SELECT libros.*,

        CONCAT(
        usuarios.nombre,
        ' ',
        usuarios.apellido
        )

        AS publicado_por,


        (

        SELECT COUNT(*)

        FROM favoritos

        WHERE favoritos.libro_id = libros.id

        )

        AS favoritos


        FROM libros


        INNER JOIN usuarios

        ON libros.usuario_id = usuarios.id


        ORDER BY libros.id DESC


        """

        return MySQLConnection("bookhub").query_db(query)





    @classmethod
    def buscar_por_id(cls,id):


        query = """

        SELECT libros.*,

        CONCAT(
        usuarios.nombre,
        ' ',
        usuarios.apellido
        )

        AS publicado_por


        FROM libros


        INNER JOIN usuarios

        ON libros.usuario_id = usuarios.id


        WHERE libros.id = %(id)s


        """


        data={

            "id":id

        }


        resultado = MySQLConnection("bookhub").query_db(query,data)



        if resultado:

            return resultado[0]


        return None





    @classmethod
    def actualizar(cls,data):


        query = """

        UPDATE libros


        SET

        titulo=%(titulo)s,

        autor=%(autor)s,

        genero=%(genero)s,

        fecha_publicacion=%(fecha_publicacion)s,

        descripcion=%(descripcion)s


        WHERE id=%(id)s

        AND usuario_id=%(usuario_id)s


        """

        return MySQLConnection("bookhub").query_db(query,data)





    @classmethod
    def eliminar(cls,id,usuario_id):


        query = """

        DELETE FROM libros

        WHERE id=%(id)s

        AND usuario_id=%(usuario_id)s

        """

        data={

            "id":id,

            "usuario_id":usuario_id

        }


        return MySQLConnection("bookhub").query_db(query,data)