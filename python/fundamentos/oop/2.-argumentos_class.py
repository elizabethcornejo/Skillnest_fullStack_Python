#➡️ Pasar argumentos 
#Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__ y 
#que de esta manera podamos asignarle a los atributos los valores correspondientes.


class Usuario:
    def __init__(self, nombre, apellido, email): #estos son parametros
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
        
#creacion de las instancias 
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la,",30000,0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la",50000,20000)
tete = Usuario("tete" , "cornejo", "tete@gmail.com", 1000, 20)
#imprimimos valores 
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel


#-------:tarea rapida ------------------

'''
Crear una clase estudiante y asignarle los siguientes atributos:
(rut,nombre, apellido, especialidad, fecha_nac)
Crear tres instancias para la clase,con distintas personas.
- imprimir el nombre y apellido concatenado + especialidad.
'''
class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac): 
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.rut = rut
        self.fecha_nac = fecha_nac

randy = Estudiante("22.898.879-0", "randy", "Cortinez", "programacion", "29/11/2008")
benjamin = Estudiante("22.926.226-2", "benjamin", "delgado", "programacion", "07/01/2009")
dany = Estudiante ("18.555.870-3", "dany", "hernandez", "programacion", "04/08/1993")

print(f"{randy.nombre} {randy.apellido} {randy.rut} {randy.especialidad} {randy.fecha_nac}")
print(f"{benjamin.nombre} {benjamin.apellido} {benjamin.rut} {benjamin.especialidad} {benjamin.fecha_nac}")
print(f"{dany.nombre} {dany.apellido} {dany.rut} {dany.especialidad} {dany.fecha_nac}")

