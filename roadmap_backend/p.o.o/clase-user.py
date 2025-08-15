class User:
    def __init__(self):
        self.email = input('Introduzca su correo electronico: ')
        self.__password = input('Introduzca su contraseña: ')
        self.permissions = ['edit','create','update']
        self.username = None
    
    def setear_username(self):
        self.username = input('Introduzca el username que desea tener: ')
        print('Su username fue modificado exitosamente a: {}'.format(self.username))

class UserPro(User):
    def __init__(self):
        super().__init__()
        self.permissions += ['delete','download']

    def suscription(self,monto):
        print('Usted ha pagado exitosamente el monto (${})'.format(monto))
    
class UserManager:
    def create_user(self,suscripcion):
        if suscripcion:
            user = UserPro()
        else:
            user = User()
        print('Se ha creado exitosamente su usuario. Sus permisos son: {}'.format(user.permissions))
        return user

usuario1 = User()
usuario1.setear_username()

