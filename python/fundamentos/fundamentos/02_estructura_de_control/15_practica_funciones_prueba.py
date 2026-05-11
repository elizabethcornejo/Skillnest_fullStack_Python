#1.-Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
def numeroMayor(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El numero mayor es: {mayor} \nEl numero menor es: {menor} ")

def ejercicio1():
    limit = int(input("Ingresar un limite de valores."))
    listadoNum = []
    i = 1
    while i <= limit:
        num = int(input("Ingresar un numero entero {i} de {limit} :"))
        listadoNum.append(num)
        i+=1
    numoerMayorMenor(listadoNum)

#2.-Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.

def contador_vocales(letras)
    vocales = "aeiouAEIOU"
    return letra in vocales


    def contar_vocales(texto):
        contador = 0
        for letra in texto:
            if es_vocal(letra):
                contador += 1
        print(f"La cadena contiene {contador} vocales.")


        def ejercicio2():
            texto = input("ingrese el texto: ")
            contar_vocales(texto)

ejercicio_contar_vocales()


#3.-Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.

    def filtrar(lista):
        resultado = []
        for nombre in lista:
            if len(nombre) > 5:
                resultado.append(nombre)
        return resultado

    def mostrar():
        nombres = []
        nombresLargos = []
        cantidad = int(input("Cuantos nombres quieres ingresar?"))

        for i in range(cantidad):
            nombre = input("Ingresa un nombre:")
            print(f"{nombres} agregado con exito a la lista")
            nombre.append(nombre)

        for nombre in filtrar(nombres):
            print("Los nombres con mas de 5 letras son: ")

            print(nombre) 


#4.-Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
    def listaNotas(notas):
        lista = 0
        promedio = 0
        for i in range(len(notas)):
            lista += notas[i]
            promedio = lista / (len(notas)) 
        
        if promedio >= 4.0 and promedio <= 7.0:
            return f"El estudiante aprueba con {promedio}"
        elif promedio >= 1.0 and promedio <= 3.9:
            return f"el estudiante no aprueba con {promedio}"
        else:
            return"Error"


    def ejercicio4():
        largo = int(input("cuantas notas va a ingresar: "))
        nota = []
        for i in range(largo):
            int = float(input(f"Ingrese nota {i + 1}: "))
            if int != "":
                nota.append(int)
            print(listaNotas(nota))

#5.-Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.

def descuento(valor):
    sumLista = sum(valor)
    precioInicial = sumaLista
    descuento =sumaLista * 0.1
    precioFinal = precioInicial - descuento
    print(f"El precio inicial de el producto es: \n{precioInicial}\ny con descuento \n{precioFinal}")

    def valores():
        cantidadProductos = int(input("Ingrese la cantidad de productos que quiera: \n"))
        listaPrecios = []
        for i in range(cantidadProducto):
            valorProducto = float(input("Ingrese el valor de el producto: \n"))
            listaPrecios.append(valorProducto)
        descuento(listaPrecios)
valores()


#6.- Crear una función que reciba un número entero y determine si es par o impar.

    def parImpar(numero):
        if numero % 2 == 0:
            print(f"El numero {numero} es Par.")
        elif numero % 3 == 0:
            print(f"El numero {numero} es Impar.")
        else: 
            print("Error")

    def recibirNum():
        num = int(input("Ingrese un numero: "))
        parImpar(num)
    recibirNum()

#7.-Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).

def edades(lista):
    num = 0
    for i in range(len(lista)):
        if lista[i] >= 18:
            num += 1
    return num 

    def personas():
        edad = []
        int = int(input("¿Cuantas personas vas a ingresar hoy?: "))
        for i in range(int):
            var = int(input(">> "))
            if var != "":
                edad.append(var)
            else:
                print("Por favor ingresa valor valido: ")
        resultado = edades(edad)
        print(f"Hay {resultado} personas mayores de edad.")
    personas()

#8.-Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.

def vecesApareces(palabras):
    buscar = input("Ingrese la palabra que desea buscar: ")
    vecesAparece = 0
    for i in range(len(palabras)):
        if buscar == palabras[i]:
            vecesAparece += 1
    print(f"La palabra {buscar} aparece {vecesAparece} en la lista.")


def recibirPalabras():
    cantidad = int(input("Ingrese la cantidad de palabras: "))
    listaPalabras = []
    for i in range(cantidad):
        palabra = input(f"{i + 1}. ")
        listaPalabras.append(palabra)
    vecesAparece(listaPalabras)
#9.-Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.

def soloPositivo(num):
    positiva = []
    for i in range

#10.-Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.






