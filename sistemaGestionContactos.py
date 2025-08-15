agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print("Contacto agregado.")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado.")
    else:
        print("El contacto no existe en la agenda.")

def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"Teléfono de {nombre}: {agenda[nombre]}")
    else:
        print("El contacto no existe en la agenda.")

while True:
    print("\nAgenda de Contactos")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        agregar_contacto(nombre, telefono)
    elif opcion == '2':
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        eliminar_contacto(nombre)
    elif opcion == '3':
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        buscar_contacto(nombre)
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
