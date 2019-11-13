#criando testes em python com o módulo unittest
import unittest

def fatorial(n):
    if(n == 0):
        return 1
    return n * fatorial(n -1)

def potencia(base, expoente):
    if(expoente == 0):
        return 1
    return base * potencia(base, expoente - 1)


class TestMathMethods(unittest.TestCase):
    def test_potencia(self):
        self.assertEqual(1024, potencia(2,10))

    def test_fatorial(self):
        self.assertEqual(24, fatorial(4))

unittest.main()