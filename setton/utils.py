from multipledispatch import dispatch
from threading import Thread
from keyboard import wait
from random import randint
from os import listdir, path
from setton.constantes import MORSE_COMPLETO, A_ESPECIAL, E_ESPECIAL, I_ESPECIAL, O_ESPECIAL, U_ESPECIAL, CODABLE
from setton.matematica import primos_ate
from string import ascii_lowercase, punctuation
from requests import get
from cv2 import imread, imwrite
from typing import Any, Callable
from PIL import Image


class List(list):
    def _remove(self, __value):
        self.remove(__value)
        return self

    def replace(self, __old, __new, __count: int = -1):
        c = 0
        while __old in self and c != __count:
            ind = self.index(__old)
            self[ind] = __new
            c += 1

    def _replace(self, __old, __new, __count: int = -1):
        self.replace(__old, __new, __count)
        return self

    def __sub__(self, other):
        for el in other:
            try:
                self.remove(el)
            except ValueError:
                pass


class String(str):
    def __sub__(self, other: str):
        return String(''.join(filter(lambda x: x not in other, self)))


def trata_texto(acentos: bool = True, pontos: bool = True) -> callable:
    def decorador(funcao):
        def tratamento(*args):
            novo = list(args)
            for ind, tex in enumerate(novo):
                if acentos:
                    tex = trata_acento(tex)
                if pontos:
                    tex = trata_ponto(tex)
                novo[ind] = tex[0]
            return funcao(*novo)

        return tratamento

    return decorador


def keyboard_listener(dic_funcs: dict[Any, Callable[[], None]]) -> None:
    """
    Inicia Threads que executam as funções ao pressionar suas respectivas teclas.
    :param dic_funcs: Um dicionário no formato {tecla: funcao}. funcao() será executado quando tecla for pressionado.
    :return: None
    """

    def listen(tecla):
        while True:
            try:
                wait(tecla)
                dic_funcs[tecla]()
            except KeyError:
                pass

    threads = [Thread(target=listen, kwargs={"tecla": tecla}) for tecla in dic_funcs.keys()]

    for thread in threads:
        thread.start()


def valida_resposta(texto: str, respostas: iter, somente_maiusculas: bool = True) -> str:
    """
    Faz inputs até que a resposta do usuário seja válida
    :param texto: O texto a ser exibido na tela
    :param respostas: As respostas válidas
    :param somente_maiusculas: Se for True, as respostas serão totalmente em maiúsculo
    :return: A resposta do Usuário
    """
    respostas = list(respostas)
    while True:
        res = input(texto).strip()
        if somente_maiusculas:
            res = res.upper()
            for i in respostas:
                respostas.remove(i)
                respostas.append(i.upper())
        if res != '' and res in respostas:
            break
        print('Resposta inválida.')
    return res


def trata_acento(*args) -> tuple:
    """
    Para cada item em args, se type(item) == str, retira os acentos das letras em item.
    :param args: Os textos para retirar os acentos.
    :return: Retorna args, tendo os acentos retirados dos textos.
    """
    args = list(args)
    for indice in range(len(args)):
        if type(args[indice]) == str:
            for letter in A_ESPECIAL:
                args[indice].replace(letter.lower(), 'a')
                args[indice].replace(letter.lower(), 'A')
            for letter in E_ESPECIAL:
                args[indice].replace(letter.lower(), 'e')
                args[indice].replace(letter.lower(), 'E')
            for letter in I_ESPECIAL:
                args[indice].replace(letter.lower(), 'i')
                args[indice].replace(letter.lower(), 'I')
            for letter in O_ESPECIAL:
                args[indice].replace(letter.lower(), 'o')
                args[indice].replace(letter.lower(), 'O')
            for letter in U_ESPECIAL:
                args[indice].replace(letter.lower(), 'u')
                args[indice].replace(letter.lower(), 'U')
    return tuple(args)


