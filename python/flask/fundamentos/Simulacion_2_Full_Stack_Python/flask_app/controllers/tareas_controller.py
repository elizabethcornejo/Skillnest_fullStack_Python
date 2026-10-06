from datetime import date

from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import flash

from flask_app import app

from flask_app.models.tarea import Tarea
from flask_app.models.categoria import Categoria
from flask_app.models.comentario import Comentario


def usuario_actual():
    return session.get("usuario_id")


@app.route("/dashboard")
def dashboard():
    if not usuario_actual():
        return redirect("/")

    tareas = Tarea.todas_por_usuario(usuario_actual())
    categorias = Categoria.todas(usuario_actual())

    if tareas is None:
        tareas = []

    if categorias is None:
        categorias = []

    pendientes = 0
    progreso = 0
    completadas = 0

    for tarea in tareas:
        if tarea["estado"] == "Pendiente":
            pendientes += 1
        elif tarea["estado"] == "En progreso":
            progreso += 1
        elif tarea["estado"] == "Completada":
            completadas += 1

    resumen = {
        "pendientes": pendientes,
        "progreso": progreso,
        "completadas": completadas,
        "total": len(tareas)
    }

    proximas = []

    for tarea in tareas:
        if tarea["estado"] != "Completada":
            proximas.append(tarea)

    proximas = proximas[:3]

    return render_template(
        "dashboard.html",
        tareas=tareas,
        categorias=categorias,
        resumen=resumen,
        proximas=proximas
    )


@app.route("/tareas/nueva")
def nueva_tarea():
    if not usuario_actual():
        return redirect("/")

    categorias = Categoria.todas(usuario_actual())

    if categorias is None:
        categorias = []

    tarea = {}

    return render_template(
        "tarea_form.html",
        tarea=tarea,
        categorias=categorias
    )


@app.route("/tareas/crear", methods=["POST"])
def crear_tarea():
    if not usuario_actual():
        return redirect("/")

    titulo = request.form["titulo"].strip()
    categoria_id = request.form["categoria_id"]
    prioridad = request.form["prioridad"]
    fecha_limite = request.form["fecha_limite"]
    estado = request.form["estado"]
    descripcion = request.form["descripcion"].strip()

    if titulo == "":
        flash("El título es obligatorio.", "danger")
        return redirect("/tareas/nueva")

    if categoria_id == "":
        flash("Debes seleccionar una categoría.", "danger")
        return redirect("/tareas/nueva")

    if fecha_limite == "":
        flash("La fecha límite es obligatoria.", "danger")
        return redirect("/tareas/nueva")

    if descripcion == "":
        flash("La descripción es obligatoria.", "danger")
        return redirect("/tareas/nueva")

    try:
        fecha = date.fromisoformat(fecha_limite)
    except ValueError:
        flash("La fecha no es válida.", "danger")
        return redirect("/tareas/nueva")

    if fecha < date.today():
        flash("La fecha límite no puede ser anterior a hoy.", "danger")
        return redirect("/tareas/nueva")

    datos = {
        "titulo": titulo,
        "categoria_id": categoria_id,
        "prioridad": prioridad,
        "fecha_limite": fecha_limite,
        "estado": estado,
        "descripcion": descripcion,
        "usuario_id": usuario_actual()
    }

    Tarea.crear(datos)

    flash("Tarea creada correctamente.", "success")

    return redirect("/dashboard")


@app.route("/tareas/<int:id>")
def ver_tarea(id):
    if not usuario_actual():
        return redirect("/")

    tarea = Tarea.obtener(
        id,
        usuario_actual()
    )

    if not tarea:
        flash("La tarea no existe.", "danger")
        return redirect("/dashboard")

    comentarios = Comentario.todos_por_tarea(id)

    if comentarios is None:
        comentarios = []

    return render_template(
        "tarea_detalle.html",
        tarea=tarea,
        comentarios=comentarios
    )


@app.route("/tareas/<int:id>/editar")
def editar_tarea(id):
    if not usuario_actual():
        return redirect("/")

    tarea = Tarea.obtener(
        id,
        usuario_actual()
    )

    if not tarea:
        flash("La tarea no existe.", "danger")
        return redirect("/dashboard")

    categorias = Categoria.todas(
        usuario_actual()
    )

    if categorias is None:
        categorias = []

    return render_template(
        "tarea_form.html",
        tarea=tarea,
        categorias=categorias
    )


