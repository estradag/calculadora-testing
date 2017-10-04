# coding=utf-8


class Calculadora():

    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def sumar(self, num1, num2):
        try:
            self.resultado = num1 + num2
        except:
            return 'Datos incorrectos'

    def restar(self, num1, num2):
        if num1 == 0 and num2 == 0:
            return 'No puedes hacer una resta de ceros'
        else:
            self.resultado = num1 - num2

    def multiplicar(self, num1, num2):
        if num1 == 1 or num2 == 1:
            return 'No tiene caso multiplicar por uno, sabes el resultado'
        else:
            self.resultado = num1 * num2

    def dividir(self, num1, num2):
        if num2 == 0:
            return 'Indeterminación'
        else:
            self.resultado = num1 / num2

    def potencia(self, num1, num2):
        if num1 == 1:
            return 'No tiene caso elevar el uno a la X potencia, \
                    siempre será uno'
        else:
            self.resultado = num1 ** num2

    def raiz(self, num1, num2):
        if num2 < 0:
            return 'No se puede obtener la raíz de un número negativo'
        elif num1 == 0:
            return 'No es posible obtener una raíz cero'
        else:
            self.resultado = num2 ** (1.0 / num1)
