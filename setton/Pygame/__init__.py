import pygame as pg
pg.init()


class DefaultGame:
    def __init__(self, screen: pg.Surface, screen_name: str = "My Game",
                 screen_icon: pg.Surface = pg.Surface((50, 50), masks=pg.Color(0, 0, 0, 0))):
        self.screen = screen
        self.__screen_name = screen_name
        self.__screen_icon = screen_icon

        pg.display.set_caption(screen_name)
        pg.display.set_icon(screen_icon)

        self.running = False

    # Getters e Setters

    @property
    def width(self):
        return self.screen.get_width()

    @property
    def height(self):
        return self.screen.get_height()

    @property
    def screen_name(self):
        return self.__screen_name

    @screen_name.setter
    def screen_name(self, name: str):
        self.__screen_name = name
        pg.display.set_caption(name)

    @property
    def screen_icon(self):
        return self.__screen_icon

    @screen_icon.setter
    def screen_icon(self, icon: pg.Surface):
        self.__screen_icon = icon
        pg.display.set_icon(icon)

    # Helper Functions

    def carregamento(self, img: pg.Surface, x: int, y: int, criterio_de_parada, surface: pg.Surface,
                     fonte=pg.font.SysFont('Agency FB', 80, True)) -> None:
        surface = surface or self.screen

        def transform(image, topleft, angle):
            rotated_image = pg.transform.rotate(image, angle)
            new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

            return rotated_image, new_rect.topleft

        text = "Carregando "
        rotation = 0
        frames = 0
        clock = pg.time.Clock()
        while not criterio_de_parada:
            if frames % 10 == 0:
                if text.count('.') < 3:
                    text += '.'
                else:
                    text = text[:-3]
            rotation -= 3

            text_img = fonte.render(text, True, (0, 0, 0))
            surface.fill((255, 255, 255))
            surface.blit(*transform(img, (x, y), rotation))
            surface.blit(text_img, (x + 100, y))

            pg.display.update()
            frames += 1
            clock.tick(30)

    # Main Functions

    def events_handler(self) -> list[pg.event.Event]:
        raise NotImplementedError

    def loop(self):
        raise NotImplementedError

