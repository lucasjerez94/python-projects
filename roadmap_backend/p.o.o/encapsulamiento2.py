class Perro:
    def __init__(self, nombre, raza, color):
        self.nombre = nombre
        self.raza = raza
        self.__color = color

    def get_nombre(self):
        return self.nombre

    def get_raza(self):
        return self.raza

    def get_color(self):
        return self.__color

    def set_color(self, nuevo_color):
        colores_validos = ['Blanco', 'Negro', 'Marron', 'Gris', 'Dorado']
        nuevo_color = nuevo_color.strip().capitalize()

        if not nuevo_color.isalpha():
            print('❌ El color no debe contener números ni símbolos.')
            return False
        elif nuevo_color not in colores_validos:
            print(f'❌ "{nuevo_color}" no es un color permitido. Usá uno de estos: {", ".join(colores_validos)}')
            return False
        else:
            self.__color = nuevo_color
            print(f'✅ Color actualizado correctamente a: {self.__color}')
            return True

    def mostrar_info(self):
        print(f'{self.nombre}, de raza {self.raza}, tiene color {self.__color}')


dog = Perro('Facha', 'Dogo Argentino', 'Blanco')

name_dog = dog.get_nombre()

dog.set_color('azul')
dog.set_color('55')

new_color = 'Marron'
color_anterior = dog.get_color()
cambio_exitoso = dog.set_color(new_color)

if cambio_exitoso:
    print(f'El color anterior de {name_dog} era el color {color_anterior}. Pero ahora, su color actual es {dog.get_color()}')






















