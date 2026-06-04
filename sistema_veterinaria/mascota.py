from conexion import conexion, cursor

class mascota:

    def __init__(self, nombre, especie, raza, sexo, fecha_nac, peso, dueno):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.sexo = sexo
        self.fecha_nac = fecha_nac
        self.peso = peso
        self.dueno = dueno

    def mostrar_datos_mascotas(self):
        print(f"{self.nombre}")
        print(f"{self.especie}")
        print(f"{self.raza}")
        print(f"{self.sexo}")
        print(f"{self.fecha_nac}")
        print(f"{self.peso}")
        print(f"{self.dueno}")

    def actualizar_informacion_mascota(self, nuevo_peso):
        self.peso = nuevo_peso
        print("Información actualizada correctamente")

    def guardar(self):

        sql = """
        INSERT INTO mascotas
        (nombre_mascota,sexo_mascota,fecha_nac,peso,id_dueno,id_especie,id_raza)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        valores = (
            self.nombre,
            self.sexo,
            self.fecha_nac,
            self.peso,
            self.dueno,
            self.especie,
            self.raza
        )

        cursor.execute(sql, valores)
        conexion.commit()

        print("Mascota registrada")

    @staticmethod
    def listar():

        cursor.execute("""
            SELECT *
            FROM mascotas
            WHERE deleted = 0
        """)

        for fila in cursor.fetchall():
            print(fila)

    @staticmethod
    def buscar():

        nombre = input("Nombre mascota: ")

        cursor.execute("""
            SELECT *
            FROM mascotas
            WHERE nombre_mascota = %s
        """, (nombre,))

        for fila in cursor.fetchall():
            print(fila)

    @staticmethod
    def eliminar():

        id_mascota = int(input("ID mascota: "))

        cursor.execute("""
            UPDATE mascotas
            SET deleted = 1
            WHERE id_mascota = %s
        """, (id_mascota,))

        conexion.commit()

        print("Mascota eliminada")