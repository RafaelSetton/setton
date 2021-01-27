from setton.matematica import *
from math import pi
import unittest


class AlgarismosRomanosTests(unittest.TestCase):
    def test_para_romanos(self):
        self.assertEqual(AlgarismosRomanos.para_romanos(2847), "MMDCCCXLVII")

    def test_de_romanos(self):
        self.assertEqual(AlgarismosRomanos.de_romanos("MCXLIV"), 1144)


class CelsiusFahrenheitTests(unittest.TestCase):
    def test_to_celsius(self):
        self.assertEqual(CelsiusFahrenheit.to_celsius(95), 35)

    def test_to_fahrenheit(self):
        self.assertEqual(CelsiusFahrenheit.to_fahrenheit(30), 86)


class RadianosGrausTests(unittest.TestCase):
    def test_para_graus(self):
        self.assertAlmostEqual(RadianosGraus.para_graus(pi), 180, places=3)
        self.assertAlmostEqual(RadianosGraus.para_graus(pi / 3), 60, places=3)

    def test_para_radianos(self):
        self.assertAlmostEqual(RadianosGraus.para_radianos(180), pi, places=3)
        self.assertAlmostEqual(RadianosGraus.para_radianos(45), pi / 4, places=3)


class OtherTests(unittest.TestCase):
    def test_maior_primo_ate(self):
        self.assertEqual(maior_primo_ate(97), 97)
        self.assertEqual(maior_primo_ate(102), 101)

    def test_primos_ate(self):
        self.assertEqual(primos_ate(15), [2, 3, 5, 7, 11, 13])
        self.assertEqual(primos_ate(17), [2, 3, 5, 7, 11, 13, 17])

    def test_primo(self):
        self.assertTrue(primo(97))
        self.assertFalse(primo(102))

    def test_limite(self):
        self.assertEqual(limite(100, 0, 60), 60, "Valor dentro do limite")
        self.assertEqual(limite(100, 0, 600), 100, "Valor acima do limite")
        self.assertEqual(limite(100, 0, -3), 0, "Valor abaixo do limite")

    def test_resolve_funcao_quadratica(self):
        self.assertEqual(resolve_funcao_quadratica(1, 2, 1), '-1')
        self.assertEqual(resolve_funcao_quadratica(1, 1, 0.25), '-1/2')
        self.assertEqual(resolve_funcao_quadratica(1, 6, 5), '-5, -1')
        self.assertEqual(resolve_funcao_quadratica(1, 0, -0.25), '-1/2, 1/2')
        self.assertEqual(resolve_funcao_quadratica(3, 5, -1), '(-5 - sqrt(37)) / 6, (-5 + sqrt(37)) / 6')
        self.assertRaises(ValueError, lambda: resolve_funcao_quadratica(0, 1, 2))
        self.assertRaises(ValueError, lambda: resolve_funcao_quadratica(1, 0, 1))

    def test_simplify_polinomial(self):
        self.assertEqual(simplify_polynomial("x + 2y - 3x"), "-2x+2y")

    def test_soma_pg(self):
        self.assertEqual(soma_pg(1, 3, 5), 121)

    def test_somatoria(self):
        self.assertEqual(somatoria(10), 55)
        self.assertEqual(somatoria(5, 10), 45)
        self.assertEqual(somatoria(3, 9, 2), 24)


if __name__ == '__main__':
    unittest.main()
