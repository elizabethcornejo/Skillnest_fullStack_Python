from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_app.models.usuario import Usuario
import re

usuarios = Blueprint("usuarios", __name__)

def validar_registro(form):
    errores = []

    if len(form["nombre"].strip()) < 2:
        errores.append("El nombre debe tener mínimo 2 caracteres.")

    if len(form["apellido"].strip()) < 2:
        errores.append("El apellido debe tener mínimo 2 caracteres.")

    email = form["email"].strip().lower()

    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        errores.append("Ingresa un email válido.")

    if len(form["password"]) < 8:
        errores.append("La contraseña debe tener mínimo 8 caracteres.")

    if form["password"] != form["confirmar_password"]:
        errores.append("Las contraseñas no coinciden.")

    return errores

@usuarios.route("/")
def inicio():

    if "usuario_id" in session:
        return redirect(url_for("libros.libros"))

    return redirect(url_for("usuarios.login"))

@usuarios.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip().lower()
        password = request.form["password"]

        usuario = Usuario.buscar_por_email(email)

        if not usuario:
            flash("Email o contraseña incorrectos.", "danger")
            return redirect(url_for("usuarios.login"))

        if not check_password_hash(usuario["password"], password):
            flash("Email o contraseña incorrectos.", "danger")
            return redirect(url_for("usuarios.login"))

        session["usuario_id"] = usuario["id"]
        session["usuario_nombre"] = usuario["nombre"]

        flash("Sesión iniciada correctamente.", "success")

        return redirect(url_for("libros.libros"))

    return render_template("login.html")

@usuarios.route("/registro", methods=["POST"])
def registro():

    errores = validar_registro(request.form)

    email = request.form["email"].strip().lower()

    if Usuario.buscar_por_email(email):
        errores.append("El email ya está registrado.")

    if errores:

        for error in errores:
            flash(error, "danger")

        return redirect(url_for("usuarios.login"))

    password_hash = generate_password_hash(
        request.form["password"]
    ).decode("utf-8")

    Usuario.crear({
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": email,
        "password": password_hash
    })

    flash(
        "Cuenta creada correctamente. Ahora puedes iniciar sesión.",
        "success"
    )

    return redirect(url_for("usuarios.login"))

@usuarios.route("/logout")
def logout():

    session.clear()

    flash("Sesión cerrada correctamente.", "success")

    return redirect(url_for("usuarios.login"))