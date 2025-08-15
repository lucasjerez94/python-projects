# -------------------------- 1 -----------------------------------------
# ¿Qué es una dependencia?
# Una dependencia es cualquier objeto que una clase necesite para hacer su trabajo. Por ejemplo:
"""
class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self):
        self.motor = Motor()  # Aquí el coche crea su propia dependencia
"""    
# En este ejemplo, el coche necesita un motor para funcionar.
#-----------------------------------------------------------------------------------------------------------------------------------


# -------------------------- 2 -----------------------------------------
# Problema sin inyección de dependencias
# Si la clase Coche crea su propio Motor , no puedes cambiar fácilmente el motor por uno diferente (por ejemplo, un motor eléctrico).
#-----------------------------------------------------------------------------------------------------------------------------------


# -------------------------- 3 -----------------------------------------
# Cómo funciona la inyección de dependencias
# Con inyección de dependencias, en lugar de que Coche cree el motor, se lo pasó desde fuera:
class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self, motor):  # Aceptamos el motor como un argumento
        self.motor = motor
    
    def arrancar(self):
        self.motor.encender()
# Ahora puedes usar Coche con cualquier motor que quieras:

# Creamos un motor
motor_normal = Motor()

# Pasamos el motor al coche
mi_coche = Coche(motor_normal)
mi_coche.arrancar()
#-----------------------------------------------------------------------------------------------------------------------------------


# -------------------------- 4 -----------------------------------------
# Ventajas
# Flexibilidad : Puedes cambiar fácilmente las dependencias, como cambiar de un motor normal a uno eléctrico.
# Pruebas : Es más fácil probar las clases porque puedes pasar dependencias "falsas" para simular comportamientos.
# Por ejemplo, probando con un motor falso:
class MotorFalso:
    def encender(self):
        print("Motor falso encendido para pruebas")

motor_falso = MotorFalso()
coche_de_pruebas = Coche(motor_falso)
coche_de_pruebas.arrancar()
#-----------------------------------------------------------------------------------------------------------------------------------


# -------------------------- 5 -----------------------------------------
# Inyección con marcos
# En aplicaciones más grandes, se utilizan frameworks que automatizan esta inyección, como FastAPI o Django , donde el framework se encarga de pasar las dependencias correctas a cada clase.

"""
------------ RESUMEN --------------
1. En lugar de crear las dependencias dentro de la clase, las recibes como argumentos.
2. Esto hace que tu código sea más flexible y fácil de probar.
3. Puedes usar herramientas externas para manejarlo automáticamente.
"""




