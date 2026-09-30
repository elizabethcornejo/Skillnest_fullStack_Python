from flask import render_template, request, redirect, session
from models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
import re


def registro():

    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    email = request.form["email"]
    password = request.form["password"]
    confirmar = request.form["confirmar"]

    errores = []

    if not nombre:
        errores.append("El nombre es obligatorio.")
    elif not nombre.isalpha() or len(nombre) < 2:
        errores.append("El nombre debe tener solo letras y al menos 2 caracteres.")

    if not apellido:
        errores.append("El apellido es obligatorio.")
    elif not apellido.isalpha() or len(apellido) < 2:
        errores.append("El apellido debe tener solo letras y al menos 2 caracteres.")

    if not email:
        errores.append("El correo electrónico es obligatorio.")
    elif not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        errores.append("El correo electrónico no tiene un formato válido.")

    if not password:
        errores.append("La contraseña es obligatoria.")
    elif len(password) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres.")

    if password != confirmar:
        errores.append("Las contraseñas no coinciden.")

    usuario_existente = Usuario.buscar_por_email(email)

    if usuario_existente:
        errores.append("El correo electrónico ya está registrado.")

    if errores:
        return render_template(
            "index.html",
            errores_registro=errores
        )

    password_hash = generate_password_hash(password)

    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "password": password_hash
    }

    id_usuario = Usuario.crear(datos)

    session["usuario_id"] = id_usuario

    return redirect("/dashboard")


def login():

    email = request.form["email"]
    password = request.form["password"]

    errores = []

    usuario = Usuario.buscar_por_email(email)

    if not usuario:
        errores.append("El correo electrónico no está registrado.")
    else:

        password_hash = usuario[4]

        if not check_password_hash(password_hash, password):
            errores.append("La contraseña es incorrecta.")

    if errores:
        return render_template(
            "index.html",
            errores_login=errores
        )

    session["usuario_id"] = usuario[0]

    return redirect("/dashboard")


def dashboard():

    if "usuario_id" not in session:
        return redirect("/")

    usuario = Usuario.buscar_por_id(session["usuario_id"])

    return render_template(
        "dashboard.html",
        usuario=usuario
    )


def logout():

    session.clear()

    return redirect("/")