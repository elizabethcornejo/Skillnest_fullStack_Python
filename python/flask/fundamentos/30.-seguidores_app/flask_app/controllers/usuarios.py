from flask_app import app

from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_app.models.usuario import Usuario
from flask_app.models.seguidor import Seguidor


@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))


@app.route("/usuarios")
def usuarios():

    usuarios = Usuario.get_all()
    relaciones = Seguidor.get_all()

    return render_template(
        "usuarios.html",
        usuarios=usuarios,
        relaciones=relaciones
    )


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():

    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    email = request.form["email"]

    if not nombre or not apellido or not email:
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for("usuarios"))

    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }

    Usuario.save(data)

    flash("Usuario creado correctamente.", "success")

    return redirect(url_for("usuarios"))


@app.route("/seguir", methods=["POST"])
def seguir():

    usuario_id = request.form["usuario_id"]
    seguidor_id = request.form["seguidor_id"]

    data = {
        "usuario_id": usuario_id,
        "seguidor_id": seguidor_id
    }

    if Seguidor.existe(data):
        flash("Esta relación ya existe.", "warning")
        return redirect(url_for("usuarios"))

    Seguidor.seguir(data)

    flash("Relación registrada correctamente.", "success")

    return redirect(url_for("usuarios"))