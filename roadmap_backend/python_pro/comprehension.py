# Función para determinar si un número es par
def is_even(number: int) -> bool:
    return number % 2 == 0

# ✅ List comprehension con función normal
# Aplica is_even() a cada número del 1 al 10
lista1 = [is_even(number) for number in range(1, 11)]

# ✅ List comprehension con función lambda
# Hace lo mismo que arriba, pero sin definir la función aparte
lista2 = [(lambda x: x % 2 == 0)(number) for number in range(1, 11)]

# ✅ Mostrar resultados
print(f'Lista 1 (con función): {lista1}')
print(f'Lista 2 (con lambda):  {lista2}')

# ✅ Generador
# Crea un generador que produce los números del 1 al 5
number_thing = (number for number in range(1, 6))

print('\nNúmeros del generador:')
for number in number_thing:
    print(number)


