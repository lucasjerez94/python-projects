class Curso():
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial" # Propiedad encapsulada

    def get_imparticion(self):
        return self.__imparticion
    
    def set_imparticion(self, modo):
        if modo in ['Presencial', 'Virtual']:
            self.__imparticion = modo 
        else:
            print('❌ Modo de impartición inválido. Solo puede ser "Presencial" o "Virtual".')
    
    def mostrarDatos(self):
        dat = 'Nombre: {0}. \nCreditos: {1}. \nProfesion: {2}. \nModo de imparticion: {3}'
        print(dat.format(self.nombre, self.creditos, self.profesion, self.__imparticion))


curse = Curso('Backend Developer JR','1000','IT')
curse.mostrarDatos()
print(curse.get_imparticion())
curse.set_imparticion('Virtualito')
print(curse.get_imparticion())