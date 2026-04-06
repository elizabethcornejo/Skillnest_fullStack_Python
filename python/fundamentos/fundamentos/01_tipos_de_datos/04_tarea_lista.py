'''
Actividad: Gestor deinventario

'''

'''
1- Creacion: Crear una lista llamada inventario que contenga lo siguiente 
articulos: "laptop", "raton", "monitor", "cable hdmi"
'''
inventario = ['laptop', 'raton', 'monitor', 'cable hdmi']
'''
2.- Expansion: Utiliza el metodo correspondiente para agregar "impresora" y "teclado"
al final de la lista
'''
inventario.append("impresora")
inventario.append("teclado")
'''
3.- Conteo:Utiliza la funcion integrada para mostrar cuantos elementos 
totales hay en la lista.
''' 
print(len(inventario)) 
'''
4.- Acceso y modificacion: Modifica "teclado" por "teclado mecanico"
'''
inventario[5] = "teclado mecanico "
'''
5.- Slicing: Crear una nuev lista llamada "promocion",debe contener solo los tres primeros 
elementos de la lista "inventario".
'''
promocion = inventario
print(f"5.-Lista promocio:{promocion[:4]}") 
'''
6.- Mostrar la lista de inventario ordenado alfabeticamente.
'''
inventario.sort()
print(inventario)
'''
7.- Elimina el ultimo elemento de la lista inventario mostrando elemento 
eliminado y las lista final
'''
eliminado = inventario.pop()

print("articulo eliminado", eliminado)
print(inventario)