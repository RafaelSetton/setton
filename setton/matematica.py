from functools import reduce
from math import sqrt, pi, cos, radians, sin, inf
from multipledispatch import dispatch
from typing import Callable
from itertools import combinations
from re import findall

# Constantes

GUGOL = 10**100

# Classes


class Forma2D:
    def __init__(self, lados):
        self.lados = lados

    @property
    def area(self, arredondar: int = False):
        raise NotImplementedError

    @property
    def perimetro(self, arredondar: int = False):
        raise NotImplementedError


class Triangulo(Forma2D):
    def __init__(self, base: float, altura: float, lados: tuple = tuple(), angulos: tuple = tuple()):
        """

        :param base: a base do triângulo
        :param altura: a altura do triângulo
        :param lados: os lados A, B e C do triângulo. Caso um dos lados seja indefinido, coloque -1 no lugar.
        :param angulos: os angulos AB, BC e CA do triângulo. Caso um dos angulos seja indefinido, coloque -1 no lugar.
        """
        erros = []
        if base <= 0 or altura <= 0:
            erros.append("A base e a altura devem ser positivas")
        if 2 * max(lados) >= sum(lados):
            erros.append("A soma dos dois menores lados deve ser maior que o maior lado")
        if angulos.count(-1) == 1:
            ind = angulos.index(-1)
            angulos = list(angulos)
            angulos[ind] = 179 - sum(angulos)
        elif angulos.count(-1) > 1:
            angulos = []
        if 0 in lados:
            erros.append("Todos os lados devem ser positivos")
        if erros:
            raise ValueError('\n'.join(erros))

        super().__init__(3)
        self.base = base
        self.altura = altura
        self.lados = list(lados)
        self.angulos = list(angulos)

        if self.angulos and self.lados:
            for i, v in enumerate(self.lados):
                if v < 0:
                    angulo = self.angulos[i-2]
                    self.lados[i] = self.lados[i-1]**2 + self.lados[i-2]**2 - cos(radians(angulo))

    @property
    def area(self, arredondar: int = False):
        return self.base * self.altura / 2

    @property
    def perimetro(self, arredondar: int = False):
        return sum(self.lados)


class Quadrilatero(Forma2D):
    def __init__(self):
        super().__init__(4)

    @property
    def area(self, arredondar: int = False):
        raise NotImplementedError

    @property
    def perimetro(self, arredondar: int = False):
        raise NotImplementedError


class Trapezio(Quadrilatero):
    def __init__(self, base_maior: float, base_menor: float, altura: float,
                 diagonais: tuple = tuple(), angulos: tuple = tuple()):
        """
        Cria um Trapézio ABCD
        :param base_maior: A base maior (CD)
        :param base_menor: A base menor (AB)
        :param altura: A altura do trapézio
        :param diagonais: os lados BC e DA
        :param angulos: os angulos A, B, C, D
        """

        super().__init__()
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura
        self.diagonais = list(diagonais)
        self.angulos = list(angulos)

    @property
    def area(self, arredondar: int = False):
        res = (self.base_menor + self.base_maior) * self.altura / 2
        return round(res, arredondar) if arredondar else res

    @property
    def perimetro(self, arredondar: int = False):
        if len(self.diagonais) == 2:
            return sum([*self.diagonais, self.base_maior, self.base_menor])
        raise ValueError("Diagonais não informadas")


class Paralelogramo(Quadrilatero):
    def __init__(self, base: float = None, altura: float = None, angulos: tuple = tuple(), diagonal: float = None):
        super().__init__()
        self.base = base
        self.altura = altura

        if angulos:
            if len(angulos) == 1:
                angulos = (angulos[0], 90 - angulos[0])
            self.angulo_agudo = min(angulos)
            self.angulo_obtuso = max(angulos)

        if self.altura and angulos and not diagonal:
            diagonal = self.altura / sin(radians(self.angulo_agudo))
        self.diagonal = diagonal

    @property
    def area(self, arredondar: int = False):
        res = self.base * self.altura
        return round(res, arredondar) if arredondar else res

    @property
    def perimetro(self, arredondar: int = False):
        res = (self.base + self.diagonal) * 2
        return round(res, arredondar) if arredondar else res


