import os
import sys
# Aggiunge la cartella del progetto al PYTHONPATH per eseguire i test sia da root sia direttamente
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import unittest
from unittest.mock import patch
from src.arcocoseno import calcola_arcocoseno_utente

class TestArcocosenoUtente(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3', '1', '0', '-1'])
    def test_arcocoseno_valori_noti(self, mock_input, mock_print):
        """
        Testa l'arcocoseno di 1, 0 e -1.
        Ci aspettiamo [0.0, 90.0, 180.0] gradi.
        """
        risultato = calcola_arcocoseno_utente()
        self.assertEqual(risultato, [0.0, 90.0, 180.0])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', '1.5'])
    def test_valore_fuori_dominio(self, mock_input, mock_print):
        """
        Testa il comportamento con un input > 1 (non valido per acos).
        """
        risultato = calcola_arcocoseno_utente()
        self.assertIsNone(risultato)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['0'])
    def test_quantita_zero(self, mock_input, mock_print):
        """
        Testa l'inserimento di 0 come quantità di elementi.
        """
        risultato = calcola_arcocoseno_utente()
        self.assertEqual(risultato, [])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['test_stringa'])
    def test_input_non_valido(self, mock_input, mock_print):
        """
        Testa la gestione di stringhe non numeriche.
        """
        risultato = calcola_arcocoseno_utente()
        self.assertIsNone(risultato)

if __name__ == '__main__':
    unittest.main()