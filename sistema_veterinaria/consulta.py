from conexion import conexion, cursor

class consulta:

    def __init__(self, motivo, anamnesis, tipo_consulta, mascota):
        self.motivo = motivo
        self.anamnesis = anamnesis
        self.tipo_consulta = tipo_consulta
        self.mascota = mascota

    def mostrar_datos_cosulta(self):
        print(f"{self.motivo}")
        print(f"{self.anamnesis}")
        print(f"{self.tipo_consulta}")
        print(f"{self.mascota}")

    def actualizar_anamnesis(self, nueva_anamnesis):
        self.anamnesis = nueva_anamnesis
        print("Información actualizada correctamente")

    def guardar(self):

        sql = """
        INSERT INTO consultas
        (motivo_consulta, anamnesis, id_tipo_consulta, id_mascota)
        VALUES (%s,%s,%s,%s)
        """

        valores = (
            self.motivo,
            self.anamnesis,
            self.tipo_consulta,
            self.mascota
        )

        cursor.execute(sql, valores)
        conexion.commit()

        print("Consulta registrada")

    @staticmethod
    def listar():

        cursor.execute("""
            SELECT *
            FROM consultas
            WHERE deleted = 0
        """)

        for fila in cursor.fetchall():
            print(fila)

    @staticmethod
    def buscar():

        id_consulta = int(input("ID consulta: "))

        cursor.execute("""
            SELECT *
            FROM consultas
            WHERE id_consulta = %s
        """, (id_consulta,))

        for fila in cursor.fetchall():
            print(fila)

    @staticmethod
    def eliminar():

        id_consulta = int(input("ID consulta: "))

        cursor.execute("""
            UPDATE consultas
            SET deleted = 1
            WHERE id_consulta = %s
        """, (id_consulta,))

        conexion.commit()

        print("Consulta eliminada")
