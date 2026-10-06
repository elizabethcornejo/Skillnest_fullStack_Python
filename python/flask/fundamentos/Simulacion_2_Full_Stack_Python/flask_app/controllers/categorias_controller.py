from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import flash

from flask_app import app
from flask_app.models.categoria import Categoria


def usuario_actual():
    return session.get("usuario_id")


@app.route("/categorias")
def categorias():
    if not usuario_actual():
        return redirect("/")

    categorias = Categoria.todas(usuario_actual())

    if categorias is None:
        categorias = []

    return render_template(
        "categorias.html",
        categorias=categorias
    )


@app.route("/categorias/nueva")
def nueva_categoria():
    if not usuario_actual():
        return redirect("/")

    categoria = {}

    return render_template(
        "categoria_form.html",
        categoria=categoria,
        solo_ver=False
    )


@app.route("/categorias/crear", methods=["POST"])
def crear_categoria():
    if not usuario_actual():
        return redirect("/")

    nombre = request.form["nombre"].strip()

    if nombre == "":
        flash(
            "El nombre de la categoría es obligatorio.",
            "danger"
        )
        return redirect("/categorias/nueva")

    datos = {
        "nombre": nombre,
        "usuario_id": usuario_actual()
    }

    try:
        Categoria.crear(datos)

        flash(
            "Categoría creada correctamente.",
            "success"
        )

    except Exception:
        flash(
            "La categoría ya existe.",
            "danger"
        )

    return redirect("/categorias")


@app.route("/categorias/<int:id>")
def ver_categoria(id):
    if not usuario_actual():
        return redirect("/")

    categoria = Categoria.obtener(
        id,
        usuario_actual()
    )

    if not categoria:
        flash(
            "La categoría no existe.",
            "danger"
        )
        return redirect("/categorias")

    return render_template(
        "categoria_form.html",
        categoria=categoria,
        solo_ver=True
    )


@app.route("/categorias/<int:id>/editar")
def editar_categoria(id):
    if not usuario_actual():
        return redirect("/")

    categoria = Categoria.obtener(
        id,
        usuario_actual()
    )

    if not categoria:
        flash(
            "La categoría no existe.",
            "danger"
        )
        return redirect("/categorias")

    return render_template(
        "categoria_form.html",
        categoria=categoria,
        solo_ver=False
    )


@app.route(
    "/categorias/<int:id>/actualizar",
    methods=["POST"]
)
def actualizar_categoria(id):
    if not usuario_actual():
        return redirect("/")

    nombre = request.form["nombre"].strip()

    if nombre == "":
        flash(
            "El nombre de la categoría es obligatorio.",
            "danger"
        )
        return redirect(
            f"/categorias/{id}/editar"
        )

    categoria = Categoria.obtener(
        id,
        usuario_actual()
    )

    if not categoria:
        flash(
            "La categoría no existe.",
            "danger"
        )
        return redirect("/categorias")

    datos = {
        "id": id,
        "nombre": nombre,
        "usuario_id": usuario_actual()
    }

    try:
        Categoria.actualizar(datos)

        flash(
            "Categoría actualizada correctamente.",
            "success"
        )

    except Exception:
        flash(
            "No se pudo actualizar la categoría.",
            "danger"
        )

    return redirect("/categorias")


@app.route(
    "/categorias/<int:id>/eliminar",
    methods=["POST"]
)
def eliminar_categoria(id):
    if not usuario_actual():
        return redirect("/")

    categoria = Categoria.obtener(
        id,
        usuario_actual()
    )

    if not categoria:
        flash(
            "La categoría no existe.",
            "danger"
        )
        return redirect("/categorias")

    try:
        Categoria.eliminar(
            id,
            usuario_actual()
        )

        flash(
            "Categoría eliminada correctamente.",
            "success"
        )

    except Exception:
        flash(
            "No puedes eliminar una categoría que tiene tareas.",
            "danger"
        )

    return redirect("/categorias")