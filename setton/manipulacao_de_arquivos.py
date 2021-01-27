from setton.utils import String


class File:
    def __init__(self, file: str, encoding: str = 'ascii'):
        self.__file = open(file, 'w+', encoding=encoding)
        self.__content = String(self.__file.read())
        self.__encoding = encoding
        self.__cursor = 0

    def __del__(self):
        self.close()

    # Basics
    def seek(self, offset: int, whence: int = 0):
        assert whence in (0, 1, 2), "Whence deve ser 0, 1 ou 2"
        if whence == 0:
            self.__cursor = offset
        elif whence == 1:
            self.__cursor += offset
        else:
            self.__cursor = len(self.read()) + offset - 1

    def read(self) -> str:
        return str(self.__content)

    def overwrite(self, text: str):
        self.__content = String(self.__content[:self.__cursor] + text + self.__content[self.__cursor+len(text)+1:])

    def close(self):
        self.__file.close()

    # New
    @property
    def cursor_pos(self):
        return self.__cursor

    @property
    def numero_de_linhas(self):
        return self.__content.count('\n') + 1

    def clear(self):
        self.__content = String()

    def insert(self, text):
        self.__content = self.__content.insert(self.__cursor, text)

    def backspace(self):
        if self.__cursor == 0:
            raise IOError("Impossível executar 'backspace()' em índice 0.")
        self.__content = self.__content.pop(self.__cursor)
        self.seek(-1, 1)

    def busca_indices(self, termo, case_sensitive=False):
        self.seek(0)
        leitura = self.read()
        if not case_sensitive:
            termo = termo.lower()
            leitura = leitura.lower()
        tamanho = len(termo)
        indexes = []
        for indice in range(len(leitura)):
            if leitura[indice:indice + tamanho] == termo:
                indexes.append(indice)
        return indexes

    def conta_ocorrencias(self, termo, case_sensitive=False):
        return len(self.busca_indices(termo, case_sensitive))
