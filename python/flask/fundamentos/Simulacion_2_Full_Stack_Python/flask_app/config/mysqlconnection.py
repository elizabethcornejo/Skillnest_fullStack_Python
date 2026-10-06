import pymysql.cursors

class MySQLConnection:

    @staticmethod
    def get_db():
        return pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="tasktrack",
            cursorclass=pymysql.cursors.DictCursor
        )