def trata_ponto(*args) -> tuple:
    """
    Para cada item em args, se type(item) == str, retira os pontos em item.
    :param args: Os textos para retirar os pontos.
    :return: Retorna args, tendo os pontos retirados dos textos.
    """
    args = list(args)
    for texto in args:
        if type(texto) == str:
            for ponto in punctuation:
                texto.replace(ponto, ' ')
    return tuple(args)


def split_nth(iteravel: iter, n: int) -> list:
    """
    Divide o iteravel a cada n itens
    :param iteravel: O iterável para ser partido
    :param n: A quantidade de itens em cada fatia
    :return: Uma lista com as partes do iteravel
    """
    return [iteravel[i:i + n] for i in range(0, len(list(iteravel)), n)]


@dispatch(str, int)
def codifica(texto, repeticoes_maximas) -> str:
    """
    Codifica um texto de várias veezes de forma diferente.
    :param texto: O texto a ser codificado
    :param repeticoes_maximas: O número máximo de repetições a serem realizadas
    :return: O texto codificado
    """
    texto = trata_acento(texto)[0]
    rands = []
    repeticoes_maximas = max(10, repeticoes_maximas)
    for _ in range(randint(10, repeticoes_maximas)):
        rands.append(randint(1, 2))
        texto = codifica(texto, rands[-1], 1)
    texto = codifica(texto, 3, 1)
    rands = [str(rand) for rand in rands]
    rands = ''.join(rands)
    texto = rands + '()' + texto
    return texto


@dispatch(str)
def codifica(texto) -> str:
    """
    Executa 'codifica(texto, 20)'
    :param texto: O texto a ser codificado
    :return: O texto codificado
    """
    return codifica(texto, 20)


@dispatch(str, int, int)
def codifica(texto, modo, repetir) -> str:
    """
    Codifica um texto de uma maneira específica
    :param texto: O texto a ser codificado
    :param modo:
    1 => Troca as letras em um padrão definido
    2 => Embaralha as letras do texto
    3 => Código Morse
    4 => Substitui as letras por números primos
    5 => Utiliza o código dos caracteres
    :param repetir: O número de vezes que a codificação deve ser repetida
    :return: O texto codificado
    """
    texto = trata_acento(texto)[0]

    # Alfabeto + 1
    if modo == 1:
        repetir = repetir % len(CODABLE)
        dic = str.maketrans({CODABLE[num - repetir]: CODABLE[num] for num in range(len(CODABLE))})
        texto = texto.translate(dic)
    # Embaralha
    if modo == 2:
        for _ in range(repetir):
            texto = texto[1::2] + texto[::2]
    # Morse
    if modo == 3:
        dic = str.maketrans({code[0]: code[1] for code in MORSE_COMPLETO})
        resultado = [let.translate(dic) for let in list(texto)]
        texto = ' '.join(resultado)
    # Primos
    if modo == 4:
        texto = trata_ponto(texto)[0]
        nums = [f"{num:2}".replace(' ', '0') for num in ([1] + primos_ate(100))]
        codes = str.maketrans({letra: num for num, letra in zip(nums, ascii_lowercase)})
        texto = texto.translate(codes)
    # Unicode
    if modo == 5:
        def unicode(char):
            return str(ord(char)) + ' '

        texto = ''.join(map(unicode, texto))

    return texto


@dispatch(str)
def decodifica(texto) -> str:
    """
    Decodifica um texto que foi codificado utilizando codifica()
    :param texto: O texto para ser decodificado
    :return: O texto decoficado
    """
    texto = texto.split('()')
    execucoes = [int(num) for num in texto[0]]
    texto = texto[1]
    texto = decodifica(texto, 3, 1)
    while execucoes:
        execucao = execucoes.pop()
        texto = decodifica(texto, execucao, 1)
    return texto


