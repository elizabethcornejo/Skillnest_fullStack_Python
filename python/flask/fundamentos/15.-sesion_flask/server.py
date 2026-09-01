from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# Clave secreta necesaria para proteger la sesión
app.secret_key = "una-clave-secreta"


# Ruta principal con el formulario
@app.route("/")
def index():
    return render_template("index.html")


# Procesamiento del formulario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    # 1. Obtener los 3 datos del formulario
    nombre = request.form["nombre"]
    email = request.form["email"]
    ciudad = request.form["ciudad"]

    # 2. Guardar la información en la sesión
    session["nombre_usuario"] = nombre
    session["email_usuario"] = email
    session["ciudad_usuario"] = ciudad

    # 3. Redireccionar
    return redirect("/mostrar_usuario")


# Mostrar confirmación de registro
@app.route("/mostrar_usuario")
def mostrar_usuario():
    return render_template("mostrar.html")


# ⭐ DESAFÍO ADICIONAL: Ruta /perfil
@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


if __name__ == "__main__":
    app.run(debug=True)