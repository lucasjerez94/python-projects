class Animal:
    def __init__(self):
        self.__edad: int = None
        self.__pelaje: str = None

    # Getters
    def get_edad(self) -> int:
        return self.__edad

    def get_pelaje(self) -> str:
        return self.__pelaje

    # Setters con validación
    def set_edad(self, edad: int) -> bool:
        if isinstance(edad, int) and edad >= 0:
            self.__edad = edad
            return True
        else:
            print("❌ Edad inválida. Debe ser un número entero positivo.")
            return False

    def set_pelaje(self, pelaje: str) -> bool:
        if isinstance(pelaje, str) and pelaje.strip():
            self.__pelaje = pelaje.capitalize()
            return True
        else:
            print("❌ Pelaje inválido. Debe ser una cadena no vacía.")
            return False

    def comer(self):
        print("El animal está comiendo.")

    def reproducirse(self):
        print("El animal se está reproduciendo.")


class Perro(Animal):
    def __init__(self, nombre: str, tamaño: str, raza: str):
        super().__init__()
        if not all(isinstance(val, str) and val.strip() for val in [nombre, tamaño, raza]):
            raise ValueError("Todos los valores deben ser strings no vacíos.")
        self.nombre = nombre.strip().capitalize()
        self.tamaño = tamaño.strip().capitalize()
        self.raza = raza.strip().capitalize()
        self.__color = None

    # Setter de color con validaciones
    def set_color(self, nuevo_color: str) -> bool:
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

    def get_color(self) -> str:
        return self.__color

    def ladrar(self):
        print(f'{self.nombre} está ladrando.')

    def jugar(self):
        print(f'{self.nombre} está jugando.')

    def check_hambre(self, hambre: bool):
        if hambre:
            print(f'{self.nombre} tiene hambre y debería comer.')
            self.comer()
        else:
            print(f'{self.nombre} no está hambriento.')

    def __str__(self) -> str:
        return f'Perro: {self.nombre}, Raza: {self.raza}, Tamaño: {self.tamaño}, Color: {self.__color or "No asignado"}'
    


# ------------------------ Logica de programa ----------------------------

print('PARTE 1 - "Creando perros"')
print('"----- Refugio de animales -----"')
print('A continuación, ingrese los datos de los perros.\n')

refugio = []

def crear_perro(numero: int) -> Perro:
    while True:
        try:
            print(f'\nPerro #{numero}')
            nombre = input('Ingrese el nombre: ').strip().capitalize()
            tamaño = input('Ingrese el tamaño: ').strip().capitalize()
            raza = input('Ingrese la raza: ').strip().capitalize()

            perro = Perro(nombre, tamaño, raza)
            return perro

        except ValueError as e:
            print(f'❌ Error: {e}. Intente nuevamente.\n')


for i in range(1, 3):
    refugio.append(crear_perro(i))

print('\n✅ Perros creados exitosamente!')
for perro in refugio:
    print(perro)


print('\nPARTE 2 - "Configurar atributos"\n')

for perro in refugio:
    print(f"Configurando datos para {perro.nombre}")

    while True:
        try:
            edad = int(input('Ingrese edad: '))
            if perro.set_edad(edad):
                break
        except ValueError:
            print('❌ Debes ingresar un número entero válido.')

    while True:
        pelaje = input('Ingrese tipo de pelaje: ')
        if perro.set_pelaje(pelaje):
            break

    while True:
        color = input('Ingrese color: ')
        if perro.set_color(color):
            break
    
print('\nPARTE 3 - "Acciones con métodos"\n')

print('\n✅ DATOS FINALES DE LOS PERROS:')
for perro in refugio:
    print(perro)

# Preguntar hambre de cada perro
for perro in refugio:
    while True:
        respuesta = input(f'¿{perro.nombre} tiene hambre? (s/n): ').strip().lower()
        if respuesta in ['s', 'n']:
            hambre = (respuesta == 's')
            perro.check_hambre(hambre)
            break
        else:
            print('❌ Respuesta inválida. Por favor, ingresa "s" o "n".')

# Acciones especiales
if len(refugio) >= 1:
    refugio[0].ladrar()

if len(refugio) >= 2:
    refugio[1].jugar()


print('\nPARTE 4 - "BONUS"\n')
print("\n📋 LISTADO FINAL DEL REFUGIO:\n")
for perro in refugio:
    print(perro)