@dispatch(str, int, int)
def decodifica(texto, modo, repetir) -> str:
    """
    Decodifica um texto que foi codificado utilizando codifica()
    :param texto: O texto para ser decodificado
    :param modo:
    1 => Troca as letras em um padrão definido
    2 => Embaralha as letras do texto
    3 => Código Morse
    4 => Substitui as letras por números primos
    5 => Utiliza o código dos caracteres
    :param repetir: O número de vezes que a decodificação deve ser repetida
    :return: O texto decodificado
    """

    # Alfabeto + 1
    if modo == 1:
        repetir = repetir % len(CODABLE)
        dic = str.maketrans({CODABLE[num]: CODABLE[num - repetir] for num in range(len(CODABLE))})
        texto = texto.translate(dic)
    # Embaralha
    if modo == 2:
        for _ in range(repetir):
            metade = int(len(texto) / 2)
            a = texto[:metade]
            b = texto[metade:]
            new = "".join(b[i] + a[i] for i in range(metade))
            if len(texto) % 2:
                new += texto[-1]
            texto = new
    # Morse
    if modo == 3:
        resultado = []
        texto = texto.split()
        for letra in texto:
            for code in MORSE_COMPLETO:
                if letra == code[1]:
                    resultado.append(code[0])
                    break
            else:
                resultado.append(letra)

        texto = ''.join(resultado)
    # Primos
    if modo == 4:
        nums = [f"{num:2}".replace(' ', '0') for num in ([1] + primos_ate(100))]
        codes = tuple((num, letra) for num, letra in zip(nums, ascii_lowercase))
        texto = split_nth(texto, 2)
        res = ''

        for num in texto:
            if num == '  ':
                res += ' '
                continue
            for cd in codes:
                if cd[0] == str(num):
                    res += cd[1]
                    break
        texto = res
    # Unicode
    if modo == 5:
        texto = ''.join(map(chr, [int(code) for code in texto.split()]))

    return texto


def udir(objeto: object) -> list[str]:
    """
    Executa a função dir(objeto) e retorna somente as propriedades e/ou métodos que não começam com '__'
    :param objeto: O objeto que deve ser utilizado
    :return: Uma lista com as propriedades e/ou métodos que não começam com '__'
    """
    lista = []
    for i in dir(objeto):
        if not i.startswith('__'):
            lista.append(i)
    return lista


def mais_repetidas(iterable: iter, quantidade_de_itens: int = 3, quantidade_minima: int = 0) -> list:
    """
    Busca os itens mais repetidos em um iterável
    :param iterable: O iterável para fazer a busca
    :param quantidade_de_itens: A quantidade de itens que deve ser retonada
    :param quantidade_minima: A quantidade mínima de vezes que um item deve aparecer para ser retornado
    :return: Uma lista com os itens mais repetidos seguindo as regras acima
    """
    text = list(set(iterable))
    text.sort(key=list(iterable).count, reverse=True)
    text = [item for item in text if text.count(item) >= quantidade_minima]
    return text[:quantidade_de_itens]


def inverte_dict(dicionario: dict) -> dict:
    """
    Inverte um dicionário da seguinte maneira: {chave1: valor1, chave2: valor2} -> {valor1: chave1, valor2: chave2}
    :param dicionario: O dicionário que deve ser invertido
    :return: O novo dicionário
    """
    return {v: k for k, v in dicionario.items()}


def alphalen(iterable: iter) -> int:
    """
    Retorna  o tamanho do iteravel contando somente os itens que satisfazem item.isaplha()
    :param iterable: O iterável que deverá ser contado
    :return: A quantidade de itens alfabéticos contidos nesse iterável
    """
    alen = 0
    for digit in iterable:
        if digit.isalpha():
            alen += 1
    return alen


def sort_2_keys(__iter: iter, primary: callable, secondary: callable, reverse: bool = False):
    """
    Retorna o uma lista ordenada com base em uma chave primária e uma secundária
    :param __iter: O iterável para ser ordenado
    :param primary: A chave primária de checagem
    :param secondary: A chave secundária de checagem
    :param reverse: Se for verdadeiro, a lista será ordenada do maior para o menor
    :return: A lista ordenada
    """
    __iter = sorted(__iter, key=secondary, reverse=reverse)
    return sorted(__iter, key=primary, reverse=reverse)