class Retangulo(Quadrilatero):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    @property
    def diagonal(self):
        return sqrt(self.base**2 + self.altura**2)

    @property
    def area(self, arredondar: int = False):
        res = self.base = self.altura
        return round(res, arredondar) if arredondar else res

    @property
    def perimetro(self, arredondar: int = False):
        res = 2 * (self.base + self.altura)
        return round(res, arredondar) if arredondar else res


class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
        self.lado = lado

    @property
    def area(self, arredondar: int = False):
        res = self.lado ** 2
        return round(res, arredondar) if arredondar else res

    @property
    def perimetro(self, arredondar: int = False):
        res = self.lado * 4
        return round(res, arredondar) if arredondar else res


class Circulo(Forma2D):
    def __init__(self, raio):
        super().__init__(inf)
        if self.raio <= 0:
            raise ValueError("O raio deve ser maior que zero.")
        self.raio = raio

    @property
    def perimetro(self, arredondar: int = False):
        res = 2*self.raio*pi
        return round(res, arredondar) if arredondar else res

    @property
    def area(self, arredondar: int = False) -> (float, int):
        return round(pi*self.raio*self.raio, arredondar) if type(arredondar) == int else pi*self.raio*self.raio


class Forma3D:
    def __init__(self, vertices=None, faces=None, arestas=None):
        self.__vertices = vertices
        self.__faces = faces
        self.__arestas = arestas

        if self.__faces is None and \
                type(self.__arestas) in (float or int) and type(self.__vertices) in (float or int):
            self.__faces = 2 + self.__arestas - self.__vertices
        elif self.__arestas is None and \
                type(self.__faces) in (float or int) and type(self.__vertices) in (float or int):
            self.__arestas = self.__faces + self.__vertices - 2
        elif self.__vertices is None and \
                type(self.__arestas) in (float or int) and type(self.__faces) in (float or int):
            self.__vertices = 2 + self.__arestas - self.__faces

    @property
    def faces(self):
        return self.__faces

    @property
    def arestas(self):
        return self.__arestas

    @property
    def vertices(self):
        return self.__vertices


class PrismaRetangular(Forma3D):
    def __init__(self, altura, largura, profundidade):
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade
        self.medidas = [self.altura, self.largura, self.profundidade]
        super().__init__(8, 6, 12)

    @property
    def area_superficial(self):
        return sum([lado1 * lado2 for lado1, lado2 in combinations(self.medidas, 2)])*2

    @property
    def volume(self):
        return self.altura * self.largura * self.profundidade

    def massa(self, densidade):
        return densidade*self.volume


# Conversões

class AlgarismosRomanos:
    NUM_TO_STR = {1000: 'M',
                  900: 'CM',
                  500: 'D',
                  400: 'CD',
                  100: 'C',
                  90: 'XC',
                  50: 'L',
                  40: 'XL',
                  10: 'X',
                  9: 'IX',
                  5: 'V',
                  4: 'IV',
                  1: 'I'
                  }
    STR_TO_NUM = {v: k for k, v in NUM_TO_STR.items()}

    @classmethod
    def para_romanos(cls, n):
        roman_string = ''
        for key in sorted(cls.NUM_TO_STR.keys(), reverse=True):
            while n >= key:
                roman_string += cls.NUM_TO_STR[key]
                n -= key
        return roman_string

    @classmethod
    def de_romanos(cls, roman):
        n = 0
        while roman:
            for key in sorted(cls.STR_TO_NUM.keys(), key=lambda k: cls.STR_TO_NUM[k], reverse=True):
                if roman.startswith(key):
                    n += cls.STR_TO_NUM[key]
                    roman = roman.replace(key, '', 1)
        return n


