import unittest
import moj_kalkulator

class test_kalkulator(unittest.TestCase):

    def test_dodawanie(self):
        wynik = moj_kalkulator.dodaj(2,3)
        self.assertEqual(wynik, 5)
        self.assertNotEqual(wynik,2)

    def test_odejmowanie(self):
        wynik = moj_kalkulator.odejmij(8,6)
        self.assertEqual(wynik, 2)
        self.assertNotEqual(wynik, 14)

    def test_mnozenie(self):
        wynik = moj_kalkulator.pomnoz(2,3)
        self.assertEqual(wynik, 6)
        self.assertNotEqual(wynik, 5)

    def test_dzielenie(self):
        wynik = moj_kalkulator.podziel(8,2)
        self.assertEqual(wynik, 4)
        self.assertNotEqual(wynik, 9)

if __name__ == '__main__':
    unittest.main()
