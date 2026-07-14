from conexion import Conexion
import mysql.connector

class Usuario:
    # Constructor explícito: Almacena en orden cada parámetro dentro del self
    def __init__(self, id=None, usuario=None, password=None, tipo=None):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo = tipo

    def validar_inicio_sesion(self, txt_usuario, txt_password):
        """Autentica las credenciales ingresadas contra los registros de la base de datos."""
        obj_conexion = Conexion()
        db = obj_conexion.conectar()
        if not db: 
            return None

        cursor = db.cursor(dictionary=True)
        try:
            sql = """
                SELECT u.id, u.usuario, u.password, r.nombre as tipo 
                FROM usuarios u
                INNER JOIN roles r ON u.tipo_usuario_id = r.id
                WHERE u.usuario = %s AND u.password = %s
            """
            cursor.execute(sql, (txt_usuario, txt_password))
            resultado = cursor.fetchone()
            
            if resultado:
                # Instanciamos la clase pasándole los datos al listado del constructor
                return Usuario(
                    id=resultado['id'], 
                    usuario=resultado['usuario'], 
                    password=resultado['password'], 
                    tipo=resultado['tipo']
                )
            return None
        finally:
            cursor.close()
            obj_conexion.cerrar()

    def existe_usuario(self, txt_usuario):
        """Desafío Extra: Verifica la disponibilidad de un nombre de usuario."""
        obj_conexion = Conexion()
        db = obj_conexion.conectar()
        cursor = db.cursor(dictionary=True)
        try:
            sql = "SELECT id FROM usuarios WHERE usuario = %s"
            cursor.execute(sql, (txt_usuario,))
            return cursor.fetchone() is not None
        finally:
            cursor.close()
            obj_conexion.cerrar()

    def crear_usuario(self, txt_usuario, txt_password, tipo_str):
        """Inserta un nuevo usuario asociándolo a su correspondiente ID de rol."""
        if self.existe_usuario(txt_usuario):
            print(" Error: El nombre de usuario ya se encuentra registrado.")
            return False

        obj_conexion = Conexion()
        db = obj_conexion.conectar()
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT id FROM roles WHERE nombre = %s", (tipo_str,))
            rol = cursor.fetchone()
            if not rol: 
                return False

            sql = "INSERT INTO usuarios (usuario, password, tipo_usuario_id) VALUES (%s, %s, %s)"
            cursor.execute(sql, (txt_usuario, txt_password, rol['id']))
            db.commit()
            return True
        except mysql.connector.Error as e:
            print(f" Error al intentar registrar en la base de datos: {e}")
            return False
        finally:
            cursor.close()
            obj_conexion.cerrar()

    def obtener_listado_usuarios(self):
        """Trae todos los registros de la base de datos de forma relacional."""
        obj_conexion = Conexion()
        db = obj_conexion.conectar()
        cursor = db.cursor(dictionary=True)
        try:
            sql = """
                SELECT u.id, u.usuario, r.nombre as tipo 
                FROM usuarios u
                INNER JOIN roles r ON u.tipo_usuario_id = r.id
            """
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close()
            obj_conexion.cerrar()

    def buscar_por_id(self, id_usuario):
        """Busca y extrae la información completa de una fila por su ID único."""
        obj_conexion = Conexion()
        db = obj_conexion.conectar()
        cursor = db.cursor(dictionary=True)
        try:
            sql = """
                SELECT u.id, u.usuario, r.nombre as tipo 
                FROM usuarios u
                INNER JOIN roles r ON u.tipo_usuario_id = r.id
                WHERE u.id = %s
            """
            cursor.execute(sql, (id_usuario,))
            return cursor.fetchone()
        finally:
            cursor.close()
            obj_conexion.cerrar()

    def modificar_usuario(self, id_usuario, nuevo_user, nueva_pass, nuevo_tipo):
        """Actualiza todas las columnas de un registro específico identificándolo por su ID."""
        obj_conexion = Conexion()
        db = obj_conexion.conectar()
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT id FROM roles WHERE nombre = %s", (nuevo_tipo,))
            rol = cursor.fetchone()
            if not rol: 
                return False

            sql = "UPDATE usuarios SET usuario = %s, password = %s, tipo_usuario_id = %s WHERE id = %s"
            cursor.execute(sql, (nuevo_user, nueva_pass, rol['id'], id_usuario))
            db.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            obj_conexion.cerrar()

    def eliminar_usuario(self, id_usuario):
        """Borra la fila seleccionada de la tabla usuarios de forma definitiva."""
        obj_conexion = Conexion()
        db = obj_conexion.conectar()
        cursor = db.cursor(dictionary=True)
        try:
            sql = "DELETE FROM usuarios WHERE id = %s"
            cursor.execute(sql, (id_usuario,))
            db.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            obj_conexion.cerrar()