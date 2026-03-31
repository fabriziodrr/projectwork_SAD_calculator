import unittest
from unittest.mock import patch
from moltiplicazione import moltiplicazione

class TestMoltiplicazione(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['2', '3', '4'])
    def test_numeri_positivi(self, mock_input):
        risultato = moltiplicazione()
        print(f"\n[Test numeri positivi] Risultato ottenuto: {risultato} (Atteso: 12)")
        self.assertEqual(risultato, 12)
        
    @patch('builtins.input', side_effect=['3', '5', '0', '10'])
    def test_con_zero(self, mock_input):
        risultato = moltiplicazione()
        print(f"\n[Test con zero] Risultato ottenuto: {risultato} (Atteso: 0)")
        self.assertEqual(risultato, 0)
        
    @patch('builtins.input', side_effect=['2', '-2', '4'])
    def test_numeri_negativi(self, mock_input):
        risultato = moltiplicazione()
        print(f"\n[Test numeri negativi] Risultato ottenuto: {risultato} (Atteso: -8)")
        self.assertEqual(risultato, -8)
        
    @patch('builtins.input', side_effect=['0', '2', 'errore', '7', '1'])
    def test_gestione_errori_input(self, mock_input):
        risultato = moltiplicazione()
        print(f"\n[Test gestione errori] Risultato ottenuto: {risultato} (Atteso: 7)")
        self.assertEqual(risultato, 7)

if __name__ == '__main__':
    unittest.main(verbosity=2)