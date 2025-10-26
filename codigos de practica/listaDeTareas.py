lista_tareas = []

def agregar_tarea():
    tarea = input("Ingrese la tarea: ")
    lista_tareas.append(tarea)
    print("Tarea agregada.")

def eliminar_tarea():
    if lista_tareas:
        print("Lista de tareas:")
        for i, tarea in enumerate(lista_tareas):
            print(f"{i + 1}. {tarea}")
        indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
        if 0 <= indice < len(lista_tareas):
            tarea_eliminada = lista_tareas.pop(indice)
            print(f"Tarea eliminada: {tarea_eliminada}")
        else:
            print("Número de tarea no válido.")
    else:
        print("No hay tareas en la lista.")

def mostrar_tareas():
    if lista_tareas:
        print("Lista de tareas:")
        for i, tarea in enumerate(lista_tareas):
            print(f"{i + 1}. {tarea}")
    else:
        print("No hay tareas en la lista.")

while True:
    print("\nLista de Tareas")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_tarea()
    elif opcion == '2':
        eliminar_tarea()
    elif opcion == '3':
        mostrar_tareas()
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