class CelsiusFahrenheit:

    @staticmethod
    def to_celsius(fahrenheit: float, arredondar: int = False) -> (float, int):
        """Converte um temperatura de celsius para fahrenheit"""
        calc = (fahrenheit - 32) / 1.4
        return round(calc, arredondar) if type(arredondar) == int else calc

    @staticmethod
    def celcius_fahrenheit(celsius: float, arredondar: int = False) -> (float, int):
        """Converte um temperatura de celsius para fahrenheit"""
        calc = celsius * 1.4 + 32
        return round(calc, arredondar) if type(arredondar) == int else calc


class RadianosGraus:
    @staticmethod
    def graus_radianos(graus: float, mostrar_como_decimal: bool = False) -> (float, str):
        return pi * graus / 180 if mostrar_como_decimal else f"{graus/180}π"

    @staticmethod
    @dispatch(str)
    def radianos_graus(radianos: str) -> float:
        return float(radianos[:-1])*180

    @staticmethod
    @dispatch(float)
    def radianos_graus(radianos: float) -> float:
        return radianos * 180 / pi


# Funções

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
    for i in range(3, numero + 1):
        for j in todos:
            if j > sqrt(i):
                todos.append(i)
                break
            if not i % j:
                break
    return todos


def maior_primo_ate(numero):
    if numero == 2:
        return 2
    if numero < 2:
        return None
    if not numero % 2:
        numero -= 1
    while not primo(numero):
        numero -= 2
    return numero


@dispatch(int, int, int)
def somatoria(inicio: int, fim: int, passo: int) -> float:
    """Retorna a soma de todos os números inteiros entre o inicio e o fim pelo passo informado"""
    if (inicio - fim) % passo:
        raise ValueError('Passo inválido, não coincide.')

    return ((fim - inicio)/passo + 1)*(fim + inicio)/2


@dispatch(int, int)
def somatoria(inicio: int, fim: int) -> float:
    """Retorna a soma de todos os números inteiros entre o inicio e o fim"""
    return somatoria(inicio, fim, 1)


@dispatch(int)
def somatoria(fim: int) -> float:
    """Retorna a soma de todos os números inteiros entre 1 e o número informado"""
    return somatoria(1, fim, 1)


def gera_funcao_quadratica(a: float, b: float, c: float) -> Callable[[float], float]:
    """Retorna a função f(x) = ax^2 + bx + c"""
    return lambda x: a * x ** 2 + b * x + c


def resolve_funcao_quadratica(a: float, b: float, c: float) -> str:
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


def limite(maximo: float, minimo: float, valor: float) -> float:
    """Se o valor estiver entre os limites, retorna o valor, se estiver acima do limite, retorna o maximo
    e se estiver abaixo retorna o minimo"""
    return min(max(valor, minimo), maximo)


def soma_pg(termo_1: float, razao: float, numero_de_termos: int) -> float:
    return termo_1*(pow(razao, numero_de_termos)-1)/(razao-1)


def simplify_polynomial(poly: str):
    monoms = [''.join(sorted(x)) for x in findall("[a-z0-9]+", poly)]
    ops = [''.join(sorted(x)) for x in findall("[+-]", poly)]
    if len(ops) < len(monoms):
        ops.insert(0, '+')
    dic = dict()
    for i, monom in enumerate(monoms):
        var = ''.join([let for let in monom if let.isalpha()])
        coef = ''.join([let for let in monom if let.isnumeric()]) or '1'
        if dic.get(var):
            dic[var] += int(f"{ops[i]}{coef}")
        else:
            dic[var] = int(f"{ops[i]}{coef}")
    final = ''
    for var in sorted(sorted(dic.keys()), key=len):
        coef = dic[var]
        if coef == 1:
            final += f'+{var}'
        elif coef == -1:
            final += f'-{var}'
        elif coef > 0:
            final += f'+{coef}{var}'
        elif coef < 0:
            final += f'{coef}{var}'
    if final.startswith('+'):
        final = final[1:]
    return final
