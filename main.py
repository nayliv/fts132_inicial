def calcular_area_quadrado (lado):
    return lado * lado

def calcular_area_retangulo(lado1, lado2):
    return lado1 * lado2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def somar_dois_numeros(num1, num2):
    return num1 + num2

def dividir_dois_numeros(num1,num2):
    try:
        return num1 / num2

    except ZeroDivisionError:
        return 'Não é possível dividir por zero.'

def multiplicar_dois_numeros(num1,num2):
    return num1 * num2

def elevar_um_numero_pelo_outro(base,exp):
    return base ** exp

def calcular_area_circulo(raio):
    try:
        return 3.14 * raio ** 2
    except TypeError:
        return 'Falha no cálculo - Raio não é um número'

def calcular_volume_do_paralelograma(largura, comprimento, altura):
    return largura * comprimento * altura

if __name__ == '__main__':
    soma = somar_dois_numeros(5,7)
    print(f'A soma é {soma}')

    divisao = dividir_dois_numeros(10,0)
    print(f'A divisão é {divisao}')

    multiplicacao = multiplicar_dois_numeros(5,2)
    print(f'A multiplicação é {multiplicacao}')

    exponenciacao = elevar_um_numero_pelo_outro(5, 2)
    print(f'A exponenciação é {exponenciacao}')

    area_quadrado = calcular_area_quadrado(4)
    print(f'A área do quadrado é {area_quadrado}')

    area_retangulo = calcular_area_retangulo(4, 5)
    print(f'A área do retângulo é {area_retangulo}')

    area_triangulo = calcular_area_triangulo(4, 2)
    print(f'A área do triângulo é {area_triangulo}')

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

def test_calcular_volume_do_paralelograma():
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100
    resultado_atual = calcular_volume_do_paralelograma(largura,comprimento,altura)

    assert resultado_esperado == resultado_atual



'''def test_somar_dois_numeros():
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

# Calcular e testar a área de um quadrado
# Calcular e testar a área de um retângulo
# Calcular e testar a área de um triângulo'''