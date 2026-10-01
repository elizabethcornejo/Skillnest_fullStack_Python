import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        if query.lower().startswith("select"):
            return cursor.fetchall()
        elif query.lower().startswith("insert"):
            self.connection.commit()
            return cursor.lastrowid
        else:
            self.connection.commit()
            return cursor.rowcount

def connectToMySQL(db):
    return MySQLConnection(db)