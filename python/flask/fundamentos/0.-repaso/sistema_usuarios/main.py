from usuario import Usuario


def registrar_usuario():
    print("\nREGISTRAR USUARIO")

    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    print("1. ADMIN")
    print("2. USER")

    opcion = input("Tipo: ")

    if opcion == "1":
        tipo = 1
    elif opcion == "2":
        tipo = 2
    else:
        print("Tipo de usuario incorrecto.")
        return

    nuevo_usuario = Usuario(
        usuario=usuario,
        password=password,
        tipo=tipo
    )

    nuevo_usuario.crear()

    print("Usuario registrado correctamente.")


def listar_usuarios():
    print("\nLISTADO DE USUARIOS")
    print("ID\tUsuario\tTipo")

    usuarios = Usuario.listar()

    for usuario in usuarios:
        print(f"{usuario[0]}\t{usuario[1]}\t{usuario[2]}")


def buscar_usuario():
    print("\nBUSCAR USUARIO")

    id_usuario = input("ID del usuario: ")

    usuario = Usuario.buscar_por_id(id_usuario)

    if usuario:
        print("\nID:", usuario[0])
        print("Usuario:", usuario[1])
        print("Contraseña:", usuario[2])
        print("Tipo:", usuario[3])
    else:
        print("Usuario no encontrado.")


def modificar_usuario():
    print("\nMODIFICAR USUARIO")

    id_usuario = input("ID del usuario: ")

    usuario_actual = Usuario.buscar_por_id(id_usuario)

    if not usuario_actual:
        print("Usuario no encontrado.")
        return

    usuario = input("Nuevo usuario: ")
    password = input("Nueva contraseña: ")

    print("1. ADMIN")
    print("2. USER")

    opcion = input("Nuevo tipo: ")

    if opcion == "1":
        tipo = 1
    elif opcion == "2":
        tipo = 2
    else:
        print("Tipo de usuario incorrecto.")
        return

    usuario_modificado = Usuario(
        id=id_usuario,
        usuario=usuario,
        password=password,
        tipo=tipo
    )

    usuario_modificado.modificar()

    print("Usuario modificado correctamente.")


def eliminar_usuario():
    print("\nELIMINAR USUARIO")

    id_usuario = input("ID del usuario: ")

    usuario = Usuario.buscar_por_id(id_usuario)

    if not usuario:
        print("Usuario no encontrado.")
        return

    Usuario.eliminar(id_usuario)

    print("Usuario eliminado correctamente.")


def menu_admin(usuario):
    while True:
        print("\n==============================")
        print("Bienvenido Administrador:")
        print(usuario[1])
        print("==============================")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("6. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            listar_usuarios()

        elif opcion == "3":
            buscar_usuario()

        elif opcion == "4":
            modificar_usuario()

        elif opcion == "5":
            eliminar_usuario()

        elif opcion == "6":
            print("Sesión cerrada.")
            break

        else:
            print("Opción incorrecta.")


def menu_user(usuario):
    while True:
        print("\n==============================")
        print("Bienvenido")
        print()
        print(usuario[1])
        print()
        print("Tipo de usuario:")
        print(usuario[4])
        print("==============================")
        print("1. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Sesión cerrada.")
            break

        else:
            print("Opción incorrecta.")


def iniciar_sesion():
    print("\nINICIO DE SESIÓN")

    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    resultado = Usuario.validar_login(usuario, password)

    if not resultado:
        print("Usuario o contraseña incorrectos.")
        return

    tipo = resultado[4]

    if tipo == "ADMIN":
        menu_admin(resultado)
    else:
        menu_user(resultado)


def menu_principal():
    while True:
        print("\n==============================")
        print("  SISTEMA DE USUARIOS")
        print("==============================")
        print("1. Iniciar sesión")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()

        elif opcion == "2":
            print("Programa finalizado.")
            break

        else:
            print("Opción incorrecta.")


menu_principal()