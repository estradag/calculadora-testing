# coding=utf-8
from lettuce import step, world
from calculadora import Calculadora

# -----------------------------------------------------------------------------
# -------------------------------- Calculadora --------------------------------
# -----------------------------------------------------------------------------
@step(u'Dado que ingreso un par de numeros')
def dado_que_ingreso_un_par_de_numeros(step):
    world.cal = Calculadora()


@step(u'cuando realizo la suma de "([^"]*)" mas "([^"]*)"')
def cuando_realizo_la_suma_de_num1_mas_num1(step, num1, num2):
    world.cal.sumar(int(num1), int(num2))


@step(u'cuando realizo la resta de "([^"]*)" menos "([^"]*)"')
def cuando_realizo_la_resta_de_num1_menos_num1(step, num1, num2):
    world.cal.restar(int(num1), int(num2))


@step(u'cuando realizo la multiplicación de "([^"]*)" por "([^"]*)"')
def cuando_realizo_la_multiplicacion_de_num1_por_num1(step, num1, num2):
    world.cal.multiplicar(int(num1), int(num2))


@step(u'cuando realizo la división de "([^"]*)" entre "([^"]*)"')
def cuando_realizo_la_division_de_num1_entre_num1(step, num1, num2):
    world.cal.dividir(int(num1), int(num2))


@step(u'cuando realizo la potencia de "([^"]*)" elevado a "([^"]*)"')
def cuando_realizo_la_potencia_de_num1_elevado_a_num1(step, num1, num2):
    world.cal.potencia(int(num1), int(num2))


@step(u'cuando realizo la raíz "([^"]*)" de "([^"]*)"')
def cuando_realizo_la_raiz_num1_de_num2(step, num1, num2):
    world.cal.raiz(int(num1), int(num2))


@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_num1(step, esperado):
    obtenido = world.cal.obtener_resultado()
    assert int(esperado) == obtenido, \
        'El resultado esperado es: ' + esperado + \
        " y el obtenido es: " + str(obtenido)
