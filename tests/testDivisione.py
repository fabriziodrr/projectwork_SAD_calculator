import os
import sys
# Aggiunge la cartella del progetto al PYTHONPATH per eseguire i test sia da root sia direttamente
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import unittest
from unittest.mock import patch
from src.divisione import calcola_divisione_utente

class TestDivisioneUtente(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3', '100', '2', '5'])
    def test_divisione_standard(self, mock_input, mock_print):
        """
        Testa 100 / 2 / 5 = 10.0
        """
        risultato = calcola_divisione_utente()
        self.assertEqual(risultato, 10.0)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '50', '0'])
    def test_divisione_per_zero(self, mock_input, mock_print):
        """
        Testa il comportamento quando il divisore è zero (deve restituire None).
        """
        risultato = calcola_divisione_utente()
        self.assertIsNone(risultato)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', '10'])
    def test_singolo_valore(self, mock_input, mock_print):
        """
        Se inserisco un solo valore, il risultato deve essere il valore stesso.
        """
        risultato = calcola_divisione_utente()
        self.assertEqual(risultato, 10.0)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['invalid'])
    def test_input_non_numerico(self, mock_input, mock_print):
        """
        Testa l'inserimento di stringhe invece di numeri.
        """
        risultato = calcola_divisione_utente()
        self.assertIsNone(risultato)

if __name__ == '__main__':
    unittest.main()