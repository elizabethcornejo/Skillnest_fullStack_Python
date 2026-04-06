
#CADENA LITERAL
print("Esta es una cadenas de caracteres.")

# CONCATENAR
nombre = "Marcelo"
print("Me llamo", nombre)

nombre = "Marcelo"
print("Mi nombre es "+ nombre)

#CONVERCION DE TIPOS
print("¿Cuántas vocales hay? " + 5) 
#ERROR: TypeError: can only concatenate str (not "int") to str
print("¿Cuántas vocales hay? " + str(5)) #Imprime: ¿Cuántas vocales hay? 5


tiempo_preparacion = 1
tiempo_horneado = "2"
tiempo_total = tiempo_preparacion + tiempo_horneado 
#ERROR: TypeError: unsupported operand type(s) for +: 'int' and 'str'
tiempo_total = tiempo_preparacion + int(tiempo_horneado) #Imprime: 3

#INTERPOLACION DE CADENAS 

'''
También tenemos la posibilidad de insertar variables en nuestras
cadenas, una práctica conocida como interpolación de cadenas.
Existen distintas maneras de llevar a cabo esta tarea.
'''

#CADENAS 
nombre = "Marcelo"
edad = 29
print(f"Mi nombre es {nombre} y tengo {edad} años de edad.")

#STRING FORMAL
nombre = "Marcelo"
edad = 29
print("Mi nombre es {} y tengo {} años de edad.".format(nombre, edad))

#Imprime: Mi nombre es Marcelo y tengo 29 años de edad.
print("Tengo {} años de edad y mi nombre es {}".format(edad, nombre))

#Imprime: Tengo 29 años de edad y mi nombre es Marcelo

#%-FORMATTING

nombre = "Marcelo"
edad = 29
print("Mi nombre es %s y tengo %d años de edad." % (nombre, edad))

#Imprime: Mi nombre es Marcelo y tengo 29 años de edad.

#METODOS DE CADENAS INTEGRADOS  

'''
Además de .format(), existen muchos métodos más que nos ayudarán a manipular nuestras cadenas. Estos son algunos de ellos:

🔠 string.upper(): regresa la cadena con todos los caracteres en mayúscula.
🔡 string.lower(): regresa la cadena con todos los caracteres en minúscula.
🔡 string.count(substring): regresa el número de recurrencias de una subcadena de una cadena.
✂️ string.split(caracter):regresa una lista de valores donde la cadena es dividida en el carácter especificado.
 En caso de no enviar el carácter, la división se hace en cada espacio.
🔍 string.find(substring): regresa el índice del comienzo de la primer recurrencia de la subcadena dentro de una cadena.
🔤 string.isalnum(): regresa un booleano dependiendo de si la longitud de la cadena es > 0 y todos los caracteres sean alfanuméricos 
(solo letras y números). Las cadenas que incluyen espacios y puntuación devolverán False con este método. Métodos similares incluyen 
.isalpha(), .isdigit(), .islower(), .isupper(), entre otros. Todos devuelven booleanos.
🪢 string.join(lista): regresa una cadena que contiene todas las cadenas de nuestro conjunto (en este caso, una lista) concatenadas.
🔚 string.endswith(substring): regresa True o False si los últimos caracteres de la cadena coinciden con la subcadena.
'''