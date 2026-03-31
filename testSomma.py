import unittest
from unittest.mock import patch
from addizione import calcola_somma_utente

class TestSommaUtente(unittest.TestCase):

    @patch('builtins.print') # Silenzia l'output
    @patch('builtins.input', side_effect=['3', '10', '20', '5.5'])
    def test_somma_tre_valori(self, mock_input, mock_print):
        risultato = calcola_somma_utente()
        self.assertEqual(risultato, 35.5)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '0', '-5'])
    def test_somma_valori_negativi(self, mock_input, mock_print):
        risultato = calcola_somma_utente()
        self.assertEqual(risultato, -5.0)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['0'])
    def test_quantita_zero(self, mock_input, mock_print):
        risultato = calcola_somma_utente()
        self.assertEqual(risultato, 0)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['abc'])
    def test_input_non_valido(self, mock_input, mock_print):
        risultato = calcola_somma_utente()
        self.assertIsNone(risultato)

if __name__ == '__main__':
    unittest.main()