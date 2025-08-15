class Perro:
    def __init__(self, n, r, c, edad=0):
        self.nombre = n
        self.raza = r
        self.color = c
        self.tamaño = None
        self.edad = edad

    def ladrar(self):
        print(f'{self.nombre} está ladrando')

    def mostrar_raza(self):
        print(f'{self.nombre} pertenece a la raza {self.raza}')

    def mostrar_edad(self):
        print(f'{self.nombre} tiene {self.edad} años')

    def mostrar_color(self):
        print(f'{self.nombre}, que es de raza {self.raza}, tiene como color dominante el {self.color}')

    def cumpleaños(self):
        self.edad += 1
        print(f'{self.nombre} ahora tiene {self.edad} años')

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre.capitalize()
        print('✅ Nuevo nombre asignado:', self.nombre)

class Gato:
    def __init__(self, n, t, c, edad=0):
        self.nombre = n
        self.tamaño = t
        self.color = c
        self.edad = edad

    def set_edad(self, edad):
        self.edad = edad
        print(f'{self.nombre} tiene {self.edad} años de edad')

    def mostrar_edad(self):
        print(f'{self.nombre} tiene {self.edad} años')

    def pedirComida(self):
        print(f'{self.nombre}, que es de tamaño {self.tamaño} y de color {self.color}, vive pidiendo comida')

    def cumpleaños(self):
        self.edad += 1
        print(f'{self.nombre}, ahora tiene un año más de vida, por lo tanto tiene {self.edad} años')
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre.capitalize()
        print('✅ Nuevo nombre asignado:', self.nombre)


# ---------- LÓGICA DEL PROGRAMA ----------

#1. Crea una instancia de Gato y otra de Perro con valores predeterminados
cat = Gato('Zimba','pequeño','Gris',edad = 5)
dog = Perro('Facha','Dogo Argentino','Blanco', edad = 3)

#2. Simula un paso del tiempo en bucle (for o while) donde en cada ciclo el gato cumple años y pide comida y el perro ladra
for year in range(1,4):
    cat.cumpleaños()
    cat.pedirComida()
    dog.cumpleaños()
    dog.ladrar()

#3. Luego de 3 años: mostra la edad final de ambos animales y permiti cambiar el nombre de uno de los 2 usando imput
cat.mostrar_edad()
dog.mostrar_edad()

while True:
    respuesta = input('¿Desea cambiar el nombre de alguno de los animales? (gato / perro / no): ').strip().lower()
    
    if respuesta == 'gato':
        nuevo_nombre = input('Ingrese el nuevo nombre para el gato: ').strip().capitalize()
        cat.cambiar_nombre(nuevo_nombre)
        break
    
    elif respuesta == 'perro':
        nuevo_nombre = input('Ingrese el nuevo nombre para el perro: ').strip().capitalize()
        dog.cambiar_nombre(nuevo_nombre)
        break
    
    elif respuesta == 'no':
        print('No se modifica el nombre de ningún animal.')
        break

    else:
        print('❌ Opción inválida. Por favor, escriba "gato", "perro" o "no".')
        








