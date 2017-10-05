# coding=utf-8

import unittest
from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_valor_de_inicio_igual_a_cero(self):
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_sumar_2_mas_2_igual_a_4(self):
        self.calc.sumar(2, 2)
        self.assertEquals(self.calc.obtener_resultado(), 4)

    def test_sumar_3_mas_3_igual_a_6(self):
        self.calc.sumar(3, 3)
        self.assertEquals(self.calc.obtener_resultado(), 6)

    def test_sumar_1_neg_mas_2_igual_a_1(self):
        self.calc.sumar(-1, 2)
        self.assertEquals(self.calc.obtener_resultado(), 1)

    def test_sumar_L_mas_4_igual_a_error(self):
        self.assertEquals(self.calc.sumar('L', 4), 'Datos incorrectos')

    def test_restar_1_menos_6_neg_igual_a_7(self):
        self.calc.restar(1, -6)
        self.assertEquals(self.calc.obtener_resultado(), 7)

    def test_restar_0_menos_0_igual_a_error(self):
        self.assertEquals(self.calc.restar(0, 0),
                            'No puedes hacer una resta de ceros')

    def test_multiplicar_2_por_2_igual_a_4(self):
        self.calc.multiplicar(2, 2)
        self.assertEquals(self.calc.obtener_resultado(), 4)

    def test_numX_por_1_no_tiene_caso(self):
        self.assertEquals(self.calc.multiplicar(7, 1),
                            'N multiplicado por uno siempre sera n')

    def test_dividir_10_entre_2_igual_a_5(self):
        self.calc.dividir(10, 2)
        self.assertEquals(self.calc.obtener_resultado(), 5)

    def test_dividir_numX_entre_0_igual_error(self):
        self.assertEquals(self.calc.dividir(25, 0), 'Indeterminacion')

    def test_elevar_2_a_5_igual_32(self):
        self.calc.potencia(2, 5)
        self.assertEquals(self.calc.obtener_resultado(), 32)

    def test_elevar_1_a_5_no_tiene_caso(self):
        self.assertEquals(self.calc.potencia(1, 5),
                            'Elevar el uno a la X potencia siempre sera uno')

    def test_raiz_cuadrada_de_144_es_12(self):
        self.calc.raiz(2, 144)
        self.assertEquals(self.calc.obtener_resultado(), 12.0)

    def test_raiz_numero_negativo_igual_error(self):
        self.assertEquals(self.calc.raiz(2, -100),
                            'No se puede obtener la raiz de un numero negativo')

    def test_raiz_0_igual_error(self):
        self.assertEquals(self.calc.raiz(0, 100),
                            'No es posible obtener una raiz cero')

    def tearDown(self):
        pass

if __name__ == '__main__': # pragma: no cover
    unittest.main() # pragma: no cover
