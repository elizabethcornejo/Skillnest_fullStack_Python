import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  # cambia esto si tienes contraseña
        database="veterinaria"
    )
    cursor = conexion.cursor()
    print("Conexión exitosa")

except Exception as e:
    print("Error:", e)