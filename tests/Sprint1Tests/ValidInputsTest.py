import unittest
from unittest.mock import patch
from Main import main

class TestValidInputs(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'man', '25', '75', '70', '10', '180',
        '3', '4', 'no'
    ])
    def test_valid_inputs(self, mock_input):
        user_data = main()
        self.assertEqual(user_data['sex'], 'man')
        self.assertEqual(user_data['age'], 25)
        self.assertEqual(user_data['weight'], 75.0)
        self.assertEqual(user_data['target_weight'], 70.0)
        self.assertEqual(user_data['weeks'], 10)
        self.assertEqual(user_data['height'], 180.0)
        self.assertEqual(user_data['work_activity'], 3)
        self.assertEqual(user_data['spare_time_activity'], 4)

if __name__ == "__main__":
    unittest.main()
