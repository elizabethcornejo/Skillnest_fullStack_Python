from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = "tasktrack_clave_secreta"

bcrypt = Bcrypt(app)

from flask_app.controllers import usuarios_controller
from flask_app.controllers import tareas_controller
from flask_app.controllers import categorias_controller