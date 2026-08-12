from flask import Flask, render_template, request

app = Flask(__name__)

frutas = [
    {
        "nombre": "Manzana",
        "precio": 2.5,
        "imagen": "manzana.jpg",
        "descripcion": "Fruta dulce y crujiente, rica en fibra y vitamina C."
    },
    {
        "nombre": "Plátano",
        "precio": 1.8,
        "imagen": "platano.jpg",
        "descripcion": "Fruta energética rica en potasio, perfecta para deportistas."
    },
    {
        "nombre": "Naranja",
        "precio": 3.0,
        "imagen": "naranja.jpg",
        "descripcion": "Cítrico jugoso con alto contenido de vitamina C y antioxidantes."
    },
    {
        "nombre": "Fresa",
        "precio": 4.5,
        "imagen": "fresa.jpg",
        "descripcion": "Baya dulce y aromática, rica en antioxidantes y vitamina C."
    },
    {
        "nombre": "Uva",
        "precio": 3.8,
        "imagen": "uva.jpg",
        "descripcion": "Fruta pequeña y dulce, ideal para snacks y postres."
    },
    {
        "nombre": "Piña",
        "precio": 5.0,
        "imagen": "piña.jpg",
        "descripcion": "Fruta tropical dulce y ácida, con propiedades antiinflamatorias."
    },
    {
        "nombre": "Sandía",
        "precio": 4.2,
        "imagen": "sandia.jpg",
        "descripcion": "Fruta refrescante, compuesta en un 90% de agua, ideal para el verano."
    },
    {
        "nombre": "Mango",
        "precio": 3.5,
        "imagen": "mango.jpg",
        "descripcion": "Fruta tropical dulce y aromática, rica en vitaminas A y C."
    }
]


@app.route("/")
def index():
    return render_template("index.html", frutas=frutas)


@app.route("/checkout", methods=["POST"])
def checkout():

    nombre = request.form.get("nombre")
    email = request.form.get("email")
    direccion = request.form.get("direccion")

    orden = []
    total_frutas = 0
    total_pagar = 0

    for i, fruta in enumerate(frutas):

        cantidad = int(request.form.get(f"cantidad_{i}", 0))

        if cantidad > 0:

            subtotal = cantidad * fruta["precio"]

            orden.append({
                "nombre": fruta["nombre"],
                "precio": fruta["precio"],
                "cantidad": cantidad,
                "subtotal": subtotal
            })

            total_frutas += cantidad
            total_pagar += subtotal

    return render_template(
        "checkout.html",
        nombre=nombre,
        email=email,
        direccion=direccion,
        orden=orden,
        total_frutas=total_frutas,
        total_pagar=total_pagar
    )


@app.route("/frutas")
def mostrar_frutas():
    return render_template("frutas.html", frutas=frutas)


if __name__ == "__main__":
    app.run(debug=True)