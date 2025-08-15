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

miAuto = Auto('Peugeot','Style')
miAuto.desplazamiento()

miMoto = Moto('Honda','Civic')
miMoto.desplazamiento()

miCamion = Camion('Trucker','Speed')
miCamion.desplazamiento()
