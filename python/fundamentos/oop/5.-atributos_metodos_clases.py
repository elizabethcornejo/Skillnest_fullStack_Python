#Atributos, metodos de clases y metodos estaticos 

# definicion de la clase 

class Estudiante: 
    #Atributo de clase 
    colegio = "Liceo Vate Vicente Huidobro"
    #Lista en donde esten todos los estudiantes 
    estudiantes = []

    #Metodo constructor 
    def __init__(self, nombre, nota):
        #Atributo de instancia 
        self.nombre = nombre
        self.nota = nota

        #Agregar elementos a la lista estudiante (objeto)
        Estudiante.estudiantes.append(self)


    #Metodo de instancia 
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(F"Nota: {self.nota}")

#Metodo de clase 
#Usa (CLS) por que trabaja con las informacion de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre


    @classmethod #este va a contar la cantidad de estudiantes 
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)


        #metodo estatico
        #este no usa CLS ni SELF, solo parametros 

    @staticmethod 
    def aprobar(nota):
        if nota >= 4.0:
            return True 
        else:
            return False


#Creacion de objetos (Instancias)
e1 = Estudiante("Donovan", 4.0)
e2 = Estudiante("Randy", 6.7)
e3 = Estudiante("Dany", 3.9)


#Uso de metodo de instancias
print("==METODO DE INSTANCIAS==")

#Mostrar datos de estudiantes
e1.mostrar_info()
print()
e2.mostrar_info()
print()
e3.mostrar_info()
print()


#Mostrar atributo de la clase
print("==ATRIBUTO DE CLASE==")

print(e1.colegio)
print(e2.colegio)
print(e3.colegio)
print()

#Uso de metodo de clase 
print("===METODO DE CLASES===")

Estudiante.cambiar_colegio("Purkuyen")
print(e1.colegio)
e1.colegio = "VVH"  #Modifica el atributo de la instancia en la clase
print()


Estudiante.cambiar_colegio("Purkuyen")
print(e2.colegio)
e2.colegio = "VVH"
print()


Estudiante.cambiar_colegio("Purkuyen")
print(e3.colegio)
e3.colegio = "VVH"
print()



#Contar estudiantes 

print("===CONTAR ESTUDIANTES===")
print(f"Total estudiantes: {Estudiante.cantidad_estudiantes()}")


#Metodo estatico 
print("===MÉTODO ESTÁTICO===")

print(f"¿{e1.nombre} Aprueba?")
print(Estudiante.aprobar(e1.nota))
print()


print(f"¿{e2.nombre} Aprueba?")
print(Estudiante.aprobar(e2.nota))
print()


print(f"¿{e3.nombre} Aprueba?")
print(Estudiante.aprobar(e3.nota))
print()


##Funcion repaso 
##crear una funcion que valide usuario y contraseña 
def validador(user, password):
    if user == "matias123" and password == "matias123":
        print(f"Bienvenido, {user}")
        return True
    else:
        print(f"Acceso denegado")
        return False

        def enviarDatos():
            username = input("Ingrese su nombre usuario: ")
            password = input("Ingrese su contraseña: ")
            validator(username, password )


    enviarDatos()
