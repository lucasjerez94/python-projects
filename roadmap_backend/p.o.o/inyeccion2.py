"""
class Bateria:
    def encender(self):
        print("Batería encendida")

class Celular:
    def __init__(self,bateria):
        self.bateria = bateria

    def prender(self):
        self.bateria.encender()
        print("El celular esta encendido")

bateria_real = Bateria()

mi_celular = Celular(bateria_real)
mi_celular.prender()
"""

class MotorGasolina:
    def encender(self):
        print("Motor de gasolina encendido")
class MotorElectrico:
    def encender(self):
        print("Motor electrico encendido")

class Coche:
    def __init__(self,motor):
        self.motor = motor
    
    def arrancar(self):
        self.motor.encender()

# Crear motores diferentes
motor_gas = MotorGasolina()
motor_elec = MotorElectrico()

# Usar el coche con diferentes motores
coche_1 = Coche(motor_gas)
coche_2 = Coche(motor_elec)

coche_1.arrancar()
coche_2.arrancar()