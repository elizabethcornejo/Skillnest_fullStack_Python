from flask import Blueprint, render_template, redirect, request, session, flash
from flask_app.models.libro import Libro
from flask_app.models.favorito import Favorito

libros = Blueprint("libros", __name__)


@libros.route("/libros")
def lista_libros():

    if "usuario_id" not in session:
        return redirect("/login")

    mis_libros = Libro.mis_libros(session["usuario_id"])
    todos_libros = Libro.todos()

    return render_template(
        "libros.html",
        mis_libros=mis_libros,
        todos_libros=todos_libros
    )


@libros.route("/libros/nuevo", methods=["GET", "POST"])
def nuevo():

    if "usuario_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        datos = {
            "titulo": request.form["titulo"],
            "autor": request.form["autor"],
            "genero": request.form["genero"],
            "fecha_publicacion": request.form["fecha_publicacion"],
            "descripcion": request.form["descripcion"],
            "usuario_id": session["usuario_id"]
        }

        if not datos["titulo"] or not datos["autor"]:
            flash("Completa los campos obligatorios")
            return redirect("/libros/nuevo")

        Libro.crear(datos)

        flash("Libro creado correctamente")
        return redirect("/libros")

    return render_template("nuevo_libro.html")


@libros.route("/libros/<int:libro_id>")
def detalle(libro_id):

    if "usuario_id" not in session:
        return redirect("/login")

    libro = Libro.buscar_por_id(libro_id)

    if not libro:
        flash("Libro no encontrado")
        return redirect("/libros")

    favorito = Favorito.existe(
        session["usuario_id"],
        libro_id
    )

    usuarios_favoritos = Favorito.usuarios_del_libro(libro_id)

    return render_template(
        "detalle_libro.html",
        libro=libro,
        favorito=favorito,
        usuarios_favoritos=usuarios_favoritos
    )


@libros.route("/libros/editar/<int:libro_id>", methods=["GET", "POST"])
def editar(libro_id):

    if "usuario_id" not in session:
        return redirect("/login")

    libro = Libro.buscar_por_id(libro_id)

    if not libro:
        flash("Libro no encontrado")
        return redirect("/libros")

    if libro["usuario_id"] != session["usuario_id"]:
        flash("No puedes editar este libro")
        return redirect("/libros")

    if request.method == "POST":

        datos = {
            "titulo": request.form["titulo"],
            "autor": request.form["autor"],
            "genero": request.form["genero"],
            "fecha_publicacion": request.form["fecha_publicacion"],
            "descripcion": request.form["descripcion"]
        }

        Libro.actualizar(libro_id, session["usuario_id"], datos)

        flash("Libro actualizado correctamente")
        return redirect("/libros/" + str(libro_id))

    return render_template(
        "editar_libro.html",
        libro=libro
    )


@libros.route("/libros/eliminar/<int:libro_id>", methods=["POST"])
def eliminar(libro_id):

    if "usuario_id" not in session:
        return redirect("/login")

    Libro.eliminar(
        libro_id,
        session["usuario_id"]
    )

    flash("Libro eliminado correctamente")

    return redirect("/libros")