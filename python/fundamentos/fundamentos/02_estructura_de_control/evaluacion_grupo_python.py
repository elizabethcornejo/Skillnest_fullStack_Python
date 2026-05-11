#Ejericio teté



#lista de nombres y que muestre una letra
def filtrar_letra(lista, letra):
    resultado = []
    letra = letra.lower()# convertimos la letra a minúscula para que la comparación sea visible 
    
    for nombre in lista:
        # vemos si el nombre empieza con la letra usando lower()
        if nombre.lower().startswith(letra): #startswith es para strings que devuelve True si el texto empieza con el carácter que le pidas.
            resultado.append(nombre)
    return resultado

def mostrar():
    nombres = []
    cantidad = int(input("¿Cuántos nombres quieres ingresar? "))

    for i in range(cantidad):
        nombre = input(f"{i+1}. Ingresa un nombre: ")
        nombres.append(nombre) # Agregamos el nombre a la lista
        print(f"'{nombre}' agregado con éxito.")

    letra_buscada = input("¿Por qué letra quieres filtrar? ")
    nombres_filtrados = filtrar_letra(nombres, letra_buscada)
    print(f"\n--- Resultados (Letra: {letra_buscada}) ---")# muestra le resultados con el conteo
    for nombre in nombres_filtrados:
        print(nombre)
    
    print(f"\nTotal de nombres que cumplen la condición: {len(nombres_filtrados)}")
mostrar()



