from setton.utils import *
from setton.constantes import CODABLE
from random import choices, randint
from os import remove
import unittest


class EncryptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ''.join(choices(String(CODABLE) - r'\ ' + ' ', k=randint(1, 20)))
    
    def test_main(self):
        self.assertEqual(decodifica(codifica(self.text)), self.text)

    def test_mode_1(self):
        self.assertEqual(decodifica(codifica(self.text, 1, 1), 1, 1), self.text)
    
    def test_mode_2(self):
        self.assertEqual(decodifica(codifica(self.text, 2, 1), 2, 1), self.text)
    
    def test_mode_3(self):
        self.assertEqual(decodifica(codifica(self.text, 3, 1), 3, 1), self.text)
    
    def test_mode_4(self):
        self.assertEqual(decodifica(codifica(self.text, 4, 1), 4, 1), self.text)
    
    def test_mode_5(self):
        self.assertEqual(decodifica(codifica(self.text, 5, 1), 5, 1), self.text)


class IterableTests(unittest.TestCase):
    def test_alphalen(self):
        self.assertEqual(String("a1s3dkx2 al").alphalen(), 7)
        self.assertEqual(List("a1s3dkx2 al").alphalen(), 7)


class ListTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.object = List("random characteres to test class")

    def test_class(self):
        self.assertIsInstance(self.object, List)
        self.assertIsInstance(self.object.copy(), List)

    def test_replace(self):
        self.assertEqual(self.object.copy()._replace("s", "5"), List("random charactere5 to te5t cla55"))

    def test_remove_all(self):
        self.assertEqual(self.object.copy()._remove("s"), List("random charactere to tet cla"))

    def test_remove_some(self):
        self.assertEqual(self.object.copy()._remove("s", 2), List("random charactere to tet class"))

    def test_sub(self):
        self.assertEqual(self.object - ['o', 'e'], List("randm charactrs t tst class"))


class StringTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.object: String = String("random characteres to test class")

    def test_class(self):
        self.assertIsInstance(self.object, String)

    def test_sub(self):
        self.assertEqual(self.object - 'oe', String("randm charactrs t tst class"))

    def test_insert(self):
        new = self.object
        self.assertEqual(new.insert(3, "ola"), String("ranoladom characteres to test class"))

    def test_pop(self):
        new = self.object
        self.assertEqual(new.pop(5), String("rando characteres to test class"))


class OtherTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lista_mais_repetidas = [1, 2, 1, 1, 1, 3, 4, 4, 2, 2, 2, 3, 3, 3, 3, 3]
        cls.lista_any_all_key = [None, 1, 'asd', 3.0, '', 0]

    def test_trata_acento(self):
        self.assertEqual(trata_acento("Água", "café", "pão", "Ônibus", "ir à praça"),
                         ("Agua", "cafe", "pao", "Onibus", "ir a praça"))

    def test_trata_ponto(self):
        self.assertEqual(trata_ponto("Era uma vez, na floresta", "fim de frase.", "indica: isso"),
                         ("Era uma vez  na floresta", "fim de frase ", "indica  isso"))

    def test_split_nth_int(self):
        self.assertEqual(split_nth([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_split_nth_break(self):
        self.assertEqual(split_nth([1, 2, 3, 4, 5, 6, 7, 8], 3), [[1, 2, 3], [4, 5, 6], [7, 8]])

    def test_mais_repetidas_default(self):
        self.assertEqual(mais_repetidas(self.lista_mais_repetidas), [3, 2, 1])

    def test_mais_repetidas_min_occur(self):
        self.assertEqual(mais_repetidas(self.lista_mais_repetidas, quantidade_minima=5), [3])

    def test_inverte_dict(self):
        self.assertDictEqual(inverte_dict({'a': 'b', 1: 2, (3, 4): 7.0}), {'b': 'a', 2: 1, 7.0: (3, 4)})

    def test_sort_2_keys(self):
        self.assertEqual(sort_2_keys(['abc', 'asdkl', 'denj', 'def', 'aaa'], str.__len__, str),
                         ['aaa', 'abc', 'def', 'denj', 'asdkl'])

    def test_desempacote_lista(self):
        self.assertEqual(desempacota_listas([1, [2, 3, [4, [5]], [6, 7]], 8]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_esteganografia(self):
        texto = "Rafael Setton, 20/10/2004, Porto Velho-RO | Brazil"
        file_name = "./test_esteganografia.png"
        esteganografia(texto, file_name)
        result = esteganografia("", file_name)
        remove(file_name)
        self.assertEqual(texto, result)

    def test_all_key(self):
        self.assertEqual(all_key(self.lista_any_all_key, int.__instancecheck__), False)

    def test_any_key(self):
        self.assertEqual(any_key(self.lista_any_all_key, int.__instancecheck__), True)


if __name__ == '__main__':
    unittest.main()
