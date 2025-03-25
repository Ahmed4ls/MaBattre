import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from main import MainApp

class TestCalorieCalculatorInvalid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.app = MainApp()

    def test_calorie_calculator_invalid(self):
        """Test invalid calorie calculator inputs (non-numeric weight)."""
        self.app.stack.setCurrentIndex(1)
        self.app.calculator_widget.weight_input.setText("abc")
        QTest.mouseClick(self.app.calculator_widget.calculate_button, Qt.LeftButton)
        QApplication.processEvents()

        self.assertIn("Please enter valid numbers", self.app.calculator_widget.result_label.text())

if __name__ == "__main__":
    unittest.main()
