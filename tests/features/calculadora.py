# coding=utf-8

# comentario agregado para que travis CI detecte un cambio
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
            return 'N multiplicado por uno siempre sera n'
        else:
            self.resultado = num1 * num2

    def dividir(self, num1, num2):
        if num2 == 0:
            return 'Indeterminacion'
        else:
            self.resultado = num1 / num2

    def potencia(self, num1, num2):
        if num1 == 1:
            return 'Elevar el uno a la X potencia siempre sera uno'
        else:
            self.resultado = num1 ** num2

    def raiz(self, num1, num2):
        if num2 < 0:
            return 'No se puede obtener la raiz de un número negativo'
        elif num1 == 0:
            return 'No es posible obtener una raiz cero'
        else:
            self.resultado = num2 ** (1.0 / num1)
