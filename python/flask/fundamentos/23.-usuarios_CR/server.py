from flask import Flask, render_template, request, redirect
from usuario import Usuario

app = Flask(__name__)

# Esta ruta redirige automáticamente cuando entras a http://127.0.0.1:5000/
@app.route("/")
def index():
    return redirect("/usuarios")

@app.route("/usuarios")
def usuarios():
    todos_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_usuarios)

@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("nuevo_usuario.html")

@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.save(data)
    return redirect("/usuarios")

if __name__ == "__main__":
    app.run(debug=True)