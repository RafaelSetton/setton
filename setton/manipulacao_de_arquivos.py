from io import UnsupportedOperation, TextIOWrapper


class File(TextIOWrapper):
    def __init__(self, file: str, mode: str = 'r', encoding: str = None):
        self.__file = open(file, f'{mode}b', encoding=encoding)
        super().__init__(self.__file, encoding)

    @property
    def numero_de_linhas(self):
        self.__file.seek(0)
        return self.__file.read().count(b'\n') + 1

    def insere(self, indice, texto):
        if self.__file.writable():
            self.__file.seek(0)
            text = list(self.__file.read())
            text.insert(indice, bytes(texto, self.encoding))
            text = b''.join(text)
            self.__file.seek(0)
            self.__file.write(text)
        else:
            raise UnsupportedOperation("O arquivo não está em modo de escrita")

    def bkspc(self, indice):
        if self.__file.writable():
            self.__file.seek(0)
            text = list(self.__file.read())
            text.pop(indice)
            text = b''.join(text)
            self.__file.write(text)
        else:
            raise UnsupportedOperation("O arquivo não está em modo de escrita")

    def busca_indices(self, termo, case_sensitive=False):
        self.__file.seek(0)
        leitura = self.__file.read()
        if not case_sensitive:
            termo = termo.lower()
            leitura = leitura.lower()
        tamanho = len(termo)
        indexes = []
        for indice in range(len(leitura)):
            if leitura[indice:indice + tamanho] == bytes(termo, self.encoding):
                indexes.append(indice)
        return indexes

    def conta_ocorrencias(self, termo, case_sensitive=False):
        return len(self.busca_indices(termo, case_sensitive))
