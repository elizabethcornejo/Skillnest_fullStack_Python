class usuario:
    def __init__(self, nombre, email, rut, edad):
        self.nombre = nombre
        self.email = email
        self.rut = rut
        self.edad = edad 

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Rut: {self.rut}")
        print(f"Edad: {self.edad}")

    def actualizar_correo(self, nuevo_correo):
        self.email = nuevo_correo



class Libro:
    def __init__(self, id_libro, autor, titulo, anio_publicacion, disponible = True):
        self.id_libro = id_libro
        self.autor =  autor
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible

    def mostrar_informacion(self):
        print(f"id_libro: {self.id_libro}")
        print(f"Autor: {self.autor}")
        print(f"Titulo: {self.titulo}")
        print(f"Año de publicación: {self.anio_publicacion}")
        print(f"Disponibilidad: {self.disponible}")

    def cambiar_disponibilidad(self, estado_disponibilidad):
        self.disponible = estado_disponibilidad


class Prestamo:
    def __init__(self, usuario, libro, fecha):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha

    def registrar_prestamo(self):
        if  self.libro.disponible:
            self.libro.cambiar_disponibilidad(False)
            print("Prestamo registrado correctamente.")
        else:
            print("El libro no esta disponible.")
        
    def devolver_libro(self):
        self.libro.cambiar_disponibilidad(True)
        print("Libro devuelto correctamente.")

class direccion:
    def __init__(self, comuna, calle, numero_residencia):
        self.comuna = comuna
        self.calle = calle
        self.numero_residencia = numero_residencia


    def envio(self):
        print(f"Comuna: {self.comuna}")
        print(f"Calle: {self.calle}")
        print(f"Numero de la residencia: {self.numero_residencia}")

usuario1 = usuario("camilo", "camilo123@gmail.com", "12345678-8", 16)
usuario2 = usuario("luis", "luis123@gmail.com", "12345678-8", 19)
usuario3 = usuario("jheimy", "jheimy123@gmail.com", "12345678-9", 17)

libro1 = Libro(1, "fernando", "La casa de papel", "2016")
libro2 = Libro(2, "sabrina", "principito", "1985")
libro3 = Libro(3, "luis", "merlina", "2022")

prestamo1 = Prestamo(usuario1, libro1, "25/05/2026")
prestamo2 = Prestamo(usuario2, libro2, "25/05/2026")
prestamo3 = Prestamo(usuario3, libro3, "25/05/2026") 


direccion1 = direccion("La Cisterna", "Trinidad Ramirez", "254")
direccion2 = direccion("La Granja", "Pasaje 1", "2453")
direccion3 = direccion("El Bosque", "Perez Roman", "987")

usuario1.actualizar_correo("camilo2810@gmail.com")
usuario2.actualizar_correo("luis5643@gmail.com")
usuario3.actualizar_correo("jheimycausa@gmail.com")

print()
print()
usuario1.mostrar_datos()
print()
libro1.mostrar_informacion()
print()
prestamo1.registrar_prestamo()
print()
direccion1.envio()
print()
print()
usuario2.mostrar_datos()
print()
libro2.mostrar_informacion()
print()
prestamo2.registrar_prestamo()
print()
direccion2.envio()
print()
print()
usuario3.mostrar_datos()
print()
libro3.mostrar_informacion()
print()
prestamo3.registrar_prestamo()
print()
direccion3.envio()
