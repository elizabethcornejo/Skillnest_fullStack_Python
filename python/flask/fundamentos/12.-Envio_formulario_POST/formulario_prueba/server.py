from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    nombre = request.form["nombre"]
    email = request.form["email"]
    edad = request.form["edad"]
    ciudad = request.form["ciudad"]
    telefono = request.form["telefono"]

    print("====================================")
    print("Usuario registrado correctamente")
    print("Nombre :", nombre)
    print("Correo :", email)
    print("Edad :", edad)
    print("Ciudad :", ciudad)
    print("Teléfono :", telefono)
    print("====================================")

    return render_template(
        "usuario.html",
        nombre=nombre,
        email=email,
        edad=edad,
        ciudad=ciudad,
        telefono=telefono
    )

if __name__ == "__main__":
    app.run(debug=True)