@app.route("/tareas/<int:id>/actualizar", methods=["POST"])
def actualizar_tarea(id):
    if not usuario_actual():
        return redirect("/")

    tarea = Tarea.obtener(
        id,
        usuario_actual()
    )

    if not tarea:
        flash("La tarea no existe.", "danger")
        return redirect("/dashboard")

    titulo = request.form["titulo"].strip()
    categoria_id = request.form["categoria_id"]
    prioridad = request.form["prioridad"]
    fecha_limite = request.form["fecha_limite"]
    estado = request.form["estado"]
    descripcion = request.form["descripcion"].strip()

    if titulo == "":
        flash("El título es obligatorio.", "danger")
        return redirect(f"/tareas/{id}/editar")

    if categoria_id == "":
        flash("Debes seleccionar una categoría.", "danger")
        return redirect(f"/tareas/{id}/editar")

    if fecha_limite == "":
        flash("La fecha límite es obligatoria.", "danger")
        return redirect(f"/tareas/{id}/editar")

    if descripcion == "":
        flash("La descripción es obligatoria.", "danger")
        return redirect(f"/tareas/{id}/editar")

    try:
        date.fromisoformat(fecha_limite)
    except ValueError:
        flash("La fecha no es válida.", "danger")
        return redirect(f"/tareas/{id}/editar")

    datos = {
        "id": id,
        "titulo": titulo,
        "categoria_id": categoria_id,
        "prioridad": prioridad,
        "fecha_limite": fecha_limite,
        "estado": estado,
        "descripcion": descripcion,
        "usuario_id": usuario_actual()
    }

    Tarea.actualizar(datos)

    flash("Tarea actualizada correctamente.", "success")

    return redirect(f"/tareas/{id}")


@app.route("/tareas/<int:id>/eliminar", methods=["POST"])
def eliminar_tarea(id):
    if not usuario_actual():
        return redirect("/")

    tarea = Tarea.obtener(
        id,
        usuario_actual()
    )

    if not tarea:
        flash("La tarea no existe.", "danger")
        return redirect("/dashboard")

    Tarea.eliminar(
        id,
        usuario_actual()
    )

    flash("Tarea eliminada correctamente.", "success")

    return redirect("/dashboard")


@app.route("/tareas/<int:id>/completar", methods=["POST"])
def completar_tarea(id):
    if not usuario_actual():
        return redirect("/")

    tarea = Tarea.obtener(
        id,
        usuario_actual()
    )

    if not tarea:
        flash("La tarea no existe.", "danger")
        return redirect("/dashboard")

    Tarea.cambiar_estado(
        id,
        "Completada",
        usuario_actual()
    )

    flash(
        "Tarea marcada como completada.",
        "success"
    )

    return redirect(f"/tareas/{id}")


@app.route(
    "/tareas/<int:id>/comentarios",
    methods=["POST"]
)
def agregar_comentario(id):
    if not usuario_actual():
        return redirect("/")

    tarea = Tarea.obtener(
        id,
        usuario_actual()
    )

    if not tarea:
        flash("La tarea no existe.", "danger")
        return redirect("/dashboard")

    contenido = request.form["contenido"].strip()

    if contenido == "":
        flash(
            "El comentario no puede estar vacío.",
            "danger"
        )
        return redirect(f"/tareas/{id}")

    datos = {
        "contenido": contenido,
        "usuario_id": usuario_actual(),
        "tarea_id": id
    }

    Comentario.crear(datos)

    flash(
        "Comentario agregado correctamente.",
        "success"
    )

    return redirect(f"/tareas/{id}")


@app.route("/tareas/buscar")
def buscar_tareas():
    if not usuario_actual():
        return redirect("/")

    texto = request.args.get("q", "").strip()
    estado = request.args.get("estado", "")

    tareas = Tarea.buscar(
        usuario_actual(),
        texto,
        estado
    )

    categorias = Categoria.todas(
        usuario_actual()
    )

    if tareas is None:
        tareas = []

    if categorias is None:
        categorias = []

    pendientes = 0
    progreso = 0
    completadas = 0

    for tarea in tareas:
        if tarea["estado"] == "Pendiente":
            pendientes += 1
        elif tarea["estado"] == "En progreso":
            progreso += 1
        elif tarea["estado"] == "Completada":
            completadas += 1

    resumen = {
        "pendientes": pendientes,
        "progreso": progreso,
        "completadas": completadas,
        "total": len(tareas)
    }

    proximas = []

    for tarea in tareas:
        if tarea["estado"] != "Completada":
            proximas.append(tarea)

    proximas = proximas[:3]

    return render_template(
        "dashboard.html",
        tareas=tareas,
        categorias=categorias,
        resumen=resumen,
        proximas=proximas
    )