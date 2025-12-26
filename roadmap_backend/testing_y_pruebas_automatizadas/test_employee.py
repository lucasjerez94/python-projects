import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@email.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(emp_1.email, 'Jane.Schafer@email.com')

    def test_fullname(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Sue Smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'John Schafer')
        self.assertEqual(emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)

if __name__ == '__main__':
    unittest.main()
"""
Corre este codigo y en la terminal figura:
...
Ran 3 tests in 0.000s
OK

Nose porque, pero luego añade 2 metodos mas dentro de la clase TestEmployee, los agrega al inicio, antes que comiencen los test_email, etc.
Agrega
def setUp(self):
    self.emp_1 = Employee('Corey', 'Schafer', 50000)
    self.emp_2 = Employee('Sue', 'Smith', 60000)
def tearDown(self):
    pass 

Como el video esta en otro idioma, no entiendo lo que dice cuando agrega estas funciones-metodos, no entiendo por ahora su objetivo.

Luego, quita la palabra "pass" de la funcion setUp y agrega esos datos, de emp1 y 2 y borra de las funciones test_email, test_fullname y test_apply_raise la declaracion de Employee y los 2 empleados creados.
Luego en todas las funciones-metodos, en cada oportunidad que aparece el emp1 y 2 les declara un self. en las declaraciones de emp_1.first y entro de los assertEqual de todas las funciones-metodos

Como resultado, la consola le da:
...
Ran 3 tests
OK

Luego suplanta todo el codigo y por lo visto solo le agrega unos print a cada funcion metodo, antes de cualquier otra sentencia. Es decir, ahora en todas las funciones metodos hay un print y lo agregado es lo siguiente:

print('setUp')
print('tearDown\n')
print('test_email')
print('test_fullname')
print('test_apply_raise')

Ahora en consola le sale:
setUp
test_apply_raise
tearDown

setUp
test_email
tearDown

setUp
test_fullname
tearDown

...
Ran 3 tests 
OK

Ahora vuelve a modificar la clase principal quedando de la siguiente manera.

@classmethod
def setUpClass(cls):
    print('setupClass')

@classmethod
def tearDownClass(cls):
    print('teardownClass')


Sale ok, pero salen en diferente orden los prints,
no entiendo el sentido de esto.

Luego, agrega una funcion mas al final de todo, luego de la de apply_raise en la clase Employee

def monthly_schedule(self, month):
    response = requests.get(f'http://company.com/{self.last}/{month})
    if response.ok:
        return response.text
    else:
        return 'Bad Response!'

Los imports quedaron asi:
import unittest
from unittest.mock import patch
from employee import Employee

Y ahora agrega el test para el monthly_schedule

def test_monthly_schedule(self):
    with patch('employee.requests.get') as mocked_get:
        mocked_get.return_value.ok = True
        mocked_get.return_value.text = 'Success'

        schedule = self.emp_1.monthly_schedule('May')
        mocked_get.assert_called_with('http://company.com/Schafer/May')
        self.assertEqual(schedule, 'Success')

Corre el codigo y da
Ran 4 tests 
OK


Luego prueba modificar y agrega lo siguiente:

mocked_get.return_value.ok = True
schedule = self.emp_2.monthly_schedule('June')
mocked_get.assert_called_with('http://company.com/Smith/June')
self.assertEqual(schedule, 'Bad Response!')

Mismo resultado que antes en la consola.


"""

