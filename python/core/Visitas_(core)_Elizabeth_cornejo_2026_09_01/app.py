from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# La clave secreta es indispensable para poder usar session
app.secret_key = 'clave_secreta_super_segura'


@app.route('/')
def index():
    # Inicializar el contador de visitas si no existe en la sesión
    if 'visitas' not in session:
        session['visitas'] = 0

    # Incrementar las visitas en 1 por cada recarga/visita normal
    session['visitas'] += 1

    # Inicializar el contador de reinicios si no existe
    if 'reinicios' not in session:
        session['reinicios'] = 0

    return render_template('index.html', visitas=session['visitas'], reinicios=session['reinicios'])


@app.route('/aumentar_dos', methods=['POST'])
def aumentar_dos():
    # Al sumar 2 en esta ruta, contrarrestamos o sumamos sobre la visita de la ruta raíz.
    # Como la redirección a '/' sumará +1, agregamos +1 aquí para completar un incremento de +2.
    if 'visitas' in session:
        session['visitas'] += 1
    return redirect('/')


@app.route('/incrementar_personalizado', methods=['POST'])
def incrementar_personalizado():
    # BONUS ORO: Obtener el número ingresado por el usuario
    cantidad = request.form.get('cantidad', type=int)
    if cantidad and 'visitas' in session:
        # Se resta 1 porque al redirigir a '/' se volverá a sumar +1 de la visita normal
        session['visitas'] += (cantidad - 1)
    return redirect('/')


@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    # BONUS PLATA Y ORO: Reiniciar el contador de visitas e incrementar el historial de reinicios
    session['visitas'] = 0
    if 'reinicios' in session:
        session['reinicios'] += 1
    else:
        session['reinicios'] = 1
    return redirect('/')


@app.route('/destruir_sesion')
def destruir_sesion():
    # Eliminar toda la información guardada en la sesión
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)