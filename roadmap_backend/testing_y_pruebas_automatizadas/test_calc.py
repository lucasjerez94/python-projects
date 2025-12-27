import unittest
import calc


class TestCalc(unittest.TestCase):
    """
    Esta clase contiene todas las pruebas unitarias
    para las funciones definidas en calc.py.

    Cada método que comienza con 'test_' representa
    un caso de prueba independiente.
    """

    def test_add(self):
        """Pruebas para la función add"""
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        """Pruebas para la función subtract"""
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        """Pruebas para la función multiply"""
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        """Pruebas para la función divide"""
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """
        Verifica que la función divide
        lance un ValueError cuando el divisor es 0.
        """
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()

