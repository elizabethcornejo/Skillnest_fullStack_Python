from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>¡Hola!<h1/> <p>Bienvenido a mi página<p/>"


@app.route("/usuario/<nombre>")
def usuario(nombre):
    return f"Hola, {nombre}"

@app.route("/edad/<int:edad>")
def mostrar_edad(edad):
    return f"Tienes {edad} años."

@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):

    return f"¡Hola {nombre}!" * veces

if __name__ == "__main__":
    app.run(debug=True)

