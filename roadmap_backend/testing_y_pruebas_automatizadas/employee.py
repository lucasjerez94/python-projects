class Employee: #No tiene parametro y empieza con mayuscula, esta ok?
    """A sample Employee class """

    raise_ant = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property #Necesito recordar que siginificaba esto tambien
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_ant)
"""
Comento lo que entiendo de esto:
Dentro de la clase Employee primero se declara una variable de propiedad float.

Luego se declaran los atributos de la clase, esas 3 variables: first, last, pay.

El @property creo que se llama decorador, no? pero no entiendo que es lo que esta trayendo digamos.
Se define el metodo email, que retorna el nombre y apellido agregando el dominio de correo.
Lo mismo el segundo @property, pero solo retorna nombre y apellido.

El tercer metodo, es para aplicar un aumento en el pago. 
Define nuevamente el valor de la variable pay, lo define como un int y multiplica el primer valor
ingresado en la variable pay multiplicado por el valor de la variable definida al comienzo del codigo. 

"""

