import unittest
import calc

class TesctCalc(unittest.TestCase):

    def test_add(self): #Luego le cambio el nombre a add_test y funciono igual
        result = calc.add(10, 5)
        self.assertEqual(result, 15) #Luego prueba cambiando el segundo valor a 14 y cambia el resultado por consola, avisando que hay error.
    
# Al ejecutar en la terminal la sentencia: python test_calc.py no devueleve nada
# Hay que ejecutar la sentencia: python -m unittest test_calc.py, salida: OK
# Para lograr que la ejecucion funcione bien con la primer sentencia, en el codigo se debe agregar lo siguiente:

if __name__ == '__main__':
    unittest.main()

"""
Luego, dentro de la clase TestCalc prueba modificar la estructura 
de la funcion test_add de la siguiente manera:
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

 Y al correr el codigo, la salida en la terminal es : OK 

 Y ahora agrega lo siguiente:

 def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

Tambien le da como resultado OK, diciendo "Ran 4 tests"

Luego prueba ir al archivo calc.py y modificar el return de la funcion, le agrega un *, quedando: "return x ** y". Vuelve a correr el codigo y el error que sale dice "AssertionError: 1000000 != 50" 

Arriba de la terminal, en cada resultado hay una F que va agregando puntos, nose que significara porque el video esta en otro idioma. Por ejemplo, en esta ultima ejecucion figura: ..F. (entiendo que representan la cantidad de testeos y la F siginifica Fail, no lo se)

Luego edita la funcion de division, le agrega un / , pero no da error.

Luego, en la funcion def test_divide agrega una sentencia mas que dice:
self.assertEqual(calc.divide(5, 2), 2.5) y ahi le da error nuevamente. 
En la terminal sale:
.F..
FAIL: test_divide (__main__.TestCalc)
AssertionError: 2 != 2.5

Asi que luego vuelve al editar la funcion de division y le deja un solo / y ya no da error al correr el codigo. 
Sale:
....
OK

Agrega una sentencia mas dentro de la funciona test_divide :
self.assertRaises(ValueError, calc.divide, 10, 0) y en la terminal sale:
....
OK
Luego le cambia como el dividendo o divisor, nose cual es jaja, cambia el 0 por un 2 y ahi si le sale error.
Dice: AssertionError: ValueError not raised by divide

Luego agrega la siguiente sentencia, siempre dentro de la funcion test_divide:

with self.assertRaises(ValueError):
    calc.divide(10,0)

Resultado: OK



"""



