import os
import sys
# Aggiunge la cartella del progetto al PYTHONPATH per eseguire i test sia da root sia direttamente
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import unittest
import math
# Importiamo la funzione dal tuo file seno.py
from src.seno import calcola_seno

class TestSeno(unittest.TestCase):

    def test_valori_fondamentali(self):
        """Verifica i punti cardine della funzione seno"""
        # Seno di 0 gradi  deve essere 0.0
        self.assertAlmostEqual(calcola_seno(0), 0.0, places=7)
        
        # Seno di 90 gradi deve essere 1.0
        self.assertAlmostEqual(calcola_seno(90), 1.0, places=7)
        
        # Seno di 180 gradi deve essere 0.0
        self.assertAlmostEqual(calcola_seno(180), 0.0, places=7)
        
        # Seno di 270 gradi deve essere -1.0
        self.assertAlmostEqual(calcola_seno(270), -1.0, places=7)

    def test_angoli_noti(self):
        """Verifica angoli con valori frazionari noti"""
        # Seno di 30 gradi è 0.5
        self.assertAlmostEqual(calcola_seno(30), 0.5, places=7)

    def test_angoli_negativi(self):
        """Verifica la simmetria (seno è una funzione dispari)"""
        # Seno di -90 gradi è -1.0
        self.assertAlmostEqual(calcola_seno(-90), -1.0, places=7)

if __name__ == '__main__':
    unittest.main()