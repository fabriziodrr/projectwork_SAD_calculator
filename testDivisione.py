import unittest
from unittest.mock import patch

class TestDivisioneUtente(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '100', '2', '5'])
    def test_divisione_standard(self, mock_input):
        """
        Testa 100 / 2 / 5 = 10.0
        """
        risultato = calcola_divisione_utente()
        self.assertEqual(risultato, 10.0)

    @patch('builtins.input', side_effect=['2', '50', '0'])
    def test_divisione_per_zero(self, mock_input):
        """
        Testa il comportamento quando il divisore è zero.
        """
        risultato = calcola_divisione_utente()
        self.assertIsNone(risultato)

    @patch('builtins.input', side_effect=['1', '10'])
    def test_singolo_valore(self, mock_input):
        """
        Se inserisco un solo valore, il risultato deve essere il valore stesso.
        """
        risultato = calcola_divisione_utente()
        self.assertEqual(risultato, 10.0)

    @patch('builtins.input', side_effect=['invalid'])
    def test_input_non_numerico(self, mock_input):
        """
        Testa l'inserimento di stringhe invece di numeri.
        """
        risultato = calcola_divisione_utente()
        self.assertIsNone(risultato)

if __name__ == '__main__':
    unittest.main()