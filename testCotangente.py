import unittest
from unittest.mock import patch
from cotangente import calcola_cotangente_utente

class TestCotangenteUtente(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '45', '90'])
    def test_cotangente_valori_noti(self, mock_input, mock_print):
        """
        Testa la cotangente di 45 e 90 gradi.
        Ci aspettiamo [1.0, 0.0].
        """
        risultato = calcola_cotangente_utente()
        self.assertEqual(risultato, [1.0, 0.0])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', '180'])
    def test_cotangente_non_definita(self, mock_input, mock_print):
        """
        Testa il comportamento a 180 gradi (dove il seno è zero).
        Deve restituire None.
        """
        risultato = calcola_cotangente_utente()
        self.assertIsNone(risultato)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['0'])
    def test_quantita_zero(self, mock_input, mock_print):
        """
        Testa l'inserimento di 0 come quantità.
        """
        risultato = calcola_cotangente_utente()
        self.assertEqual(risultato, [])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['invalid_data'])
    def test_input_non_valido(self, mock_input, mock_print):
        """
        Testa l'inserimento di una stringa.
        """
        risultato = calcola_cotangente_utente()
        self.assertIsNone(risultato)

if __name__ == '__main__':
    unittest.main()