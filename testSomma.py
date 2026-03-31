import unittest
from unittest.mock import patch
# Assicurati che la funzione sia importata correttamente o definita nello stesso file
# from nome_file import calcola_somma_utente

class TestSommaUtente(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '10', '20', '5.5'])
    def test_somma_tre_valori(self, mock_input):
        """
        Testa se la funzione somma correttamente 3 valori: 10 + 20 + 5.5 = 35.5
        """
        risultato = calcola_somma_utente()
        self.assertEqual(risultato, 35.5)

    @patch('builtins.input', side_effect=['2', '0', '-5'])
    def test_somma_valori_negativi(self, mock_input):
        """
        Testa la somma con numeri negativi e zero: 0 + (-5) = -5.0
        """
        risultato = calcola_somma_utente()
        self.assertEqual(risultato, -5.0)

    @patch('builtins.input', side_effect=['0'])
    def test_quantita_zero(self, mock_input):
        """
        Testa il comportamento quando l'utente chiede di sommare 0 valori.
        """
        risultato = calcola_somma_utente()
        self.assertEqual(risultato, 0)

    @patch('builtins.input', side_effect=['abc'])
    def test_input_non_valido(self, mock_input):
        """
        Testa la gestione dell'errore (ValueError) se l'utente inserisce testo.
        """
        risultato = calcola_somma_utente()
        self.assertIsNone(risultato)

if __name__ == '__main__':
    unittest.main()