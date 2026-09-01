from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ==========================================
# 1. RUTA PRINCIPAL (Formulario)
# ==========================================
@app.route("/")
def index():
    return render_template("index.html")

# ==========================================
# 2. PROCESAR FORMULARIO (POST)
# ==========================================
@app.route("/registrar", methods=["POST"])
def registrar():
    # Obtener los datos del formulario
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    # Imprimir en la terminal
    print("============================")
    print("Producto recibido")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Categoría: {categoria}")
    print("============================")

    # Redireccionar usando url_for para mayor seguridad en la ruta
    return redirect(url_for("resultado"))

# ==========================================
# 3. MOSTRAR RESULTADO (GET)
# ==========================================
@app.route("/resultado")
def resultado():
    # request.form estará vacío aquí porque es una nueva solicitud GET
    return render_template("resultado.html")

# ==========================================
# 4. DESAFÍO ADICIONAL: RUTA DE AYUDA (GET)
# ==========================================
@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")

if __name__ == "__main__":
    app.run(debug=True)