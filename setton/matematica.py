from functools import reduce
from math import sqrt, pi
from multipledispatch import dispatch

# Constantes

GUGOL = 10**100

# Classes

'''
class Forma2D:
    def __init__(self, lados):
        self.area = None
        self.lados = lados


class Triangulo(Forma2D):
    def __init__(self, base, altura):
        super().__init__(3)
        self.area = base * altura / 2


class Quadrilatero(Forma2D):
    def __init__(self, **kwargs):
        super().__init__(4)
        self.base = kwargs['base']
        self.altura = kwargs['altura']
        self.area = kwargs['base']*kwargs['altura']


class Trapezio(Quadrilatero):
    def __init__(self, base_maior, base_menor, altura, **kwargs):
        super().__init__(base=(base_maior+base_menor)/2, altura=altura)
        self.angulo1 = kwargs['angulo1']
        self.angulo2 = kwargs['angulo2']
        self.angulo3 = kwargs['angulo3']
        self.angulo4 = kwargs['angulo4']
        self.diagonal1 = kwargs['diagonal1']
        self.diagonal2 = kwargs['diagonal2']


class Paralelogramo(Quadrilatero):
    def __init__(self, base, altura, **kwargs):
        super().__init__(base=base, altura=altura)
        self.angulo_agudo = kwargs['angulo_agudo']
        self.angulo_obtuso = kwargs['angulo_obtuso']
        self.nao_base = kwargs['diagonal']


class Retangulo(Quadrilatero):
    def __init__(self, base, altura):
        super().__init__(base=base, altura=altura)

    @property
    def diagonal(self):
        return sqrt(self.base**2 + self.altura**2)


class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


class PrismaRetangular:
    def __init__(self, altura, largura, profundidade):
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade
        self.medidas = [self.altura, self.largura, self.profundidade]
        self.volume = times(*self.medidas)
        self.area_superficial = sum([times(*comb) for comb in combinations(self.medidas, 2)])*2

    def massa(self, densidade):
        return densidade*self.volume
'''

# Funções


def add(*args):
    """Soma todos os argumentos passados e retorna o resultado"""
    return sum(args)


def subtr(num1, num2, absolute=False):
    """Recebe dois dados do tipo float e retorna o resultado da subtração do maior pelo menor"""
    return abs(num1 - num2) if absolute else num1 - num2


def times(*args):
    """Multiplica todos os argumentos passados e retorna o resultado"""
    return reduce(lambda x, y: x*y, args)


def divide(dividendo, divisor, arredondar=False):
    """Recebe dois dados do tipo float e retorna o resultado da divisão do primeiro pelo segundo"""
    if type(arredondar) == int:
        return round(dividendo / divisor, arredondar)
    return dividendo / divisor


def mmc2(num1, num2):
    maior = max(num1, num2)
    menor = min(num1, num2)
    maiorini = maior
    while True:
        if not maior % menor:
            return maior
        maior += maiorini


def mmc(*args):
    return reduce(mmc2, args)


def primo(numero):
    if numero == 2:
        return True
    if numero % 2 == 0 or numero < 2:
        return False
    for i in range(3, int(sqrt(numero))+1, 2):
        if not numero % i:
            return False
    return True


def primos_ate(numero):
    if numero < 2:
        return []
    todos = [2]
    for i in range(2, numero + 1):
        for j in todos:
            if j > sqrt(i):
                todos.append(i)
                break
            if not i % j:
                break
    return todos


def maior_primo_ate(numero):
    while not primo(numero):
        numero -= 1
    return numero


def circunferencia(raio, arredondar=False):
    if raio <= 0:
        raise ValueError("O raio deve ser maior que zero.")
    return round(2*raio*pi, arredondar) if type(arredondar) == int else 2*raio*pi


def area_do_circulo(raio, arredondar=False):
    if raio <= 0:
        raise ValueError("O raio deve ser maior que zero.")
    return round(pi*raio*raio, arredondar) if type(arredondar) == int else pi*raio*raio


@dispatch(int, int, int)
def somatoria(inicio, fim, passo):
    """Retorna a soma de todos os números inteiros entre o inicio e o fim pelo passo informado"""
    if (inicio - fim) % passo:
        return 'Passo inválido, não coincide.'

    return ((fim - inicio)/passo + 1)*(fim + inicio)/2


@dispatch(int, int)
def somatoria(inicio, fim):
    """Retorna a soma de todos os números inteiros entre o inicio e o fim"""
    return somatoria(inicio, fim, 1)


@dispatch(int)
def somatoria(fim):
    """Retorna a soma de todos os números inteiros entre 1 e o número informado"""
    return somatoria(1, fim, 1)


