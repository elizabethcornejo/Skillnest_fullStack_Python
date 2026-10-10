
import pymysql
import pymysql.cursors

def connectToMySQL(base_datos):
    class MySQLConnection:
        def __init__(self, base_datos):
            self.base_datos = base_datos

        def query_db(self, query, datos=None):
            conexion = pymysql.connect(
                host="localhost",
                user="root",
                password="1234",
                database=self.base_datos,
                cursorclass=pymysql.cursors.DictCursor
            )

            resultado = None

            try:
                with conexion.cursor() as cursor:
                    cursor.execute(query, datos or ())

                    if query.strip().lower().startswith("select"):
                        resultado = cursor.fetchall()
                    else:
                        conexion.commit()
                        resultado = cursor.lastrowid

            finally:
                conexion.close()

            return resultado

    return MySQLConnection(base_datos)
