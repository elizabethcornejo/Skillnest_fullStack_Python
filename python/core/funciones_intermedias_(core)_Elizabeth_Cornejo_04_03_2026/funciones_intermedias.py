#parte 1

# Ranking de puntajes de un torneo de eSports
puntaje = [ [1000, 1500, 2000], [300, 700, 1400] ]

# Ranking de puntajes de un torneo de eSports
puntaje = [ [1000, 1500, 2000], [300, 700, 1400] ]
puntaje[1][0] = 600
print(puntaje)


# Lista de creadores de contenido en una plataforma de streaming
streamer = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamer[0]["nombre"] = "EliteGamerX"
print(streamer)


# Eventos en distintas ciudades del mundo
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}

eventos["Estados Unidos"][2] = "San Francisco"
print(eventos)


# Coordenadas de la sede de un torneo internacional
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]

ubicacion[0]["latitud"] = "40.712776"
print(ubicacion)

#parte 2

def diccionario(lista):
    for streamer in lista:
        print(f"nombre : {streamer['nombre']} seguidores : {streamer['seguidores']}")


diccionario(streamer)

def valores(clave, lista):
    for item in lista:
        print(item[clave])

valores("nombre", streamer)
valores("seguidores", streamer)


#parte 3


for paises, lista in eventos.items():
    print(f"---{paises.upper()}---")
    for item in lista:
        print(f"{item}")