def km_a_millas(km):
    return km * 0.621371

def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

km = float(input("Ingrese la distancia en kilómetros: "))
print("Distancia en millas:", km_a_millas(km))

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(celsius))
