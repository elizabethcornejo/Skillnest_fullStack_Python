from flask import Blueprint, render_template, request, redirect, session, flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

usuarios = Blueprint("usuarios", __name__)

bcrypt = Bcrypt()


@usuarios.route("/")
def inicio():
    return redirect("/login")


@usuarios.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    email = request.form["email"]
    password = request.form["password"]

    usuario = Usuario.buscar_por_email(email)

    if usuario is None:
        flash("Usuario no encontrado")
        return redirect("/login")

    if not bcrypt.check_password_hash(usuario.password, password):
        flash("Contraseña incorrecta")
        return redirect("/login")

    session["usuario_id"] = usuario.id
    session["nombre"] = usuario.nombre

    return redirect("/libros")


@usuarios.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "GET":
        return render_template("registro.html")

    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    email = request.form["email"]
    password = request.form["password"]

    if len(nombre) < 2:
        flash("Nombre muy corto")
        return redirect("/registro")

    if len(apellido) < 2:
        flash("Apellido muy corto")
        return redirect("/registro")

    if len(password) < 6:
        flash("La contraseña debe tener al menos 6 caracteres")
        return redirect("/registro")

    usuario = Usuario.buscar_por_email(email)

    if usuario is not None:
        flash("Este correo ya está registrado")
        return redirect("/registro")

    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "password": password_hash
    }

    Usuario.crear(data)

    flash("Registro exitoso. Ahora puedes iniciar sesión")

    return redirect("/login")


@usuarios.route("/logout")
def logout():

    session.clear()

    return redirect("/login")