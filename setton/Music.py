from setton.setton.Tones import a, bfl, c, d, e, f, g, sil, play
from setton.setton.utils import keyboard_listener, valida_resposta, trata_acento
from setton.setton.matematica import limite
from random import choice
from os import listdir, path
from pygame import mixer, error


def coffin_dance():

    def agudo():
        g()
        g(5, 250)
        bfl(6, 250)
        a(6, 250)
        bfl(6, 250)
        a(6, 250)
        bfl(6, 250)

    def prep():
        g()
        g(5, 250)
        d(6, 250)
        c(6)
        bfl()
        a()
        a(5, 250)
        a(5, 250)
        c(6)
        bfl(5, 250)
        a(5, 250)

    def x4():
        notas = [
            lambda: bfl(5, 250),
            lambda: d(6, 250),
            lambda: c(6, 250),
            lambda: f(6, 250),
            lambda: g(6, 250),
            lambda: g(6, 250),
            lambda: g(6, 250),
        ]
        for nota in notas:
            nota()
            nota()
            nota()
            nota()

    def fall():
        c(6, 250)
        bfl(5, 250)
        a(5, 250)
        f(5, 250)

    def geral():
        prep()
        agudo()
        agudo()

    fall()

    geral()
    geral()

    x4()

    fall()

    geral()


def toca_musica(caminho):
    mixer.init()
    mixer.music.load(caminho)
    mixer.music.play()


def toca_musicas_mp3():
    mixer.init()

    caminho = r'C:\Users\rasea\OneDrive\Backup\Musicas\mp3'

    def musica():
        mus = input("Digite o nome da música para tocar: ").split('.')[0].strip().title()
        mus = trata_acento(mus)[0]

        if mus == 'Random':
            mus = choice(listdir(caminho).remove('Adicionar'))[:-4]
        try:
            mixer.music.load(path.join(caminho, mus + '.mp3'))
        except error:
            print(f"A musica {mus} não foi encontrada.")
            adic = valida_resposta("Deseja adicioná-la à lista de desejos? [S/N] ", ["S", "N"])
            if adic == "S":
                with open('C:\\Users\\rasea\\OneDrive\\Backup\\Musicas\\mp3\\Adicionar.txt', mode='r+') as adic:
                    if mus not in adic.read():
                        adic.write(mus+'\n')
        else:
            mixer.music.play()
            keyboard_listener({'+': lambda: mixer.music.set_volume(limite(1, 0, mixer.music.get_volume() + 0.05)),
                               '-': lambda: mixer.music.set_volume(limite(1, 0, mixer.music.get_volume() - 0.05)),
                               '\n': mixer.music.stop})
            input("Para parar, aperte Enter.")
            while mixer.music.get_busy():
                pass

    def alterar_volume():
        vol = int(input(f"Volume atual: {int(mixer.music.get_volume()*100)}. Alterar volume para: [0-100] "))/100
        mixer.music.set_volume(vol)

    def lista(comeco):
        for m in listdir(caminho):
            if m.startswith(comeco) and m.endswith('.Mp3'):
                print(m[:-4])

    while True:
        acao = valida_resposta("O que você deseja fazer? (V) Volume, (M) Música, (L) Listar Músicas ", ["V", "M", "L"])
        if acao == 'V':
            alterar_volume()
        elif acao == "M":
            musica()
        else:
            filtro = input("Somente músicas que começam com: (Deixe em branco para listar todas as músicas) ").title()
            lista(filtro)


def do_re_mi_fa():
    refrao = [c, d, e, f, sil, f, f, sil]
    play(*refrao, c, d, c, d, sil, d, d, sil, c, g, f, e, sil, e, e, sil, *refrao)
