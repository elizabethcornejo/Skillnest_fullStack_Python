from flask_app.config.mysqlconnection import MySQLConnection



class Favorito:



    @classmethod
    def agregar(cls,data):


        query = """

        INSERT INTO favoritos

        (
        usuario_id,
        libro_id
        )


        VALUES

        (
        %(usuario_id)s,
        %(libro_id)s
        )


        """

        return MySQLConnection("bookhub").query_db(query,data)





    @classmethod
    def eliminar(cls,data):


        query = """

        DELETE FROM favoritos


        WHERE usuario_id=%(usuario_id)s

        AND libro_id=%(libro_id)s


        """


        return MySQLConnection("bookhub").query_db(query,data)





    @classmethod
    def existe(cls,data):


        query = """

        SELECT *

        FROM favoritos


        WHERE usuario_id=%(usuario_id)s

        AND libro_id=%(libro_id)s


        """

        resultado = MySQLConnection("bookhub").query_db(query,data)



        if resultado:

            return True


        return False






    @classmethod
    def mis_favoritos(cls,usuario_id):


        query = """

        SELECT libros.*


        FROM favoritos


        INNER JOIN libros

        ON favoritos.libro_id = libros.id


        WHERE favoritos.usuario_id=%(usuario_id)s


        """


        data={

            "usuario_id":usuario_id

        }


        return MySQLConnection("bookhub").query_db(query,data)