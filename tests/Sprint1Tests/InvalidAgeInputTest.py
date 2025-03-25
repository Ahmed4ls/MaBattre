import unittest
from unittest.mock import patch
from Main import main

class TestInvalidAgeInput(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'woman', 'twenty', '65', '60', '8', '165',
        '2', '3', 'no'
    ])
    def test_invalid_age_input(self, mock_input):
        with self.assertRaises(ValueError):
            main()

if name == "main":
    unittest.main()
