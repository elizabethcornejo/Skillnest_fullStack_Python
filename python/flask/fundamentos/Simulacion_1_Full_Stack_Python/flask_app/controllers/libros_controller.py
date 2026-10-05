from flask import Blueprint, render_template, request, redirect, session, flash
from flask_app.models.libro import Libro

libros = Blueprint("libros", __name__)


@libros.route("/libros")
def mostrar_libros():

    if "usuario_id" not in session:
        return redirect("/login")

    mis_libros = Libro.mis_libros(session["usuario_id"])
    comunidad = Libro.todos()

    return render_template(
        "libros.html",
        mis_libros=mis_libros,
        comunidad=comunidad
    )


@libros.route("/libros/nuevo")
def nuevo():

    if "usuario_id" not in session:
        return redirect("/login")

    return render_template("nuevo_libro.html")


@libros.route("/libros/crear", methods=["POST"])
def crear():

    if "usuario_id" not in session:
        return redirect("/login")

    titulo = request.form["titulo"].strip()
    autor = request.form["autor"].strip()
    genero = request.form["genero"].strip()
    fecha = request.form["fecha_publicacion"]
    descripcion = request.form["descripcion"].strip()

    if len(titulo) < 2:
        flash("El título debe tener al menos 2 caracteres")
        return redirect("/libros/nuevo")

    if len(autor) < 2:
        flash("El autor debe tener al menos 2 caracteres")
        return redirect("/libros/nuevo")

    if genero == "":
        flash("Debes seleccionar un género")
        return redirect("/libros/nuevo")

    if fecha == "":
        flash("Debes ingresar una fecha de publicación")
        return redirect("/libros/nuevo")

    if len(descripcion) < 10:
        flash("La descripción debe tener al menos 10 caracteres")
        return redirect("/libros/nuevo")

    data = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "fecha_publicacion": fecha,
        "descripcion": descripcion,
        "usuario_id": session["usuario_id"]
    }

    Libro.crear(data)

    flash("Libro agregado correctamente")

    return redirect("/libros")


@libros.route("/libros/<int:id>")
def detalle(id):

    if "usuario_id" not in session:
        return redirect("/login")

    libro = Libro.buscar_por_id(id)

    if libro is None:
        flash("El libro no existe")
        return redirect("/libros")

    return render_template(
        "detalle_libro.html",
        libro=libro
    )


@libros.route("/libros/eliminar/<int:id>")
def eliminar(id):

    if "usuario_id" not in session:
        return redirect("/login")

    Libro.eliminar(
        id,
        session["usuario_id"]
    )

    flash("Libro eliminado")

    return redirect("/libros")


@libros.route("/libros/editar/<int:id>")
def editar(id):

    if "usuario_id" not in session:
        return redirect("/login")

    libro = Libro.buscar_por_id(id)

    if libro is None:
        flash("El libro no existe")
        return redirect("/libros")

    if libro["usuario_id"] != session["usuario_id"]:
        flash("No puedes editar este libro")
        return redirect("/libros")

    return render_template(
        "editar_libro.html",
        libro=libro
    )


@libros.route("/libros/actualizar", methods=["POST"])
def actualizar():

    if "usuario_id" not in session:
        return redirect("/login")

    data = {
        "id": request.form["id"],
        "titulo": request.form["titulo"].strip(),
        "autor": request.form["autor"].strip(),
        "genero": request.form["genero"].strip(),
        "fecha_publicacion": request.form["fecha_publicacion"],
        "descripcion": request.form["descripcion"].strip(),
        "usuario_id": session["usuario_id"]
    }

    if len(data["titulo"]) < 2:
        flash("El título debe tener al menos 2 caracteres")
        return redirect("/libros/editar/" + data["id"])

    if len(data["autor"]) < 2:
        flash("El autor debe tener al menos 2 caracteres")
        return redirect("/libros/editar/" + data["id"])

    if data["genero"] == "":
        flash("Debes seleccionar un género")
        return redirect("/libros/editar/" + data["id"])

    if data["fecha_publicacion"] == "":
        flash("Debes ingresar una fecha de publicación")
        return redirect("/libros/editar/" + data["id"])

    if len(data["descripcion"]) < 10:
        flash("La descripción debe tener al menos 10 caracteres")
        return redirect("/libros/editar/" + data["id"])

    Libro.actualizar(data)

    flash("Libro actualizado correctamente")

    return redirect("/libros")