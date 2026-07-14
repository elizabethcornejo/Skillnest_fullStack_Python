import sys
import os

# Agrega de forma explícita el directorio de ejecución actual al entorno de Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from usuario import Usuario
except ImportError as e:
    print("\n Error Crítico de Importación:")
    print("No se localizó el archivo 'usuario.py' o la clase 'Usuario'.")
    print(f"Detalle técnico del sistema: {e}")
    sys.exit(1)

# Estado de control de sesión de la aplicación
usuario_activo = None 

while True:
    # =============================================================
    # MENÚ INICIAL: INICIO DE SESIÓN / SALIDA
    # =============================================================
    if usuario_activo is None:
        print("\n==============================")
        print("      SISTEMA DE USUARIOS")
        print("==============================")
        print("1. Iniciar sesión")
        print("2. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            txt_user = input("Usuario: ")
            txt_pass = input("Contraseña: ")
            
            controlador = Usuario()
            usuario_validado = controlador.validar_inicio_sesion(txt_user, txt_pass)
            
            if usuario_validado:
                usuario_activo = usuario_validado
                print(f"\n ¡Inicio de sesión exitoso!")
            else:
                print("\n Usuario o contraseña incorrectos.")
                
        elif opcion == "2":
            print("\nPrograma finalizado de manera correcta.")
            sys.exit()
        else:
            print("\nOpción inválida.")

    # =============================================================
    # MENÚ SECUNDARIO: PANEL EXCLUSIVO PARA ADMINISTRADORES (ADMIN)
    # =============================================================
    elif usuario_activo.tipo == "ADMIN":
        print("\n==============================")
        print(f"Bienvenido Administrador:\n{usuario_activo.usuario}")
        print("==============================")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("6. Cerrar sesión")
        
        opcion = input("\nSeleccione una opción: ")
        dao = Usuario()

        if opcion == "1":
            print("\n--- REGISTRAR NUEVO USUARIO ---")
            user = input("Usuario: ")
            password = input("Contraseña: ")
            tipo = input("Tipo (ADMIN o USER): ").upper()
            
            if tipo in ["ADMIN", "USER"]:
                if dao.crear_usuario(user, password, tipo):
                    print(" Usuario registrado exitosamente.")
            else:
                print(" Tipo de usuario no válido. Use ADMIN o USER.")

        elif opcion == "2":
            print("\n--- LISTADO DE USUARIOS ---")
            usuarios = dao.obtener_listado_usuarios()
            print("ID\tUsuario\t\tTipo")
            print("------------------------------")
            for u in usuarios:
                print(f"{u['id']}\t{u['usuario']}\t\t{u['tipo']}")

        elif opcion == "3":
            print("\n--- BUSCAR USUARIO ---")
            id_buscar = input("Ingrese el ID a buscar: ")
            u = dao.buscar_por_id(id_buscar)
            if u:
                print(f"\n Datos del Usuario:\nID: {u['id']}\nUsuario: {u['usuario']}\nTipo: {u['tipo']}")
            else:
                print(" Usuario no encontrado.")

        elif opcion == "4":
            print("\n--- MODIFICAR USUARIO ---")
            id_mod = input("Ingrese el ID a modificar: ")
            u = dao.buscar_por_id(id_mod)
            if u:
                # Si presionas enter sin escribir nada se conserva el valor original
                nuevo_user = input(f"Nuevo usuario ({u['usuario']}): ") or u['usuario']
                nueva_pass = input("Nueva contraseña: ")
                nuevo_tipo = input(f"Nuevo tipo ADMIN/USER ({u['tipo']}): ").upper() or u['tipo']
                
                if dao.modificar_usuario(id_mod, nuevo_user, nueva_pass, nuevo_tipo):
                    print(" Usuario modificado correctamente.")
            else:
                print(" Usuario no encontrado.")

        elif opcion == "5":
            print("\n--- ELIMINAR USUARIO ---")
            id_elim = input("Ingrese el ID a eliminar: ")
            confirmar = input(f"¿Está seguro de eliminar al ID {id_elim}? (s/n): ").lower()
            if confirmar == 's':
                if dao.eliminar_usuario(id_elim):
                    print(" Usuario eliminado permanentemente.")
                else:
                    print(" No se pudo eliminar (ID inexistente).")

        elif opcion == "6":
            print("\nCerrando sesión de administrador...")
            usuario_activo = None

        else:
            print("\nOpción inválida.")

    # =============================================================
    # MENÚ SECUNDARIO: PANEL LIMITADO PARA USUARIOS COMUNES (USER)
    # =============================================================
    elif usuario_activo.tipo == "USER":
        print("\n==============================")
        print(f"Bienvenido\n\n{usuario_activo.usuario}")
        print("\nTipo de usuario:\nUSER")
        print("==============================")
        print("1. Cerrar sesión")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            print("\nCerrando sesión del usuario...")
            usuario_activo = None
        else:
            print("\nOpción inválida. Los usuarios comunes solo pueden utilizar la opción 1.")