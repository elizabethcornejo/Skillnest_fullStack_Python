import os
#Funciones basicas practica 2

#Ejercicio 1............................................

# Calcula experiencia
def multiplica_por_2(num):
    result = []
    for i in range(num + 1)
        result.append(i + 2)#el append sirve para agregarlo a la lista 
    return result
result1 = multiplica_por_2(5)
print(result1)


# Debe retornar: [0, 2, 4, 6, 8, 10]



#Ejercicio 2.........................................

# Analiza publicaciones
def suma_y_resta(num):
suma + list[0] + list[1]
resta = list[0] - list[1]
print(f"suma : {suma}")
return resta 

def ejercicio2():

resta = suma_y_resta([120, 115])
print(f"retorno / resta: {resta}")
# Imprime: 235 y retorna: 5

#Ejercicio 3...........................................
# Puntaje ajustado
def sumatoria_menos_longitud(sumatoria):
    total = sum(sumatoria)
    longitud = len(sumatoria)
    resultado = total - longitud
    print(f"Total = {total}, longitud = {longitud}")
    return resultado
def ejercicio3():
    retornar = sumatoria_menos_longitud([10, 5, 3, 7])
    print(f"El resultado de el retorno es: {retornar}")

# Suma total = 25, longitud = 4, debe retornar: 21

#Ejercicio 4............................................
# Ajusta visualizaciones
def valores_multiplicados_segundos(lista):
    if len(lista) < 2:
        print(len(lista))
        return []
    else:
        segEle = lista[1]
        nuevaLista = []
        for i in lista:
            nuevaLista.append(i *segEle)
        long = len(nuevaLista)
        print(long)
        return nuevaLista

def ejercicio4():
    result1 = valore_multiplicados_segundos([100, 3, 50, 20])
    print(result1)
    print()
    #imprime: 4 y retorna: [300, 9, 150, 60]
    result2 = valores_multiplicados_segundo([100])
    print(result2)
    #imprime 1 y retorna []

valores_multiplicados_segundo([100, 3, 50, 20])
# Imprime: 4 y retorna: [300, 9, 150, 60]
# Imprime: 1 y retorna: []

#Ejercicio 5.............................................
# Genera precio fijo
def valor_multiplicado_longitud(a, b):
    multilist = []
    for i in range(0, b):
        multilist.append(a * b)
    return multilist

def ejercicio5():
    result1 = valor_multiplicado_longitud(5, 2)
    print(f"Resultado 1: {result1}")
    #debe de retornar: [10, 10]
    result2 = valor_multiplicado_longitud(7, 5)
    print(f"Resultado 2: {result2}")
    #debe de retornar: [35, 35, 35, 35, 35]



def limpiar_consola():
    os.system('cls')

continuar = True
while continuar :
    print("\n---Ejercicios Python---")
    print("---1.- Ejercicio 1 ---")
    print("---2.- Ejercicio 2 ---")
    print("---3.- Ejercicio 3 ---")
    print("---4.- Ejercicio 4 ---")
    print("---5.- Ejercicio 5 ---")

    opcion = input("\n---Elige una opcion: (1-5) (0 para salir) = ")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        print(numerosDinamicos())
    elif opcion == "2":
        print("\nejecutando ejercicio 2: ")
        print()
    elif opcion == "3":
        print("\nejecutando ejercicio 3: ")
        print()
    elif opcion == "4":
        print("\nejecutando ejercicio 4: ")
        print()
    elif opcion == "5":
        print("\nejecutando ejercicio 5: ")
        print()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False 
    else: 
        limpiar_consola()
        print("Opción no valida,intenta otra vez.")
