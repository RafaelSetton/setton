import pygame as pg
pg.init()


def grafico_de_linha(surface: pg.Surface, values: list[int, float], cor: tuple[int, int, int],
                     top_left: tuple[int], size: tuple[int], max_value: int = 100):
    coords = list()
    height = size[1] / max_value
    width = size[0] / (len(values) - 1)

    for index, b in enumerate(values):
        coords.append((int(top_left[0] + width * index), int(top_left[1] + size[1] - height * int(b))))

    pg.draw.lines(surface, cor, False, coords, 3)


def grafico_cheio(surface: pg.Surface, values: list[int, float], cor: tuple[int, int, int],
                  top_left: tuple[int], size: tuple[int], max_value: int = 100):
    coords = [(top_left[0] + size[0], top_left[1] + size[1]), (top_left[0], top_left[1] + size[1])]
    height = size[1] / max_value
    width = size[0] / (len(values) - 1)

    for index, b in enumerate(values):
        coords.append((int(top_left[0] + width * index), int(top_left[1] + size[1] - height * b)))

    pg.draw.polygon(surface, cor, coords)
