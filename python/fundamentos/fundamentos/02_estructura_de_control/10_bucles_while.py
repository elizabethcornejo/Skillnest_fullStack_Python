#Guía de Ejercicios: Lógica Fundamental
#I. Interacción y Condicionales (Básico)
#1. Números Pares Dinámicos
#Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos.

#2. Verificador de Edad y Acceso
#Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+).Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.

#3. Calculadora de Descuentos
#Solicita el precio de un producto y la cantidad comprada.
#Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, 
#el descuento aplicado y el total final.

def aplicarDescuento():
    precio = float(input("Ingresar el precio del producto"))
    cantidad = int(input("Ingresar cantidad: "))
    if producto >= 100:
        descuento = producto * 0.15
    else:
        descuento = 0
    total = producto - descuento
    print(f"El subtotal es: {producto}. El escuento aplicado es: {descuento}.")



#4. Clasificador de Números
#Pide un número al usuario e indica si es: Positivo-Par, 
#Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
#II. Iteraciones y Bucles (Intermedio)

def calsificadorNum():
    num = int(input("Ingrese un número: "))
    if num > 0:
        if num % 2 == 0:
            print("Positivo-Par")
        elif num % 2 == 1:
            print("Positivo-Impar")
        elif num < 0:
            if num % 2 == 0:
                print("Negativo-Par")
        elif num % 2 == 1:
                print("Negativo-Impar")

        else:
            print("Es 0")


#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, 
#pero solo muestra los resultados que sean múltiplos de 3.


def tablaMultiplicar():
    num = int(input("Ingresa Número a trabajar: "))
    for i in renge (1, 13):
        resultado = num * i 
        if resultado % 3 == 0
        print(f"del {num} solo estos numeros son divisibles por 3: {resultado}. ")

#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).

def sumatoriaCentinela():
    suma_total = 0
    while true:
        n = int(input("Ingresa un numero ( negativo para salir ):"))
        if n < 0:
            break
        suma_total += n 
    print(f"La suma total es: {suma_total}")
        


#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.

def contadorVocales():
    texto = input("Ingresa una palabra o frace: ").lower()
    vocales = 0
    for i in range(len(texto)):
        vocales += 1
        if texto[i].lower() == "a" or texto[i].lower() == "e" or texto[i].lower() == "i" or texto[i].lower() == "o" or texto[i].lower() == "u"
        vocales += 1
    print(f"La cadena '{texto}' tiene {vocales} vocales en total.")


#8. Validación de Contraseña
#Define una contraseña en una variable. Pide al usuario que la intente adivinar. Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
#III. Manejo de Arreglos / Listas (Avanzado)

def 


#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.

def nombres():
    nombres = []
    max = 0
    while max < 5:
        int = input(f"Por favor ingreseun nombre {max + 1}: ")
        if int !="":
            nombres.append(int)
            max += 1
        else:
            print("Tienes que ingresar un nombre: ")
    for i in range(4, -1, -1):
        print(nombre[i])

#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.
def promedioNotas():

cantidad = int(input("¿Cuantas notas desea ingresar?"))
notas = []
for i in range(cantidad):
    nota = float (input(f"nota {i+1}: "))
    notas.append(notas)

    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio}")
    print(f"Notas mas alta: {max(notas)}")
    print(f"Notas mas bajas: {min(notas)}")

#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los números que sean mayores a 50. Muestra ambos arreglos.
def filtrosArreglos():
cantidad = int(input("¿Cuanto numeros desea ingresar: "))
mayor50 = []
for i in range(1,cantidad + 1)
if arrayUsuario = int(input("Ingrese un numero: "))
if arrayUsuario > 50:
    mayor50.append(arayUsuario)
    else:
        nUser.append(arrayUsuario)
        print(f"Valores ingresados por el usuario: {nUser} \nValores mayor a 50: {mayor50}")


#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.
#IV. Retos de Lógica Combinada
def busacdorElemento():
    ciudades = ["Nairobi", "Tokio", "Santiago", "Lima", "Caracas", "Rio", "Berlin", "Seul", "Buenos aires"]
    ciudad = input("Ingresar ciudad (con mayuscola al principio): ")
    esta = ciudades.index(ciudad)
    if esta < len(ciudades):
            print(f"Tu ciudad esta en el arreglo, en la posicion {esta}")
        else:
            print(f"tu ciudad esta en el arrglo")
#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
def inventario():
    nombres_productos = []
    precios = []

    for i in range(3):
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        nombres_productos.append(nombre)
        precios.append(precios)
    print("\nInventario: ")
    for i in range(3):
        print(f"Producto: {nombres_productos[i]} Precio {precios[i]}")

#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.

def listaCompras():
    lista= []
    while True:
        item = input("Articulo (o 'terminar')")
        if item.lower() == "terminar":
            break
        lista.append(item)
        print(f"Ordenada: {sorted(lista)}")


#15. Análisis de Temperaturas
#Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
#El promedio semanal.
#Cuántos días la temperatura fue superior a 25 grados.
#El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).

def analisisTemperatura():
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    diasSuperior = []
    total = 0
    baja = 100
    diaBaja = ""
    cant = 0

    while cant < 7:
        temps = float(input(f"Ingrese temperatura de el dia {dias{cant}}: "))
        total += temps

        if temps < baja and temps < 25:
            baja = temps
            diaBaja = dias[cant]
        elif temps> 25:
            diasSuperior.append(dias[cant])
        



continuar = True
while continuar :
    print("\n---Ejercicios Python---")
    print("---1.- Ejercicio 1 ---")
    print("---2.- Ejercicio 2 ---")
    print("---3.- Ejercicio 3 ---")
    print("---4.- Ejercicio 4 ---")
    print("---5.- Ejercicio 5 ---")
    print("---6.- Ejercicio 6 ---")
    print("---7.- Ejercicio 7 ---")
    print("---8.- Ejercicio 8 ---")
    print("---9.- Ejercicio 9 ---")
    print("---10.- Ejercicio 10 ---")
    print("---11.- Ejercicio 11 ---")
    print("---12.- Ejercicio 12 ---")
    print("---13.- Ejercicio 13 ---")
    print("---14.- Ejercicio 14 ---")
    print("---15.- Ejercicio 15 ---")

    opcion = input("\n---Elige una opcion: (1-15) (0 para salir) = ")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        print(numerosDinamicos())
    elif opcion == "2":
        print("\nejecutando ejercicio 2: ")
        print()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False 
    else: 
        print("Opcion novalilda, intenta otra vez")

