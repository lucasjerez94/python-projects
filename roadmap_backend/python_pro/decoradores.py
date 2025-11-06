"""
¿Qué es un DECORADOR?
Un decorador en Python es una función que modifica o extiende el comportamiento de otra función, sin cambiar su código original.
Un decorador “envuelve” una función para agregarle algo antes o después de que se ejecute.
"""
#Ejemplo simple

def saludar():
    print('Hola Lucas')

def decorador(funcion_original):
    def nueva_funcion():
        print('----Inicio----')
        funcion_original()
        print('----Final----')
    return nueva_funcion


saludo_mejorado = decorador(saludar)
saludo_mejorado()


print("DIVISION ENTRE EJEMPLO SIMPLE Y FORMA PYTHONICA")

#Forma "Pythonica" usando @
@decorador
def despedir():
    print('Chau Lucas')

despedir()
