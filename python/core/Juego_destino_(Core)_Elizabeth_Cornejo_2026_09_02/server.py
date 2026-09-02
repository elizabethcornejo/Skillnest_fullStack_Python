import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# Clave secreta necesaria para cifrar las cookies de sesión
app.secret_key = "clave_secreta_super_segura_para_el_destino"

# Lista de posibles predicciones generales
PREDICCIONES = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Un viaje inesperado te abrirá nuevas puertas y perspectivas. Prepárate para la aventura.",
    "Un gran logro profesional tocará a tu puerta muy pronto. Tu esfuerzo será recompensado.",
    "La fortuna sonreirá a todos tus proyectos este año. Es el momento de emprender.",
    "Descubrirás un talento oculto que cambiará el rumbo de tu vida para mejor.",
    "Una amistad del pasado reaparecerá para traerte una noticia muy positiva."
]

# Definiciones de colores (para mostrar el punto de color y el significado)
MAPA_COLORES = {
    'rojo': {'css': 'red', 'significado': 'pasión y energía'},
    'azul': {'css': 'blue', 'significado': 'calma y sabiduría'},
    'verde': {'css': 'green', 'significado': 'misterio y descubrimiento'},
    'amarillo': {'css': 'yellow', 'significado': 'optimismo y creatividad'},
    'morado': {'css': 'purple', 'significado': 'espiritualidad y poder'},
    'naranja': {'css': 'orange', 'significado': 'entusiasmo y éxito'}
}

# Definiciones de animales (para el ícono y el significado)
MAPA_ANIMALES = {
    'perro': {'icono': '🐶', 'significado': 'lealtad y protección'},
    'gato': {'icono': '🐱', 'significado': 'independencia y misterio'},
    'águila': {'icono': '🦅', 'significado': 'visión y libertad'},
    'león': {'icono': '🦁', 'significado': 'fuerza y coraje'},
    'delfín': {'icono': '🐬', 'significado': 'inteligencia y comunicación'},
    'búho': {'icono': '🦉', 'significado': 'sabiduría y conocimiento'}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    # Capturar datos del formulario y limpiar espacios en blanco
    nombre = request.form.get('nombre', '').strip()
    edad = request.form.get('edad', '').strip()
    color_fav = request.form.get('color', '').strip().lower()
    animal_fav = request.form.get('animal', '').strip().lower()

    # Validación básica (redirigir si falta algún dato)
    if not (nombre and edad and color_fav and animal_fav):
        return redirect(url_for('index'))

    # Almacenar datos en la sesión
    session['nombre'] = nombre
    session['edad'] = edad
    session['color_fav'] = color_fav
    session['animal_fav'] = animal_fav
    # Generar un número de la suerte aleatorio (1-100)
    session['numero_suerte'] = random.randint(1, 100)

    # Redirección mediante Pattern POST/Redirect/GET (PRG)
    return redirect(url_for('futuro'))

@app.route('/futuro')
def futuro():
    # Verificar que existen datos esenciales en sesión
    if 'nombre' not in session:
        return redirect(url_for('index'))

    # Recuperar datos de sesión
    nombre = session.get('nombre')
    edad = session.get('edad')
    color_input = session.get('color_fav')
    animal_input = session.get('animal_fav')
    numero_suerte = session.get('numero_suerte')

    # Obtener datos procesados para Color y Animal
    color_data = MAPA_COLORES.get(color_input, {'css': 'gray', 'significado': 'lo desconocido'})
    animal_data = MAPA_ANIMALES.get(animal_input, {'icono': '🐾', 'significado': 'un camino único'})

    # Seleccionar una predicción general aleatoria
    prediccion_general = random.choice(PREDICCIONES)

    # Preparar el texto de la edad
    try:
        edad_int = int(edad)
        # Puedes añadir lógica aquí para diferentes rangos de edad si lo deseas
        texto_edad = f"A tus {edad_int} años, estás en un momento favorable para aprovechar nuevas oportunidades."
    except ValueError:
        texto_edad = "En este momento de tu vida, estás en un momento favorable para aprovechar nuevas oportunidades."

    return render_template(
        'futuro.html',
        nombre=nombre,
        color_fav=color_input,
        color_data=color_data,
        animal_fav=animal_input,
        animal_data=animal_data,
        numero_suerte=numero_suerte,
        prediccion_general=prediccion_general,
        texto_edad=texto_edad
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)