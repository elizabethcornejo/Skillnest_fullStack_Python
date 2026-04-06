"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random # importacion de libreria para procesos aleatorios


nombre = "Frida Kahlo"  # creacion de variable tipo texto (tipo string) y se asigna un valor en este caso "Frida Kahlo"
print(type(nombre)) # type() = metodo de python para mostrar el tipo de una variable 
print(len(nombre)) # let() = cuenta el largo de la variable, devuelve el largo de una variable 


edad = 25 # creacion de variable tipo numerico(int)


if edad < 18: # se establece condicion if 
   print("Eres menor de edad.") #imprime un mensaje
elif edad == 18:# se establece su condicion elif (else if)
   print("Tienes 18 años.")# imorime un mensaje 
else: # cierre de condicion (si no se cumplen condiciones anteriores)
   print("Eres mayor de edad.")# inmprime un mensaje 


frutas = ["manzana", "pera", "fresa"] # vreacion de array con valores asiganados 
print(frutas[0])# mostrar la primera posicion de arreglo
frutas[0] = "banana"# a laposicion 0 de el arreglo se le asigna el valor de "banana"
frutas.append("uva")# se le agrega "uva" al final de el arreglo 
frutas.remove("pera")#se remueve la palabra "pera" del arreglo


dimensiones = (200, 50) # creamos una dimension tipo tupla (palabra inmutable)
print(dimensiones[0])# imprime la posicion cero de la variable creada 


persona = { # variable tipo object (object)
   "nombre": "Carlos", # se establece un item y su respectivo valor 
   "edad": 30 # se establece un item y su respectivo valor 
}
print(persona["nombre"]) # imprime el valor de el item ejemplo: carlos 
persona["edad"] = 31 # se modifica el valor de el item de la edad a 31
persona["ciudad"] = "Santiago" # se agrega un nuevo item con un valor 
del persona["ciudad"] # se elimina el item completo 


for i in range(5): # for range: se crea bucle en rango desde 0 a 5
   if i == 2: # se establece condicion if == 2
       continue # continue ignora el proceso y continua. 
   if i == 4: # se establece condicion if i == 4
       break # si i es igual que 4 ( i = 4 ), se rompe el bucle 
   print(i)# imprime el valor de i en cada iteracion.(hasta 4)


contador = 0 # se crea una variable tipo contador tipo numerica(int)
while contador < 3: # se crea bucle while con una condicion 
   print(f"while contador es: {contador}") # imprime el contador en un mensaje concatenado con f"" string 
   contador += 1 # incrementa el valor en 1 en cada iteracion 


def saludar_usuario(nombre): #  def - palabra reservada para crear una funcion en python 
   return f"Hola, {nombre}" # devuelve un valor de la funcion


print(saludar_usuario("Francisca")) 
# llamaba a la funcion y muestra el resultado