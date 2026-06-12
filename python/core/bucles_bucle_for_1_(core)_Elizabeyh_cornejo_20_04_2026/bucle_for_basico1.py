"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Barra de experiencia
# Mostrar los niveles del 0 al 100

nivel_actual = 0

while nivel_actual <= 100:
    print(nivel_actual)
    nivel_actual += 1


# 2. Carga de energía
# Mostrar los múltiplos de 2 entre 2 y 500

for energia in range(2, 501, 2):
    print(energia)


# 3. Detector de recompensas
# Si es múltiplo de 10 muestra 
# Si es múltiplo de 5 muestra 

for punto in range(1, 101):

    if punto % 10 == 0:
        print(f"{punto} Recompensa especial")

    elif punto % 5 == 0:
        print(f"{punto} Recompensa normal")


# 4. Suma gigante
# Sumar todos los números pares desde 0 hasta 500000

acumulador = 0

for valor in range(0, 500001, 2):
    acumulador += valor

print(f"La suma total de los números pares es: {acumulador}")


# 5. Viaje al pasado
# Retroceder de 3 en 3 desde 2024

for anio in range(2024, -1, -3):
    print(anio)


# 6. Contador personalizable

comienzo = 4
limite = 20
incremento = 4

for numero in range(comienzo, limite + 1):

    if numero % incremento == 0:
        print(numero)