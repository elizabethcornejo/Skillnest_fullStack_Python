from flask import Flask, render_template
from controllers.usuarios import registro, login, dashboard, logout


app = Flask(__name__)

app.secret_key = "clave_secreta"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registro", methods=["POST"])
def registrar_usuario():
    return registro()


@app.route("/login", methods=["POST"])
def iniciar_sesion():
    return login()


@app.route("/dashboard")
def mostrar_dashboard():
    return dashboard()


@app.route("/logout")
def cerrar_sesion():
    return logout()


if __name__ == "__main__":
    app.run(debug=True)