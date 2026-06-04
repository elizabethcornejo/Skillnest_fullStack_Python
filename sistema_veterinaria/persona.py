from conexion import conexion, cursor

class persona:
    def __init__(self, nombre, email, telefono, rut, comuna, calle, numero_residencia):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.rut = rut
        self.comuna = comuna
        self.calle = calle
        self.numero_residencia = numero_residencia

    def mostrar_datos_personas(self):
        print(f"{self.nombre}")
        print(f"{self.email}")
        print(f"{self.telefono}")
        print(f"{self.rut}")
        print(f"{self.comuna}")
        print(f"{self.calle}")
        print(f"{self.numero_residencia}")

    def actualizar_informacion_persona(self, nuevo_email, nuevo_telefono, nueva_comuna, nueva_calle, nuevo_numero_residencia):
        self.email = nuevo_email
        self.telefono = nuevo_telefono
        self.comuna = nueva_comuna
        self.calle = nueva_calle
        self.numero_residencia = nuevo_numero_residencia

        print("Información actualizada correctamente")

    def guardar(self):

        sql = """
        INSERT INTO duenos
        (nombre_dueno,email,telefono,rut)
        VALUES (%s,%s,%s,%s)
        """

        valores = (
            self.nombre,
            self.email,
            self.telefono,
            self.rut
        )

        cursor.execute(sql, valores)
        conexion.commit()

        print("Dueño registrado")

    @staticmethod
    def listar():

        cursor.execute("""
            SELECT *
            FROM duenos
            WHERE deleted = 0
        """)

        for fila in cursor.fetchall():
            print(fila)

    @staticmethod
    def buscar():

        nombre = input("Nombre dueño: ")

        cursor.execute("""
            SELECT *
            FROM duenos
            WHERE nombre_dueno = %s
        """, (nombre,))

        for fila in cursor.fetchall():
            print(fila)

    @staticmethod
    def eliminar():

        id_dueno = int(input("ID dueño: "))

        cursor.execute("""
            UPDATE duenos
            SET deleted = 1
            WHERE id_dueno = %s
        """, (id_dueno,))

        conexion.commit()

        print("Dueño eliminado")