def agregar_mascota():
    nombre = input("Ingrese el nombre de la mascota").lower().strip()
    tipo = input("Ingrese el tipo de mascota").lower().strip()
    genero = input("Ingrese el sexo de la mascota").lower().strip()
    dueno = input("Ingrese el nombre del dueño").lower().strip()
    nueva_mascota = {
        "nombre": nombre,
        "tipo": tipo,
        "genero": genero,
        "dueno": dueno
    }
    lista_mascotas.append(nueva_mascota)
    print(f"Se agregó {nueva_mascota['nombre'].upper()} a lista de mascotas")


def listas_mascotas():
    if not lista_mascotas:
        print("Lista vacia. No hay mascotas ingresadas")
    else:
        print("-----Lista de mascotas------")
        for i, mascota in enumerate(lista_mascotas, 1):
            print(f"{i}. Nombre: {mascota['nombre'].capitalize()}")
            print(f"{i}. Tipo: {mascota['tipo'].capitalize()}")
            print(f"{i}. Genero: {mascota['genero'].capitalize()}")
            print(f"{i}. Dueño: {mascota['dueno'].capitalize()}")
            print("--------------------")


def eliminar_mascotas():
    encontrado = False
    nombre = input("Ingrese el nombre de la mascota a eliminar: ").lower()
    for mascota in lista_mascotas:
        if mascota["nombre"] == nombre:
            lista_mascotas.remove(mascota)
            print(f"Se ha eliminado la mascota: {mascota['nombre'].capitalize()}")
            encontrado = True
            break

    if encontrado == False:
        print("No se encontró la mascota en la lista")


def buscar_mascotas():
    encontrado = False
    nombre = input("Ingrese el nombre de la mascota a buscar: ").lower()
    for mascota in lista_mascotas:
        if mascota["nombre"] == nombre:
            print("Mascota encontrada: ")
            print(f"Nombre: {mascota['nombre'].capitalize()}")
            print(f"Tipo: {mascota['tipo'].capitalize()}")
            print(f"Genero: {mascota['genero'].capitalize()}")
            print(f"Dueño: {mascota['dueno'].capitalize()}")
            encontrado = True
            break

    if encontrado == False:
        print("La mascota no se ha encontrado en la lista")


def agendar_hora():
    nombre = input("Ingrese el nombre de su mascota").strip().lower()
    existe = False
    for mascota in lista_mascotas:
        if mascota["nombre"] == nombre:
            existe = True
            break
    if existe == False:
        print(f"No se encontró una mascota con el nombre de {nombre.capitalize()} en la lista. Ingreselo a la ficha")

    if existe == True:
        try:
            hora = int(input("Agende su hora (Horario de 8 a 20 horas)"))
            if hora >= 8 and hora <= 20:
                hora_tomada = False
                for h in horas:
                    if h["hora"] == hora:
                        hora_tomada = True
                        break

                if hora_tomada == True:
                    print(f"La hora {hora}:00 ya está agendada. Intente con otra hora")
                else:
                    horas.append({
                        "hora": hora,
                        "nombre": nombre
                    })
                    print(f"Hora {hora}:00 ha sido agendada con éxito")

            else:
                print("Ingrese una hora dentro del horario válido")
        except ValueError:
            print("Ingrese un valor numérico")


def listar_horas_agendadas():
    if not horas:
        print("Aún no hay horas ingresadas")
        return
    else:
        for i in range(len(horas)):
            for j in range(i + 1, len(horas)):
                if horas[i]["hora"] > horas[j]["hora"]:
                    horas[i], horas[j] = horas[j], horas[i]  # intercambia posiciones

    print("----Horas agendadas----")
    for h in horas:
        print(f"{h['hora']}:00 - {h['nombre'].capitalize()}")


def horas_disponibles():
    horas_tomadas = []
    for h in horas:
        horas_tomadas.append(h["hora"])
    # mostrar horas que están disponibles
    print("Horas disponibles (8 a 20 horas)")
    for h in range(8, 21):
        if h not in horas_tomadas:
            print(f"{h}:00")


horas = []
diccionario_animales = {}
lista_mascotas = []

opcion = 0

def menu():
    while True:
        print("Veterinaria Cucho")
        print("1. Agregar Mascota")
        print("2. Listar Mascotas")
        print("3. Eliminar Mascotas")
        print("4. Buscar Mascotas")
        print("5. Agendar hora")
        print("6. Listar horas agendadas")
        print("7. Ver horas disponibles")
        print("8. Salir")

        try:
            opcion = int(input("Ingrese la opción que desea: "))
        except ValueError:
            print("Ingrese un valor numérico.")
            continue

        if opcion == 1:
            funcionesveterianariaclase.agregar_mascota()

        elif opcion == 2:
            funcionesveterianariaclase.listas_mascotas()

        elif opcion == 3:
            funcionesveterianariaclase.eliminar_mascotas()

        elif opcion == 4:
            funcionesveterianariaclase.buscar_mascotas()

        elif opcion == 5:
            funcionesveterianariaclase.agendar_hora()

        elif opcion == 6:
            funcionesveterianariaclase.listar_horas_agendadas()

        elif opcion == 7:
            funcionesveterianariaclase.horas_disponibles()

        elif opcion == 8:
            print("Saliendo del programa")
            break

        else:
            print("Opción no listada")