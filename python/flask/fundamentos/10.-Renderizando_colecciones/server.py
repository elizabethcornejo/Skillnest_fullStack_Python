from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/videojuegos")
def videojuegos():
    lista_videojuegos = [
        {
            "nombre": "Minecraft",
            "plataforma": "PC",
            "anio": 2011
        },
        {
            "nombre": "Fortnite",
            "plataforma": "PC",
            "anio": 2017
        },
        {
            "nombre": "The Legend of Zelda",
            "plataforma": "Nintendo Switch",
            "anio": 2017
        },
        {
            "nombre": "Grand Theft Auto V",
            "plataforma": "PlayStation 4",
            "anio": 2014
        },
        {
            "nombre": "FIFA 24",
            "plataforma": "PlayStation 5",
            "anio": 2023
        },
        {
            "nombre": "Among Us",
            "plataforma": "PC",
            "anio": 2018
        }
    ]

    return render_template(
        "videojuegos.html",
        videojuegos=lista_videojuegos
    )

if __name__ == "__main__":
    app.run(debug=True)