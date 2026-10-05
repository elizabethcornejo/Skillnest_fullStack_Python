from conexion import Conexion


class Usuario:

    def __init__(self, id=None, usuario="", password="", tipo=None):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo = tipo

    def crear(self):
        conexion = Conexion()
        db = conexion.abrir()
        cursor = db.cursor()

        sql = """
            INSERT INTO usuarios (usuario, password, tipo_usuario)
            VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (self.usuario, self.password, self.tipo))
        db.commit()

        conexion.cerrar()

    @classmethod
    def buscar_por_id(cls, id):
        conexion = Conexion()
        db = conexion.abrir()
        cursor = db.cursor()

        sql = """
            SELECT usuarios.id, usuarios.usuario, usuarios.password,
            tipos_usuario.nombre
            FROM usuarios
            INNER JOIN tipos_usuario
            ON usuarios.tipo_usuario = tipos_usuario.id
            WHERE usuarios.id = %s
        """

        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()

        conexion.cerrar()

        if resultado:
            return resultado

        return None

    @classmethod
    def listar(cls):
        conexion = Conexion()
        db = conexion.abrir()
        cursor = db.cursor()

        sql = """
            SELECT usuarios.id, usuarios.usuario, tipos_usuario.nombre
            FROM usuarios
            INNER JOIN tipos_usuario
            ON usuarios.tipo_usuario = tipos_usuario.id
            ORDER BY usuarios.id
        """

        cursor.execute(sql)
        resultados = cursor.fetchall()

        conexion.cerrar()

        return resultados

    def modificar(self):
        conexion = Conexion()
        db = conexion.abrir()
        cursor = db.cursor()

        sql = """
            UPDATE usuarios
            SET usuario = %s,
                password = %s,
                tipo_usuario = %s
            WHERE id = %s
        """

        cursor.execute(
            sql,
            (self.usuario, self.password, self.tipo, self.id)
        )

        db.commit()
        conexion.cerrar()

    @classmethod
    def eliminar(cls, id):
        conexion = Conexion()
        db = conexion.abrir()
        cursor = db.cursor()

        sql = "DELETE FROM usuarios WHERE id = %s"

        cursor.execute(sql, (id,))
        db.commit()

        conexion.cerrar()

    @classmethod
    def validar_login(cls, usuario, password):
        conexion = Conexion()
        db = conexion.abrir()
        cursor = db.cursor()

        sql = """
            SELECT usuarios.id, usuarios.usuario, usuarios.password,
            usuarios.tipo_usuario, tipos_usuario.nombre
            FROM usuarios
            INNER JOIN tipos_usuario
            ON usuarios.tipo_usuario = tipos_usuario.id
            WHERE usuarios.usuario = %s
            AND usuarios.password = %s
        """

        cursor.execute(sql, (usuario, password))
        resultado = cursor.fetchone()

        conexion.cerrar()

        return resultado