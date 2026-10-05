import pymysql
from dotenv import load_dotenv
import os

load_dotenv()


class MySQLConnection:

    def __init__(self, db):

        self.connection = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=db,
            cursorclass=pymysql.cursors.DictCursor
        )

    def query_db(self, query, data=None):

        cursor = self.connection.cursor()

        cursor.execute(query, data)

        if query.strip().lower().startswith("select"):

            resultado = cursor.fetchall()

        else:

            self.connection.commit()

            resultado = cursor.lastrowid

        cursor.close()
        self.connection.close()

        return resultado