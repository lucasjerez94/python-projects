class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True
    def acelerar(self):
        self.acelera = True
    def frenar(self):
        self.frena = True
    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn marcha: ', self.enmarcha, '\nAcelera: ', self.acelera, '\nFrena: ', self.frena)

class Moto(Vehiculos):
    def hacer_pirueta(self):
        if self.enmarcha and self.acelera:
            print('¡La moto está haciendo una pirueta!')
        else:
            print('No se puede hacer una pirueta si la moto no está en marcha y acelerando')

class Auto(Vehiculos):
    def evitar_colision(self):
        if self.enmarcha:
            self.frenar()
            print('El auto frena y evita un choque')
        else:
            print('El auto no freno nunca y choco')











