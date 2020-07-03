from multipledispatch import dispatch
from threading import Thread
from keyboard import wait
from random import randint
from os import listdir, path
from setton.constantes import A_ESPECIAL, E_ESPECIAL, I_ESPECIAL, O_ESPECIAL, U_ESPECIAL, PONTUACAO
from setton.constantes import ALFABETO_MINUSCULO, MORSE_COMPLETO, CODABLE
from setton.matematica import primos_ate
from requests import get


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


def keyboard_listener(dic_funcs: dict) -> None:
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
    for indice, texto in enumerate(args):
        if type(texto) == str:
            texto = list(texto)
            for i, l in enumerate(texto):
                if l in A_ESPECIAL:
                    if l.islower():
                        texto[i] = 'a'
                    else:
                        texto[i] = 'A'
                if l in E_ESPECIAL:
                    if l.islower():
                        texto[i] = 'e'
                    else:
                        texto[i] = 'E'
                if l in I_ESPECIAL:
                    if l.islower():
                        texto[i] = 'i'
                    else:
                        texto[i] = 'I'
                if l in O_ESPECIAL:
                    if l.islower():
                        texto[i] = 'o'
                    else:
                        texto[i] = 'O'
                if l in U_ESPECIAL:
                    if l.islower():
                        texto[i] = 'u'
                    else:
                        texto[i] = 'U'
            args[indice] = ''.join(texto)
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
            for ponto in PONTUACAO:
                texto.replace(ponto, ' ')
    return tuple(args)


def split_nth(iteravel: iter, n: int) -> list:
    """
    Divide o iteravel a cada n itens
    :param iteravel: O iterável para ser partido
    :param n: A quantidade de itens em cada fatia
    :return: Uma lista com as partes do iteravel
    """
    return [iteravel[i:i + n] for i in range(0, len(iteravel), n)]


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
    4 => Substitui as letras por números
    :param repetir: O número de vezes que a codificação deve ser repetida
    :return: O texto codificado
    """
    texto = trata_acento(texto)[0]

    # Alfabeto + 1
    if modo == 1:

        repetir = repetir % len(CODABLE)

        lista = list(texto)
        dic = {CODABLE[num-repetir]: CODABLE[num] for num in range(len(CODABLE))}
        codificado = []
        for letter in lista:
            try:
                codificado.append(dic[letter])
            except KeyError:
                codificado.append(letter)
        texto = ''.join(codificado)
    # Embaralha
    if modo == 2:
        for _ in range(repetir):
            texto = texto[1::2] + texto[::2]
    # Morse
    if modo == 3:
        resultado = []
        original = list(texto)
        for letra in original:
            for code in MORSE_COMPLETO:
                if letra == code[0]:
                    resultado.append(code[1])
        texto = '|'.join(resultado)
    # Primos
    if modo == 4:
        texto = trata_ponto(texto)[0]

        nums = [f"{num:2}".replace(' ', '0') for num in ([1] + primos_ate(100))]
        codes = tuple((num, letra) for num, letra in zip(nums, ALFABETO_MINUSCULO))
        res = ''

        for num in texto:
            if num == ' ':
                res += '  '
                continue
            for cd in codes:
                if cd[1] == str(num):
                    res += cd[0]
                    break
        texto = res
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
    4 => Substitui as letras por números
    :param repetir: O número de vezes que a decodificação deve ser repetida
    :return: O texto decodificado
    """

    # Alfabeto + 1
    if modo == 1:
        repetir = repetir % len(CODABLE)

        lista = list(texto)
        dic = {CODABLE[num]: CODABLE[num-repetir] for num in range(len(CODABLE))}
        decodificado = []
        for letter in lista:
            try:
                decodificado.append(dic[letter])
            except KeyError:
                decodificado.append(letter)
        texto = ''.join(decodificado)
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
        texto = texto.split('|')
        for letra in texto:
            for code in MORSE_COMPLETO:
                if letra == code[1]:
                    resultado.append(code[0])
                else:
                    pass
        texto = ''.join(resultado)
    # Primos
    if modo == 4:

        nums = [f"{num:2}".replace(' ', '0') for num in ([1] + primos_ate(100))]
        codes = tuple((num, letra) for num, letra in zip(nums, ALFABETO_MINUSCULO))
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

    return texto


def udir(objeto: object) -> list:
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
    text.sort(key=lambda x: iterable.count(x), reverse=True)
    text = [item for item in text if text.count(item) >= quantidade_minima]
    return text[:quantidade_de_itens]


def list_replace(lista: list, old, new) -> list:
    """
    Substitui um item em uma lista
    :param lista: A lista que deveser alterada
    :param old: O item que deve ser trocado
    :param new: O novo item que deve ser inserido
    :return: A lista alterada
    """
    while old in lista:
        ind = lista.index(old)
        lista[ind] = new
    return lista


def inverte_dict(dicionario: dict) -> dict:
    """
    Inverte um dicionário da seguinte maneira: {chave1: valor1, chave2: valor2} -> {valor1: chave1, valor2: chave2}
    :param dicionario: O dicionário que deve ser invertido
    :return: O novo dicionário
    """
    return {dicionario[key]: key for key in dicionario.keys()}


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


# STOPEI AKI


def get_all_files(directory: str, extension: str = '*', start_string: str = './') -> str:
    """
    Busca todos os arquivos em 'directory' e em todos os subdiretórios com a extensão 'extension'.
    :param directory: O diretório base para a busca
    :param extension: A extensão dos arquivos que devem ser buscadas ('*' busca todos os arquivos)
    :param start_string: O texto que deve ser colocado antes do nome do arquivo
    :return: Todos os arquivos em 'directory' e em todos os subdiretórios com a extensão 'extension'
    """
    if 'pyvenv.cfg' in listdir(directory):
        pass
    else:
        if directory.endswith('/') or directory.endswith('\\'):
            directory = directory[:-1]

        for thing in listdir(directory):
            condition = thing.endswith(f'.{extension}')
            if extension == '*':
                condition = thing.count('.') > 0

            if condition:
                yield start_string+thing
            elif '.' not in thing:
                for nxt in get_all_files(path.join(directory, thing), extension, f'{start_string+thing}/'):
                    yield nxt


def dicionario_portugues() -> list:
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


if __name__ == '__main__':
    with open('utils.py') as file:
        funcs = []
        for line in file:
            if line.startswith('def '):
                par = line.index('(')
                funcs.append(line[4:par])
        print(set(funcs))