def gera_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = ax^2 + bx + c"""
    return lambda x: a * x ** 2 + b * x + c


def resolve_funcao_quadratica(a, b, c):
    delta = b**2 - 4*a*c
    try:
        solucao1 = (-b + sqrt(delta)) / (2 * a)
        solucao2 = (-b - sqrt(delta)) / (2 * a)
    except ValueError:
        return 'Não há solução para os valores dados.'
    except ZeroDivisionError:
        return 'O coeficiente de x² não pode ser 0.'
    if delta == 0:
        return f'A solução é: {solucao1}'
    # Delta > 0
    if sqrt(delta) % 1 != 0:
        return f'As soluções são: ({-b} + √{delta}) / {2*a}, ({-b} - √{delta}) / {2*a}'  # Raiz de Delta não é exata
    elif (solucao1 or solucao2) % 1 != 0:
        return f'As soluções são: {-b + sqrt(delta)} / {2*a}, {-b - sqrt(delta)} / {2*a}'
    else:
        return f'As soluções são: {solucao1}, {solucao2}'  # Solução é exata


def limite(maximo, minimo, valor):
    """Se o valor estiver entre os limites, retorna o valor, se estiver acima do limite, retorna o maximo
    e se estiver abaixo retorna o minimo"""
    return min(max(valor, minimo), maximo)


def par(numero, mudar=''):
    res = numero % 2 == 0
    if res or not mudar:
        return res
    if mudar == '+':
        return numero + 1
    elif mudar == '-':
        return numero - 1
    else:
        raise ValueError("Mudar pode ser '+' ou '-'")


def impar(numero, mudar=''):
    res = numero % 2 == 1
    if res or not mudar:
        return res
    if mudar == '+':
        return numero + 1
    elif mudar == '-':
        return numero - 1
    else:
        raise ValueError("Mudar pode ser '+' ou '-'")


def soma_pg(termo_1, razao, numero_de_termos):
    return termo_1*(pow(razao, numero_de_termos)-1)/(razao-1)


# Conversão de Medidas


def celcius_fahrenheit(temperatura_celsius, arredondar=False):
    """Converte um temperatura de celsius para fahrenheit"""
    calc = temperatura_celsius * 1.4 + 32
    return round(calc, arredondar) if type(arredondar) == int else calc


def fahrenheit_celsius(temperatura_fahrenheit, arredondar=False):
    """Converte um temperatura de celsius para fahrenheit"""
    calc = (temperatura_fahrenheit - 32) / 1.4
    return round(calc, arredondar) if type(arredondar) == int else calc


def graus_radianos(graus, mostrar_como_decimal=False):
    return pi * graus / 180 if mostrar_como_decimal else f"{graus/180}π"


@dispatch(str)
def radianos_graus(radianos):
    return float(radianos[:-1])*180


@dispatch(float)
def radianos_graus(radianos):
    return radianos * 180 / pi


def calcular(string: str) -> float:
    """
    Calcula o valor de uma expessão dada no formato de uma string
    :param string: A expressão para ser calculada
    :return: O valor da expressão
    """
    string = string.split()

    def validacao(calc: iter) -> NotImplemented:
        # Values
        try:
            float(string[0])
        except ValueError:
            if string[0] != '(':
                raise ValueError("Expressão Inválida")
        for n in string:
            try:
                float(n)
            except ValueError:
                if n not in '()**/+-':
                    raise ValueError(f"Expressão Inválida: {n}")

        # Valid_parentheses
        cont = 0
        for char in calc:
            if char == '(':
                cont += 1
            elif char == ')':
                cont -= 1
            if cont < 0:
                raise ValueError("Parenteses não válidos")
        if cont:
            raise ValueError("Parenteses não válidos")

    validacao(string)

    def find_parenthesis(calc: iter) -> tuple:
        start = calc.index('(') + 1
        while True:
            back = calc.index(')', start)
            try:
                front = calc.index('(', start)
                start = front+1
            except ValueError:
                return start, back
            if back < front:
                return start, back

    while '(' in string:
        ini, fim = find_parenthesis(string)
        new = string[ini:fim]
        for _ in range(ini, fim+2):
            string.pop(ini-1)
        insert = str(calcular(' '.join(new)))
        string.insert(ini-1, insert)

    i = 0
    while '**' in string and i < len(string):
        if string[i] == '**':
            f1 = float(string.pop(i - 1))
            string.pop(i - 1)
            f2 = float(string.pop(i - 1))
            string.insert(i - 1, str(f1 ** f2))
            i -= 1
        i += 1
    i = 0
    while ('*' in string or '/' in string) and i < len(string):
        if string[i] == '*':
            f1 = float(string.pop(i-1))
            string.pop(i-1)
            f2 = float(string.pop(i-1))
            string.insert(i - 1, str(f1 * f2))
            i -= 1
        elif string[i] == '/':
            f1 = float(string.pop(i-1))
            string.pop(i-1)
            f2 = float(string.pop(i-1))
            string.insert(i - 1, str(f1 / f2))
            i -= 1
        i += 1
    i = 1
    while ('+' in string or '-' in string) and i < len(string):
        if string[i] == '+':
            f1 = float(string.pop(i-1))
            string.pop(i-1)
            f2 = float(string.pop(i-1))
            string.insert(i - 1, str(f1 + f2))
        elif string[i] == '-':
            f1 = float(string.pop(i-1))
            string.pop(i-1)
            f2 = float(string.pop(i-1))
            string.insert(i - 1, str(f1 - f2))

    return float(string[0])