def get_all_files(directory: str, extension: str = '*', start_string: str = './', ignore_file='') -> str:
    """
    Busca todos os arquivos em 'directory' e em todos os subdiretórios com a extensão 'extension'.
    :param directory: O diretório base para a busca
    :param extension: A extensão dos arquivos que devem ser buscadas ('*' busca todos os arquivos)
    :param start_string: O texto que deve ser colocado antes do nome do arquivo
    :param ignore_file: Arquivo listando os diretórios e arquivos que não devem ser considerados should not b
    :return: Todos os arquivos em 'directory' e em todos os subdiretórios com a extensão 'extension'
    """

    try:
        with open(ignore_file) as file:
            ignored = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        ignored = []

    try:
        list_this = listdir(directory)
    except NotADirectoryError:
        return []
    if 'pyvenv.cfg' in list_this:
        pass
    else:
        if directory in ignored:
            return []
        if directory.endswith('/') or directory.endswith('\\'):
            directory = directory[:-1]

        for thing in list_this:
            condition = thing.endswith(f'.{extension}') and thing not in ignored
            if extension == '*':
                condition = thing.count('.') > 0 and thing not in ignored

            if condition:
                yield start_string + thing
            elif '.' not in thing:
                for nxt in get_all_files(path.join(directory, thing), extension, f'{start_string + thing}/'):
                    yield nxt


def dicionario_portugues() -> list[str]:
    """
    Busca um dicionário de palavras da língua portuguesa e retorna uma lista com todas as palavras
    Origem: <https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt>
    :return: Uma lista com mais de 320.000 palavras da língua portuguesa
    """

    arq = "https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt"
    src = get(arq)

    if src.status_code != 200:
        raise FileNotFoundError(f"O arquivo de origem ({arq}) não foi encontrado.")

    return src.text.split('\n')


def desempacota_listas(lista: list) -> list:
    """
    Desempacota um conjunto de listas uma dentro da outra e retorna em uma lista só
    :param lista: A lista inicial, possivelmente contendo outras listas
    :return: Uma lista única que não contem outras listas
    """
    new = []
    for i in lista:
        if type(i) == list:
            new.extend(desempacota_listas(i))
        else:
            new.append(i)
    return new


def get_pixels(img_path: str, cor: tuple[int]) -> tuple[int]:
    """
    Retorna todos os pixels de uma determinada cor contidos na imagem especificada
    :param img_path: O caminho relativo para a imagem 
    :param cor: A cor do pixel a ser procurado no formato (r, g, b) [0-255]
    :return: Tuplas (x, y) representando as coordenadas dos pixels 
    """
    img = imread(img_path)
    height = len(img)
    width = len(img[0])
    for x in range(width):
        for y in range(height):
            if img[y][x] == cor:
                yield x, y


def esteganografia(texto: str, file_name: str = 'esteganografia.png', override: bool = False):
    def codificar():
        image = Image.new('RGB', (len(texto), 1))
        image.save(file_name, file_name[-3:].upper())
        image = imread(file_name)
        for x in range(len(texto)):
            image.itemset((0, x, 2), ord(texto[x]))
            image.itemset((0, x, 1), ord(texto[x]))
            image.itemset((0, x, 0), ord(texto[x]))
        imwrite(file_name, image)

    def traduzir():
        image = imread(file_name)
        text = ''
        for x in range(len(image[0])):
            text += chr(image.item(0, x, 0))
        return text

    try:
        if override:
            raise TypeError
        return traduzir()
    except TypeError:
        codificar()


def all_key(_iterable: iter, key: Callable):
    res = [key(x) for x in _iterable]
    return all(res)


def any_key(_iterable: iter, key: Callable):
    res = [key(x) for x in _iterable]
    return any(res)
