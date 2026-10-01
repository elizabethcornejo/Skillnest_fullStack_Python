from flask import Blueprint, render_template, redirect, session, request, flash
from flask_app.models.favorito import Favorito
from flask_app.models.libro import Libro

favoritos = Blueprint("favoritos", __name__)


@favoritos.route("/favoritos")
def lista():

    if "usuario_id" not in session:
        return redirect("/login")

    mis_favoritos = Favorito.mis_favoritos(
        session["usuario_id"]
    )

    return render_template(
        "favoritos.html",
        favoritos=mis_favoritos
    )


@favoritos.route("/favoritos/<int:libro_id>/toggle", methods=["POST"])
def toggle(libro_id):

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

    if favorito:
        Favorito.eliminar(
            session["usuario_id"],
            libro_id
        )
        flash("Libro eliminado de favoritos")
    else:
        Favorito.agregar(
            session["usuario_id"],
            libro_id
        )
        flash("Libro agregado a favoritos")

    return redirect("/libros/" + str(libro_id))