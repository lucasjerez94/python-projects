#- Crea un generador que produzca los números impares del 1 al 10, y recórralo con un for.

def generador_impares():
    for numbers in range(1,11):
            if numbers % 2 != 0:
                yield numbers

impares = generador_impares()
for numero in impares:
     print(numero)



