from flask import Blueprint, redirect, session, render_template


from flask_app.models.favorito import Favorito



favoritos = Blueprint(
    "favoritos",
    __name__
)




@favoritos.route("/favorito/<int:id>")
def agregar(id):


    data={


        "usuario_id":session["usuario_id"],

        "libro_id":id

    }



    if not Favorito.existe(data):


        Favorito.agregar(data)



    return redirect(
        f"/libros/{id}"
    )






@favoritos.route("/favoritos")
def mostrar():



    if "usuario_id" not in session:

        return redirect("/login")



    libros = Favorito.mis_favoritos(

        session["usuario_id"]

    )



    return render_template(

        "favoritos.html",

        libros=libros

    )