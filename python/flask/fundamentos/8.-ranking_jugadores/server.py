from flask import Flask, render_template

app = Flask(__name__)

# Datos de jugadores con puntajes
jugadores = [
{"nombre": "AlexGamer", "puntaje": 5000},
{"nombre": "PixelMaster", "puntaje": 7500},
{"nombre": "ShadowNinja", "puntaje": 8200},
{"nombre": "CyberWarrior", "puntaje": 9100},
{"nombre": "UltraNoob", "puntaje": 3000}
]


# Ruta para mostrar el ranking de jugadores




# Ruta para mostrar un número limitado de jugadores

# Ruta para personalizar el color del ranking
@app.route("/jugadores/color/<color>")
# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True)