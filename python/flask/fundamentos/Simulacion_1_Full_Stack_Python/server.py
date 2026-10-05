from flask import Flask
from flask_bcrypt import Bcrypt

from flask_app.controllers.usuarios_controller import usuarios
from flask_app.controllers.libros_controller import libros
from flask_app.controllers.favoritos_controller import favoritos

app = Flask(
    __name__,
    template_folder="flask_app/templates",
    static_folder="flask_app/static"
)

app.secret_key = "bookhub_clave_secreta"

bcrypt = Bcrypt(app)

app.register_blueprint(usuarios)
app.register_blueprint(libros)
app.register_blueprint(favoritos)

if __name__ == "__main__":
    app.run(debug=True)