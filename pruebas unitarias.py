class Calculadora:
    def multiplicar(self, multiplicando, multiplicador):
        return multiplicando * multiplicador


import unittest


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_multiplicar_positivos(self):
        resultado = self.calculadora.multiplicar(5, 3)
        self.assertEqual(resultado, 15)

    def test_multiplicar_por_cero(self):
        resultado = self.calculadora.multiplicar(10, 0)
        self.assertEqual(resultado, 0)


if __name__ == '__main__':
    unittest.main()