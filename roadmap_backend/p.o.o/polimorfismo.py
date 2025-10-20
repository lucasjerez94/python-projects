class Auto():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def desplazamiento(self):
        print('Soy un Auto, de la marca: {} y de modelo: {}. Mi desplazamiento es utilizando 4 ruedas'.format(self.marca,self.modelo))

class Moto(Auto):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    def desplazamiento(self):
        print('Soy una Moto, de la marca: {} y de modelo: {}. Mi desplazamiento es utilizando 2 ruedas'.format(self.marca,self.modelo))

class Camion(Auto):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    def desplazamiento(self):
        print('Soy un Camion, de la marca: {} y de modelo: {}. Mi desplazamiento es utilizando 6 ruedas'.format(self.marca,self.modelo))

class Bicicleta(Auto):
    def __init__(self, marca, modelo):
        super().__init__(marca,modelo)
    def desplazamiento(self):
        print("Soy una Bicicleta, de la marca: {} y del modelo {}. Mi desplazamiento es utilizando 2 ruedas y no utilizo combustible.".format(self.marca,self.modelo))

miAuto = Auto('Peugeot','Style')
miMoto = Moto('Honda','Civic')
miCamion = Camion('Trucker','Speed')
miBici = Bicicleta('Mountainback', 'Small')

vehiculos = [miAuto, miMoto, miCamion, miBici]

for vehiculo in vehiculos:
    vehiculo.desplazamiento()
