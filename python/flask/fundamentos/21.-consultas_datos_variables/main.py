from flask import Flask, render_template
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    query_select = "SELECT * FROM mascotas WHERE id = %(id)s;"
    datos_select = {
        'id': 1
    }
    
    mascota = connectToMySQL('primera_flask').query_db(query_select, datos_select)
    
    query_update = "UPDATE mascotas SET nombre = %(nombre)s WHERE id = %(id)s;"
    datos_update = {
        'nombre': 'Maria',
        'id': 3
    }
    connectToMySQL('primera_flask').query_db(query_update, datos_update)

    return render_template('index.html', mascota=mascota[0] if mascota else None)

if __name__ == "__main__":
    app.run(debug=True)