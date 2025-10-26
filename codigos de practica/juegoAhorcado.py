import random

def obtener_palabra_aleatoria():
    palabras = ["python", "programacion", "codigo", "computadora", "juego", "desarrollo"]
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra
        else:
            progreso += "_"
    return progreso

def jugar_ahorcado():
    palabra = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos_maximos = 6
    intentos = 0

    print("¡Bienvenido al juego del ahorcado!")
    print("Adivina la palabra. Tienes", intentos_maximos, "intentos.")

    while True:
        print("\nPalabra:", mostrar_progreso(palabra, letras_adivinadas))
        letra = input("Ingrese una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
        elif letra in palabra:
            letras_adivinadas.append(letra)
            if mostrar_progreso(palabra, letras_adivinadas) == palabra:
                print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
                break
        else:
            intentos += 1
            print("Incorrecto. Te quedan", intentos_maximos - intentos, "intentos.")
            if intentos == intentos_maximos:
                print("¡Oh no! ¡Te has quedado sin intentos!")
                print("La palabra era:", palabra)
                break

jugar_ahorcado()
