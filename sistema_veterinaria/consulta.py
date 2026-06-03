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

        print(f"Información actualizada correctamente: ")
