import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Introduce un número entre 1 y 100: "))
        intentos += 1

        if intento < numero_secreto:
            print("Más alto")
        elif intento > numero_secreto:
            print("Más bajo")
        else:
            print(f"¡Correcto! ¡Lo has adivinado en {intentos} intentos!")
            break

adivina_el_numero()
