import unittest
from unittest.mock import patch
from coseno import calcola_coseno_utente

class TestCosenoUtente(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3', '0', '90', '180'])
    def test_coseno_angoli_noti(self, mock_input, mock_print):
        """
        Testa il coseno di 0, 90 e 180 gradi.
        """
        risultato = calcola_coseno_utente()
        # Ci aspettiamo [1.0, 0.0, -1.0]
        self.assertEqual(risultato, [1.0, 0.0, -1.0])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['0'])
    def test_quantita_zero(self, mock_input, mock_print):
        """
        Se l'utente inserisce 0, deve restituire una lista vuota.
        """
        risultato = calcola_coseno_utente()
        self.assertEqual(risultato, [])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['invalid'])
    def test_input_non_numerico(self, mock_input, mock_print):
        """
        Testa l'inserimento di testo.
        """
        risultato = calcola_coseno_utente()
        self.assertIsNone(risultato)

if __name__ == '__main__':
    unittest.main()