import unittest 

def factorial(n):
    if n == 1:
        return 1 
    resultado = n * factorial(n-1)
    return resultado 

class TestFactorial(unittest.TestCase):
    
    def test_con_1(self):
        resultado = factorial(1)
        self.assertEqual(resultado, 1)

    def test_con_2(self):
        resultado = factorial(2)
        self.assertEqual(resultado, 2)

    def test_con_3(self):
        resultado = factorial(3)
        self.assertEqual(resultado, 6)

    unittest.main()
