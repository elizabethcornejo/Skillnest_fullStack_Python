from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import flash

from flask_app import app
from flask_app import bcrypt
from flask_app.models.usuario import Usuario


@app.route("/")
def login():
    if session.get("usuario_id"):
        return redirect("/dashboard")

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def iniciar_sesion():
    email = request.form["email"].strip()
    password = request.form["password"]

    if email == "" or password == "":
        flash("Debes completar todos los campos.", "danger")
        return redirect("/")

    usuario = Usuario.obtener_por_email(email)

    if usuario is None:
        flash("Correo o contraseña incorrectos.", "danger")
        return redirect("/")

    if not bcrypt.check_password_hash(
        usuario["password"],
        password
    ):
        flash("Correo o contraseña incorrectos.", "danger")
        return redirect("/")

    session["usuario_id"] = usuario["id"]
    session["usuario_nombre"] = usuario["nombre"]

    return redirect("/dashboard")


@app.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "GET":
        return render_template("registro.html")

    nombre = request.form["nombre"].strip()
    apellido = request.form["apellido"].strip()
    email = request.form["email"].strip()
    password = request.form["password"]
    confirmar_password = request.form["confirmar_password"]

    if (
        nombre == ""
        or apellido == ""
        or email == ""
        or password == ""
        or confirmar_password == ""
    ):
        flash("Todos los campos son obligatorios.", "danger")
        return redirect("/registro")

    if password != confirmar_password:
        flash("Las contraseñas no coinciden.", "danger")
        return redirect("/registro")

    usuario_existente = Usuario.obtener_por_email(email)

    if usuario_existente:
        flash("El correo ya está registrado.", "danger")
        return redirect("/registro")

    password_hash = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "password": password_hash
    }

    Usuario.crear(datos)

    flash(
        "Cuenta creada correctamente. Ahora puedes iniciar sesión.",
        "success"
    )

    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")


@app.route("/perfil")
def perfil():

    if not session.get("usuario_id"):
        return redirect("/")

    usuario_id = session["usuario_id"]

    usuario = Usuario.obtener(usuario_id)

    if usuario is None:
        session.clear()
        return redirect("/")

    estadisticas = Usuario.estadisticas(usuario_id)

    categorias = Usuario.cantidad_categorias(usuario_id)

    if estadisticas is None:
        estadisticas = {
            "total": 0,
            "pendientes": 0,
            "progreso": 0,
            "completadas": 0
        }

    if categorias is None:
        categorias = {
            "total": 0
        }

    return render_template(
        "perfil.html",
        usuario=usuario,
        estadisticas=estadisticas,
        categorias=categorias
    )