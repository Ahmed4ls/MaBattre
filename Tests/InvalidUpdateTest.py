import unittest
from unittest.mock import patch
from Main import main

class TestInvalidUpdate(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'man', '22', '80', '75', '12', '175',
        '4', '5', 'yes', 'wrong_input', 'no'
    ])
    def test_invalid_update(self, mock_input):
        user_data = main()
        self.assertEqual(user_data['age'], 22)

if name == "main":
    unittest.main()
    
