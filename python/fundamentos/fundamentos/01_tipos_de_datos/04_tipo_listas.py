#tipo listas
#sintaxis basica
lista_vacia = []
lista_compras = ['tomate', 'pan', 'queso', 'jamón']

# distintos tipos de datos dentro de una lista 
lista_especial = [1, 2, ['a', 'b', 'c'], True]

#union y copias de listas
verso1 = ['dale', 'a', 'tu', 'cuerpo']
verso2 = ['alegria', 'macarena']
estrofa = verso1 + verso2
print(estrofa)
cancion = 3 * estrofa
print(cancion)

#indices en las listas 
cajonera = ["pantalones", "camisetas", "calcetines"]
print(cajonera[0]) #Accedemos al cajón con índice 0. Imprime: "pantalones"
print(cajonera[1]) #Accedemos al cajón con índice 1. Imprime: "camisetas"
print(cajonera[2]) #Accedemos al cajón con índice 2. Imprime: "calcetines"
cajonera[1] = "sueters" #Cambiamos el valor del cajón con índice 1
print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines']


#manipulacion de listas 
cajonera.append("vestidos") #Agregamos "vestidos" al final de la lista
print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines', 'vestidos']

#Slicing
lista_grande = [2, 4, 6, 8, 10, 12, 14, 16]
print(lista_grande[3:]) #Imprime:[8, 10, 12, 14, 16]
print(lista_grande[:6]) #Imprime:[2, 4, 6, 8, 10, 12]
print(lista_grande[3:6]) #Imprime:[8, 10, 12]

#funciones integradas 
vocales = ['a', 'e', 'i', 'o', 'u']
print(len(vocales)) #Imprime: 5

'''
list.append(valor): añade un valor al final de la lista.
list.pop(índice): elimina un valor en la posición dada. Si no se pasa ningún parámetro, se eliminará el último valor en la lista.
list.index(valor): devuelve el índice (posición) del valor dado si existe en la lista y genera un error si no existe.
list.reverse(): invierte el orden de los elementos, en su lugar.*
list.sort(): ordena los elementos de menor a mayor, o alfabéticamente para cadenas.
'''