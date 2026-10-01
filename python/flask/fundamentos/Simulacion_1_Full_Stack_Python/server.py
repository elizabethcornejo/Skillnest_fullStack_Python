import os
from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

from flask_app.controllers.usuarios_controller import usuarios
from flask_app.controllers.libros_controller import libros
from flask_app.controllers.favoritos_controller import favoritos

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "clave-secreta")

bcrypt = Bcrypt(app)

app.register_blueprint(usuarios)
app.register_blueprint(libros)
app.register_blueprint(favoritos)

if __name__ == "__main__":
    app.run(debug=True)