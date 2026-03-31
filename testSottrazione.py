import unittest
from unittest.mock import patch
from sottrazione import sottrazione_vettore

class TestSottrazione(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['3', '100', '20', '10'])
    def test_sottrazione_standard(self, mock_input):
        """Test: 100 - 20 - 10 = 70.0"""
        self.assertEqual(sottrazione_vettore(), 70.0)

    @patch('builtins.input', side_effect=['2', '10', '15'])
    def test_risultato_negativo(self, mock_input):
        """Test: 10 - 15 = -5.0"""
        self.assertEqual(sottrazione_vettore(), -5.0)

    @patch('builtins.input', side_effect=['2', '10', '-5'])
    def test_sottrazione_negativo(self, mock_input):
        """Test: 10 - (-5) = 15.0"""
        self.assertEqual(sottrazione_vettore(), 15.0)

    @patch('builtins.input', side_effect=['1', '5'])
    def test_singolo_elemento(self, mock_input):
        """Test con un solo numero: deve restituire il numero stesso"""
        self.assertEqual(sottrazione_vettore(), 5.0)

if __name__ == '__main__':
    unittest.main()