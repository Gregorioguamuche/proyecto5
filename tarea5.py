cursos = []
historial_eliminados = []  # Pila (último eliminado)
cursos_revision = []       # Cola (para revisión)

def agregar_curso():
    nombre = input("Nombre del curso: ")
    if nombre == "":
        print("¡Debes escribir un nombre!\n")
        return
    try:
        nota = float(input("Nota (0 a 100): "))
        if nota < 0 or nota > 100:
            print("¡La nota debe estar entre 0 y 100!\n")
            return
    except:
        print("¡Eso no es un número!\n")
        return
    cursos.append([nombre, nota])
    print(f"Curso '{nombre}' guardado con nota {nota}\n")

    # Si la nota es baja, se agrega a revisión
    if nota < 60:
        cursos_revision.append(nombre)
        print(f"Curso '{nombre}' agregado a revisión por nota baja.\n")

def ver_cursos():
    if not cursos:
        print("No tienes cursos todavía\n")
    else:
        for i, curso in enumerate(cursos):
            print(f"{i+1}. {curso[0]}: {curso[1]}")
    print()

def calcular_promedio():
    if not cursos:
        print("No tienes cursos para calcular promedio\n")
    else:
        total = sum(curso[1] for curso in cursos)
        promedio = total / len(cursos)
        print(f"Tu promedio es: {promedio:.1f}\n")

def buscar_curso():
    if not cursos:
        print("No tienes cursos para buscar\n")
        return
    buscar = input("Nombre del curso a buscar: ")
    for curso in cursos:
        if curso[0].lower() == buscar.lower():
            print(f"Encontrado: {curso[0]} - Nota: {curso[1]}\n")
            return
    print("No se encontró ese curso\n")

def eliminar_curso():
    if not cursos:
        print("No hay cursos para eliminar\n")
        return
    eliminar = input("Nombre del curso a eliminar: ")
    for i in range(len(cursos)):
        if cursos[i][0].lower() == eliminar.lower():
            eliminado = cursos.pop(i)
            historial_eliminados.append(eliminado)  # Se guarda en pila
            print(f"Curso '{eliminar}' eliminado y guardado en historial\n")
            return
    print("No se encontró ese curso\n")

def ver_historial():
    if not historial_eliminados:
        print("No hay historial de cursos eliminados\n")
    else:
        print("Historial de cursos eliminados (último eliminado primero):")
        for curso in reversed(historial_eliminados):
            print(f"- {curso[0]}: {curso[1]}")
    print()

def ver_revision():
    if not cursos_revision:
        print("No hay cursos en la cola de revisión\n")
    else:
        print("Cursos en revisión (nota menor a 60):")
        for curso in cursos_revision:
            print(f"- {curso}")
    print()

def ordenar_por_nombre():
    # Orden burbuja por nombre
    n = len(cursos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cursos[j][0].lower() > cursos[j + 1][0].lower():
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    print("Cursos ordenados alfabéticamente (burbuja)\n")

def ordenar_por_nota():
    # Orden por inserción
    for i in range(1, len(cursos)):
        clave = cursos[i]
        j = i - 1
        while j >= 0 and cursos[j][1] > clave[1]:
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = clave
    print("Cursos ordenados por nota (inserción)\n")

# Menú principal
while True:
    print("1. Agregar curso")
    print("2. Ver cursos")
    print("3. Calcular promedio")
    print("4. Buscar curso")
    print("5. Eliminar curso")
    print("6. Ver historial de eliminados (Pila)")
    print("7. Ver cursos en revisión (Cola)")
    print("8. Ordenar cursos por nombre (Burbuja)")
    print("9. Ordenar cursos por nota (Inserción)")
    print("10. Salir")
    opcion = input("Elige una opción: ")
    print()
    
    if opcion == "1":
        agregar_curso()
    elif opcion == "2":
        ver_cursos()
    elif opcion == "3":
        calcular_promedio()
    elif opcion == "4":
        buscar_curso()
    elif opcion == "5":
        eliminar_curso()
    elif opcion == "6":
        ver_historial()
    elif opcion == "7":
        ver_revision()
    elif opcion == "8":
        ordenar_por_nombre()
    elif opcion == "9":
        ordenar_por_nota()
    elif opcion == "10":
        print("¡saliendo del programa!")
        break
    else:
        print("Opción no válida\n")
