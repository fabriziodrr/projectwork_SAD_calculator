import unittest
from unittest.mock import patch
from tangente import calcola_tangente_utente

class TestTangenteUtente(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3', '0', '45', '180'])
    def test_tangente_valori_noti(self, mock_input, mock_print):
        """
        Testa la tangente di 0, 45 e 180 gradi.
        Ci aspettiamo [0.0, 1.0, 0.0].
        """
        risultato = calcola_tangente_utente()
        self.assertEqual(risultato, [0.0, 1.0, 0.0])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', '90'])
    def test_tangente_non_definita(self, mock_input, mock_print):
        """
        Testa il comportamento a 90 gradi (asintoto).
        Deve restituire None.
        """
        risultato = calcola_tangente_utente()
        self.assertIsNone(risultato)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['0'])
    def test_quantita_zero(self, mock_input, mock_print):
        """
        Testa l'inserimento di 0 come quantità.
        """
        risultato = calcola_tangente_utente()
        self.assertEqual(risultato, [])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['error_test'])
    def test_input_non_valido(self, mock_input, mock_print):
        """
        Testa l'inserimento di una stringa al posto di un numero.
        """
        risultato = calcola_tangente_utente()
        self.assertIsNone(risultato)

if __name__ == '__main__':
    unittest.main()