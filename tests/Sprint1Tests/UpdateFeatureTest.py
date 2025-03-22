import unittest
from unittest.mock import patch
from Main import main

class TestUpdateAge(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'woman', '30', '65', '60', '8', '165',
        '2', '3', 'yes', 'age', '35', 'no'
    ])
    def test_update_age(self, mock_input):
        user_data = main()
        self.assertEqual(user_data['age'], 35)

if __name__ == "__main__":
    unittest.main()
