from flask import Flask, render_template, request, abort

app = Flask(__name__)

# Base de datos local de Pokémon con información detallada
POKEMON_DATABASE = [
    {
        "id": 1,
        "name": "Bulbasaur",
        "type": "Planta / Veneno",
        "image": "bulbasaur.png",
        "description": "Este Pokémon nace con una semilla en el lomo que crece gradualmente con el tiempo.",
        "height": "0.7 m",
        "weight": "6.9 kg",
        "stats": {"hp": 45, "attack": 49, "defense": 49, "speed": 45}
    },
    {
        "id": 4,
        "name": "Charmander",
        "type": "Fuego",
        "image": "charmander.png",
        "description": "La llama de su cola indica la fuerza vital que posee. Si está sano, la llama arderá con fuerza.",
        "height": "0.6 m",
        "weight": "8.5 kg",
        "stats": {"hp": 39, "attack": 52, "defense": 43, "speed": 65}
    },
    {
        "id": 39,
        "name": "Jigglypuff",
        "type": "Normal / Hada",
        "image": "jigglypuff.png",
        "description": "Si entona su dulce canción, sus oyentes caerán rendidos en un profundo sueño de inmediato.",
        "height": "0.5 m",
        "weight": "5.5 kg",
        "stats": {"hp": 115, "attack": 45, "defense": 20, "speed": 20}
    },
    {
        "id": 94,
        "name": "Gengar",
        "type": "Fantasma / Veneno",
        "image": "gengar.png",
        "description": "Para quitarle la vida a su presa, se oculta en su sombra y espera pacientemente el momento perfecto.",
        "height": "1.5 m",
        "weight": "40.5 kg",
        "stats": {"hp": 60, "attack": 65, "defense": 60, "speed": 110}
    }
]

def buscar_pokemon_por_filtro(criterio=""):
    """Función auxiliar para filtrar la lista de criaturas."""
    criterio = criterio.strip().lower()
    if not criterio:
        return POKEMON_DATABASE
    
    resultados = []
    for monster in POKEMON_DATABASE:
        if criterio in monster["name"].lower() or criterio in str(monster["id"]):
            resultados.append(monster)
    return resultados

@app.route('/')
def mostrar_catalogo():
    busqueda_usr = request.args.get('q', '')
    lista_filtrada = buscar_pokemon_por_filtro(busqueda_usr)
    return render_template('index.html', pokemons=lista_filtrada, query=busqueda_usr)

@app.route('/pokemon/<int:poke_id>')
def ver_detalle_pokemon(poke_id):
    coincidencia = next((p for p in POKEMON_DATABASE if p["id"] == poke_id), None)
    if not coincidencia:
        abort(404)
    return render_template('detail.html', pokemon=coincidencia)

@app.errorhandler(404)
def recurso_no_encontrado(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)