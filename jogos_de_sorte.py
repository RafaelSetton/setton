from random import choice, randint


def pedra_papel_tesoura():
    jogadas = ['pedra', 'papel', 'tesoura']
    jogada_usuario = input('Você está jogando pedra papael e tesoura. Qual a sua jogada? ').lower().strip()
    if jogada_usuario not in jogadas:
        return f'Jogada inválida. A sua jogada deve estar entre as seguintes: {jogadas}'
    jogada_computador = choice(jogadas)
    resultado = (jogada_usuario[0:2], jogada_computador[0:2])
    if jogada_usuario == jogada_computador:
        return f'Empate: Ambos jogaram {jogada_usuario}'
    elif resultado == ('pe', 'te'):
        return f'Você venceu: {jogada_usuario} X {jogada_computador}'
    elif resultado == ('pa', 'pe'):
        return f'Você venceu: {jogada_usuario} X {jogada_computador}'
    elif resultado == ('te', 'pa'):
        return f'Você venceu: {jogada_usuario} X {jogada_computador}'
    else:
        return f'Você perdeu: {jogada_usuario} X {jogada_computador}'


def par_impar():
    escolha = input('Você está jogando par ou ímpar. Escolha par ou impar: ').lower().strip()
    escolhas = {'par': 0, 'impar': 1}
    try:
        escolha = escolhas[escolha]
    except KeyError:
        return 'Jogada inválida: Você deve escolher par ou impar'
    jogada_usuario = input('Qual é a sua jogada? Ela deve ser um inteiro entre 0 e 10 ')
    if len(jogada_usuario) > 1:
        return 'Jogada inválida: A jogada deve ser um inteiro positivo menor que 10.'
    try:
        jogada_usuario = int(jogada_usuario)
    except ValueError:
        return 'Jogada inválida: A jogada deve ser um inteiro entre 0 e 10.'
    jogada_computador = randint(0, 10)
    result = jogada_computador + jogada_usuario
    if result % 2 == escolha:
        return f'Você venceu! \nResultado: {result}'
    else:
        return f'Você perdeu! \nResultado: {result}'


def dado(lados):
    return choice(range(lados)) + 1
