# Diccionario en python 

estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
# imprimir elnombre de estudiante 
print(estudiante["nombre"])

estudiante["nombre"] = "Vicente"
print(estudiante["nombre"])

estudiante["nombre"] = "Elizabeth"
print(estudiante["nombre"])


paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PR"] = "Peru"
print(paises)


# esunacondicion para buscar elemento e inserta si no existe 
if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
   print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
   paises["CRI"] = "Costa Rica"

      #Elimina valores de el diccionario 
      print(paises)
      valor_removido = paises.pop("MEX") #Elimina elemntos y devulve su valor 
      print(f"Valor removido: {valor_removido}")
      del paises ["COL"] # Elimina el elemento 
      print(paises) #imprime ["CHL"] = "Chile"

      #diccionario pintor

      pintor = { "nombre": "Frida Kahlo", "pais": "México", "fecha_nacimiento": "6 de julio de 1907"}

# diccionario pintor multitendia 
      pintor = {
   "nombre": "Frida Kahlo",
   "pais": "México",
   "fecha_nacimiento": "6 de julio de 1907"
}
# diccionarios anidados
escuela = {
   "nombre": "Coding Dojo LATAM",
   "profesores": [
         {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
         {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
         {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
   ]
}

