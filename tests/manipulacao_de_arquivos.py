from setton.manipulacao_de_arquivos import *
from os import remove
import unittest


class FileTests(unittest.TestCase):
    file: File

    @classmethod
    def setUpClass(cls) -> None:
        cls.file = File("./test_file.txt")
        cls.original_text = "File created for testing.\n" + \
                            "Just some random text\n" + \
                            "\tand some more...\n"

    def setUp(self) -> None:
        self.file.seek(0)
        self.file.clear()
        self.file.overwrite(self.original_text)

    def test_backspace(self):
        self.file.seek(15)

        for _ in range(4):
            self.file.backspace()
        self.file.seek(0)
        self.assertEqual(self.file.read(), self.original_text[:12] + self.original_text[16:])

    def test_busca_indices(self):
        self.assertEqual(self.file.busca_indices("some"), [31, 53])

    def test_conta_ocorrencias(self):
        self.assertEqual(self.file.conta_ocorrencias(" "), 8)

    def test_insere(self):
        self.file.seek(0)
        self.file.insert('begining: ')
        self.assertEqual(self.file.read(), 'begining: ' + self.original_text)

    def test_numero_de_linhas(self):
        self.assertEqual(self.file.numero_de_linhas, 4)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.file.close()
        remove("./test_file.txt")


if __name__ == '__main__':
    unittest.main()
