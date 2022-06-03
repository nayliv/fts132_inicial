
import unittest

import pytest

from main import calcular_area_triangulo, somar_dois_numeros, dividir_dois_numeros, multiplicar_dois_numeros, \
    elevar_um_numero_pelo_outro, calcular_area_retangulo, calcular_area_quadrado, calcular_area_circulo, calcular_volume_do_paralelograma



def test_calcular_area_quadrado():
    lado = 5
    resultado_esperado = 25
    resultado_atual = calcular_area_quadrado(5)

    assert resultado_esperado == resultado_atual

def test_calcular_area_retangulo():
    lado1 = 6
    lado2 = 4
    resultado_esperado = 24
    resultado_atual = calcular_area_retangulo(6, 4)

    assert resultado_esperado == resultado_atual

def test_calcular_area_triangulo():
    base = 4
    altura = 5
    resultado_esperado = 10
    resultado_atual = calcular_area_triangulo(4, 5)

    assert resultado_esperado == resultado_atual


def test_somar_dois_numeros():
    # - 1ª etapa: Configura
    # Dados / Valores
    # Entradas / Inputs
    num1 = 8
    num2 = 9

    # Saída / Output
    resultado_esperado = 17

    # - 2³ Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3³ Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def test_dividir_dois_numeros():
    num1 = 10
    num2 = 2

    resultado_esperado = 5

    resultado_atual = dividir_dois_numeros(num1, num2)

    assert resultado_atual == resultado_esperado

def test_multiplicar_dois_numeros():
    num1 = 2
    num2 = 2

    resultado_esperado = 4

    resultado_atual = multiplicar_dois_numeros(num1, num2)

    assert resultado_atual == resultado_esperado

def test_elevar_dois_numeros():
    num1 = 5
    num2 = 2

    resultado_esperado = 25

    resultado_atual = elevar_um_numero_pelo_outro(num1 , num2)

    assert resultado_esperado == resultado_atual

#anotação para utilizar como massa de teste
@pytest.mark.parametrize('raio,resultado_esperado',[
                             (1,3.14), #teste n1
                             (2,12.56), #teste n2
                             (3,28.26), #teste n3
                         ])

def test_calcular_area_circulo(raio, resultado_esperado):
    #raio = 1
    #resultado_esperado = 3.14

    resultado_atual = calcular_area_circulo(raio)
    assert resultado_esperado == resultado_atual

# Calcular e testar a área de um círculo
# Area = 3,14 * (raio ** 2)

def testar_calcular_volume_do_paralelograma():
    #1 Configura
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100

    #2 Executa
    resultado_atual = calcular_volume_do_paralelograma(largura, comprimento, altura)

    #3 Valida
    assert resultado_esperado == resultado_atual