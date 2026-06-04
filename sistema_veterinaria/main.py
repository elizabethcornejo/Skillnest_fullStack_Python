from persona import persona
from mascota import mascota
from consulta import consulta


while True:

    print("\n===================================")
    print("      SISTEMA VETERINARIA")
    print("===================================")

    print("1. Mostrar consultas")
    print("2. Mostrar mascotas")
    print("3. Mostrar dueños")
    print("4. Registrar dueño")
    print("5. Registrar mascota")
    print("6. Registrar consulta")
    print("7. Buscar mascota")
    print("8. Eliminar mascota")
    print("9. Buscar consulta")
    print("10. Eliminar consulta")
    print("11. Buscar dueño")
    print("12. Eliminar dueño")
    print("13. Salir")

    opcion = input("\nSeleccione una opción: ")

    # MOSTRAR CONSULTAS
    if opcion == "1":
        consulta.listar()

    # MOSTRAR MASCOTAS
    elif opcion == "2":
        mascota.listar()

    # MOSTRAR DUEÑOS
    elif opcion == "3":
        persona.listar()

    # REGISTRAR DUEÑO
    elif opcion == "4":

        nombre = input("Nombre: ")
        email = input("Email: ")
        telefono = input("Telefono: ")
        rut = input("Rut: ")
        comuna = input("Comuna: ")
        calle = input("Calle: ")
        numero = input("Numero residencia: ")

        nuevo_dueno = persona(
            nombre,
            email,
            telefono,
            rut,
            comuna,
            calle,
            numero
        )

        nuevo_dueno.guardar()

    # REGISTRAR MASCOTA
    elif opcion == "5":

        nombre = input("Nombre mascota: ")
        especie = int(input("ID especie: "))
        raza = int(input("ID raza: "))
        sexo = input("Sexo: ")
        fecha_nac = input("Fecha nacimiento (AAAA-MM-DD): ")
        peso = float(input("Peso: "))
        dueno = int(input("ID dueño: "))

        nueva_mascota = mascota(
            nombre,
            especie,
            raza,
            sexo,
            fecha_nac,
            peso,
            dueno
        )

        nueva_mascota.guardar()

    # REGISTRAR CONSULTA
    elif opcion == "6":

        motivo = input("Motivo consulta: ")
        anamnesis = input("Anamnesis: ")
        tipo_consulta = int(input("ID tipo consulta: "))
        mascota_id = int(input("ID mascota: "))

        nueva_consulta = consulta(
            motivo,
            anamnesis,
            tipo_consulta,
            mascota_id
        )

        nueva_consulta.guardar()

    # BUSCAR MASCOTA
    elif opcion == "7":
        mascota.buscar()

    # ELIMINAR MASCOTA
    elif opcion == "8":
        mascota.eliminar()

    # BUSCAR CONSULTA
    elif opcion == "9":
        consulta.buscar()

    # ELIMINAR CONSULTA
    elif opcion == "10":
        consulta.eliminar()

    # BUSCAR DUEÑO
    elif opcion == "11":
        persona.buscar()

    # ELIMINAR DUEÑO
    elif opcion == "12":
        persona.eliminar()

    # SALIR
    elif opcion == "13":
        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpción inválida.")