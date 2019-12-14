import unittest
import hello_world

class test_hello_world(unittest.TestCase):

    def test_wyswietlenie(self):
        wynik = hello_world.tekst()
        self.assertEqual(wynik, 'Hello World')

if __name__ == '__main__':
    unittest.main()
