def conta_linhas(arquivo):
    with open(arquivo) as arq:
        count = 1
        for _ in arq:
            count += 1
        return count


# Beta Versions
"""
def insere(arquivo, indice, texto):
    with open(arquivo) as arq:
        text = arq.read()
    text = list(text)
    text.insert(indice, texto)
    text = ''.join(text)
    with open(arquivo, 'w') as arq:
        arq.write(text)


def bkspc(arquivo, indice):
    with open(arquivo) as arq:
        text = arq.read()
    text = list(text)
    text.pop(indice)
    text = ''.join(text)
    with open(arquivo, 'w') as arq:
        arq.write(text)



@forca_tipo(str, str)
def busca_indices(arquivo, termo):
    with open(arquivo) as arq:
        termo = termo.lower()
        leitura = arq.read()
        leitura = leitura.lower()
        tamanho = len(termo)
        for indice, letter in enumerate(leitura):
            if letter == termo[0] and leitura[indice:indice + tamanho] == termo:
                yield indice


@forca_tipo(str, str)
def conta_ocorrencias(arquivo, termo):
    return len(tuple(busca_indices(arquivo, termo)))
"""
