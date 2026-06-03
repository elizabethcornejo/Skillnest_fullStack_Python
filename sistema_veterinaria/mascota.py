class  mascota:
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

        print(f"Información actualizada correctamente: ")