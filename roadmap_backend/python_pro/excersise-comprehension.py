number_thing = (number for number in range(1,16) if number % 3 == 0)
print('\nNúmeros del generador múltiplos de 3, del 1 al 15:')
for number in number_thing:
    print(number)