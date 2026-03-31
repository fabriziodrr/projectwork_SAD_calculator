import unittest
import math
# Importiamo la funzione dal tuo file arcoseno.py
from arcoseno import calcola_arcoseno

class TestArcoseno(unittest.TestCase):

    def test_valori_limite(self):
        """Verifica i confini del dominio [-1, 1]"""
        # arcsin(1) deve restituire 90 gradi
        self.assertAlmostEqual(calcola_arcoseno(1), 90.0)
        # arcsin(-1) deve restituire -90 gradi
        self.assertAlmostEqual(calcola_arcoseno(-1), -90.0)
        # arcsin(0) deve restituire 0 gradi
        self.assertAlmostEqual(calcola_arcoseno(0), 0.0)

    def test_valori_noti(self):
        """Verifica angoli trigonometrici standard"""
        # arcsin(0.5) deve essere 30 gradi
        self.assertAlmostEqual(calcola_arcoseno(0.5), 30.0)
        # arcsin(sqrt(2)/2) deve essere 45 gradi
        valore_45 = math.sqrt(2) / 2
        self.assertAlmostEqual(calcola_arcoseno(valore_45), 45.0)

    def test_fuori_dominio(self):
        """Verifica che la funzione gestisca correttamente input errati"""
        errore_atteso = "Errore: l'input deve essere compreso tra -1 e 1"
        self.assertEqual(calcola_arcoseno(1.5), errore_atteso)
        self.assertEqual(calcola_arcoseno(-1.1), errore_atteso)

if __name__ == '__main__':
    unittest.main()