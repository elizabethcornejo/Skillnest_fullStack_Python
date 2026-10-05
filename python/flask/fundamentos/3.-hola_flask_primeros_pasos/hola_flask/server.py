def mayor_menor(numeros):
    mayor = numeros[0]
    menor = numeros[0]

    for numero in numeros:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

    print("Número mayor:", mayor)
    print("Número menor:", menor)


def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    cantidad = 0

    for letra in texto:
        if letra in vocales:
            cantidad += 1

    print("Cantidad de vocales:", cantidad)


def nombres_largos(nombres):
    print("Nombres con más de 5 letras:")

    for nombre in nombres:
        if len(nombre) > 5:
            print(nombre)


def promedio_notas(notas):
    suma = 0

    for nota in notas:
        suma += nota

    promedio = suma / len(notas)

    print("Promedio:", promedio)

    if promedio >= 4.0:
        print("El estudiante aprueba")
    else:
        print("El estudiante no aprueba")


def descuento_precios(precios):
    for precio in precios:
        descuento = precio * 0.10
        nuevo_precio = precio - descuento

        print("Precio original:", precio)
        print("Precio con descuento:", nuevo_precio)


def par_impar(numero):
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")


def mayores_edad(edades):
    cantidad = 0

    for edad in edades:
        if edad >= 18:
            cantidad += 1

    print("Personas mayores de edad:", cantidad)


def buscar_palabra(palabras, palabra):
    cantidad = 0

    for elemento in palabras:
        if elemento == palabra:
            cantidad += 1

    print("La palabra aparece", cantidad, "veces")


def numeros_positivos(numeros):
    positivos = []

    for numero in numeros:
        if numero > 0:
            positivos.append(numero)

    print("Números positivos:", positivos)


def productos_stock(productos):
    print("Productos con stock menor a 5:")

    for producto in productos:
        if producto["stock"] < 5:
            print(producto["nombre"], "-", producto["stock"], "unidades")


while True:
    print("\n--- MENÚ ---")
    print("1. Número mayor y menor")
    print("2. Contar vocales")
    print("3. Nombres con más de 5 letras")
    print("4. Promedio de notas")
    print("5. Descuento de productos")
    print("6. Par o impar")
    print("7. Mayores de edad")
    print("8. Buscar palabra")
    print("9. Números positivos")
    print("10. Productos con stock menor a 5")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numeros = [10, 25, 3, 18, 7]
        mayor_menor(numeros)

    elif opcion == "2":
        texto = input("Ingrese un texto: ")
        contar_vocales(texto)

    elif opcion == "3":
        nombres = ["Elizabeth", "Ana", "Cristobal", "Luis", "Fernanda"]
        nombres_largos(nombres)

    elif opcion == "4":
        notas = [5.5, 4.0, 6.0, 3.5]
        promedio_notas(notas)

    elif opcion == "5":
        precios = [1000, 2500, 5000, 10000]
        descuento_precios(precios)

    elif opcion == "6":
        numero = int(input("Ingrese un número entero: "))
        par_impar(numero)

    elif opcion == "7":
        edades = [15, 18, 20, 16, 25, 12]
        mayores_edad(edades)

    elif opcion == "8":
        palabras = ["python", "java", "python", "html", "python", "css"]
        palabra = input("Ingrese la palabra que desea buscar: ")
        buscar_palabra(palabras, palabra)

    elif opcion == "9":
        numeros = [-5, 10, -2, 8, 0, 15, -3]
        numeros_positivos(numeros)

    elif opcion == "10":
        productos = [
            {"nombre": "Pan", "stock": 10},
            {"nombre": "Leche", "stock": 3},
            {"nombre": "Arroz", "stock": 7},
            {"nombre": "Huevos", "stock": 2},
            {"nombre": "Fideos", "stock": 4}
        ]

        productos_stock(productos)

    elif opcion == "0":
        print("Programa finalizado")
        break

    else:
        print("Opción no válida")