"""
Reglas generales de las funciones:
1- No se ejecuta la funcion a menos que la llames
2- La puedo llamar la cantidad de veces que quiera
3- Primero hay que definir la funcion, despues llamarla
4- Primero van los parámetros requeridos, y al final los opcionales
5- Para cambiar el scope de una variable, utilizar return
"""

#FUNCION SIN PARAMETRO
def derechos_humanos():
    print("Derecho a la vida")
    print("Derecho a la propiedad privada")
    print("Derecho a la igualdad ante la ley")

def derechos_mayorEdad():
    print("Derecho a votar")
    print("Derecho a trabajar")

#FUNCION CON PARAMETRO
def mayoría_de_Edad(nombre, edad):
    print(f"Según la edad de {nombre}, sus derechos son:")
    if edad >= 18:
        derechos_humanos()
        derechos_mayorEdad()
    else:
        derechos_humanos()

mayoría_de_Edad('Lucas', 30)
mayoría_de_Edad('Giselle', 32)
mayoría_de_Edad('Priscila', 14)
mayoría_de_Edad(edad= 14, nombre= 'Contract') #Se puede declarar en diferente orden los parametros, pero tenes que declarar argumento y valor asignado

#FUNCION CON PARAMETROS OPCIONALES
def mayoria_de_edad2(edad, nombre='X'):
    print(f'Según la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayorEdad()
    else:
        derechos_humanos()

mayoria_de_edad2(5)

#VARIABLE GLOBAL
def suma(a,b):
    result = a+b
    return result

resultado = suma(5,6)
print('El resultado es',resultado)

def operaciones(a,b):
    suma = a+b
    multiplicacion = a*b
    resta= a-b
    return print(f'El restultado de la suma es {suma},',f'el resultado de la multiplicacion es {multiplicacion},', f'y el resultado de la resta es {resta}')

resultados = operaciones(5,6)
print(resultados)

