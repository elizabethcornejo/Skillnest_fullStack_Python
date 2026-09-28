from server import app
from flask import render_template, request, redirect
from models.estudiante import Estudiante

@app.route("/")
def inicio():
    return redirect("/lista_estudiantes")

@app.route("/lista_estudiantes")
def lista_estudiantes():
    estudiantes = Estudiante.obtener_todos()
    return render_template("lista_estudiantes.html", estudiantes=estudiantes)

@app.route("/actualizar_estudiante", methods=["POST"])
def actualizar_estudiante():
    datos = {
        "id": request.form["id"],
        "nombre": request.form["nombre"],
        "email": request.form["email"]
    }
    Estudiante.actualizar(datos)
    return redirect("/lista_estudiantes")

@app.route("/eliminar_estudiante/<int:id>")
def eliminar_estudiante(id):
    datos = {"id": id}
    Estudiante.eliminar(datos)
    return redirect("/lista_estudiantes")