class persona:
    def __init__(self, nombre, email, telefono, rut, comuna, calle, numero_residencia):
        self.nombre = nombre
        self.email =  email
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

        print(f"Información actualizada correctamente: ")