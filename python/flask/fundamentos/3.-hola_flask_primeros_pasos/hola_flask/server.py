from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola profe!"

@app.route("/nosotros")
def nosotros():
    return "Conocenos un poco mas"

@app.route("/krishna")
def krishna():
    return "¡te amo krishna!"

@app.route("/matias")
def matias():
    return "¡amo mucho al matias!"


if __name__ == "__main__":
    app.run(debug=True)