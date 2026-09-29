from flask_app import app
from flask_app.controllers import tacos  # Importante para que registe las rutas

if __name__ == "__main__":
    app.run(debug=True)