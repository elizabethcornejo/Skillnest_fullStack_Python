from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de Pokémon
pokedex = [
    {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
    {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
    {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
    {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico", "imagen": "pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
    {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "jigglypuff.png", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
    {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
    {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
    {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
    {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
    {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "snorlax.png", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]


# Error cuando no se encuentra un Pokémon
def pokemon_no_encontrado(mensaje: str):
    """Función simple para renderizar la página 404 con un mensaje."""
    return render_template("404.html", mensaje=mensaje), 404


# Ruta para mostrar todos los Pokémon
@app.route("/pokemon")
def mostrar_todos():
    return render_template("pokemon.html", pokemon_list=pokedex, titulo="Todos los Pokémon")


# Ruta para mostrar un Pokémon por número en la Pokédex
@app.route("/pokemon/<int:id>")
def mostrar_por_id(id):
    # Buscamos el Pokémon que coincida con el ID numérico
    resultado = next((p for p in pokedex if p["id"] == id), None)
    
    if resultado is None:
        return pokemon_no_encontrado(f'No pudimos encontrar información sobre el Pokémon con ID #{id} en nuestra Pokédex.')
    
    # Pasamos una lista con un solo elemento para reutilizar el mismo template
    return render_template("pokemon.html", pokemon_list=[resultado], titulo=f"Detalle de {resultado['nombre']}")


# Ruta para mostrar un Pokémon por nombre
@app.route("/pokemon/<string:nombre>")
def mostrar_por_nombre(nombre):
    # Buscamos ignorando mayúsculas/minúsculas
    resultado = next((p for p in pokedex if p["nombre"].lower() == nombre.lower()), None)
    
    if resultado is None:
        return pokemon_no_encontrado(f'No pudimos encontrar información sobre "{nombre}" en nuestra Pokédex.')
    
    return render_template("pokemon.html", pokemon_list=[resultado], titulo=f"Detalle de {resultado['nombre']}")


# Ruta para mostrar una cantidad específica de Pokémon
@app.route("/pokemon/cantidad/<int:cant>")
def mostrar_cantidad(cant):
    # Tomamos los primeros 'cant' Pokémon de la lista
    seleccionados = pokedex[:cant]
    return render_template("pokemon.html", pokemon_list=seleccionados, titulo=f"Primeros {len(seleccionados)} Pokémon")


if __name__ == "__main__":
    app.run(debug=True)