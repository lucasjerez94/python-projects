def is_even(number):
    return number % 2 == 0

#Llamado a la funcion
lista1 = [ is_even(100) for number in range(1,11)  ]

#Lambda
lista2 = [ (lambda x: x % 2 == 0)(number) for number in range(1,11) ]

print(lista1)
print(lista2)


number_thing = (number for number in range(1,6))

for number in number_thing:
    print(number)


