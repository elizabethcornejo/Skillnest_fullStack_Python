from flask import Flask, render_template, request

app = Flask(__name__)

# Base de datos enriquecida
DATOS_PLATAFORMAS = [
    {"id": 1, "nombre": "Spotify", "categoria": "Música", "usuarios": 515, "fundado": 2006, "pais": "Suecia", "estado": "Activo"},
    {"id": 2, "nombre": "Netflix", "categoria": "Streaming", "usuarios": 247, "fundado": 1997, "pais": "EE.UU.", "estado": "Activo"},
    {"id": 3, "nombre": "YouTube", "categoria": "Video", "usuarios": 2500, "fundado": 2005, "pais": "EE.UU.", "estado": "Activo"},
    {"id": 4, "nombre": "Twitch", "categoria": "Streaming", "usuarios": 140, "fundado": 2011, "pais": "EE.UU.", "estado": "Activo"},
    {"id": 5, "nombre": "TikTok", "categoria": "Red Social", "usuarios": 1700, "fundado": 2016, "pais": "China", "estado": "Activo"},
    {"id": 6, "nombre": "Instagram", "categoria": "Red Social", "usuarios": 2350, "fundado": 2010, "pais": "EE.UU.", "estado": "Activo"},
    {"id": 7, "nombre": "Discord", "categoria": "Chat/Comunidad", "usuarios": 250, "fundado": 2015, "pais": "EE.UU.", "estado": "Activo"},
]

@app.route('/tabla')
def mostrar_tabla():
    query = request.args.get('q', '').strip().lower()
    
    # Filtrado básico por servidor (opcional, por si no cargara JS)
    plataformas = DATOS_PLATAFORMAS
    if query:
        plataformas = [
            p for p in DATOS_PLATAFORMAS 
            if query in p['nombre'].lower() or query in p['categoria'].lower() or query in p['pais'].lower()
        ]
        
    # Estadísticas para las tarjetas superiores (Dashboard style)
    total_usuarios = sum(p['usuarios'] for p in DATOS_PLATAFORMAS)
    
    return render_template(
        'tabla.html', 
        plataformas=plataformas, 
        total_usuarios=total_usuarios,
        busqueda=query
    )

if __name__ == '__main__':
    app.run(debug=True)