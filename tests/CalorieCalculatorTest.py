import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from main import MainApp

class TestCalorieCalculatorValid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.app = MainApp()

    def test_calorie_calculator_valid(self):
        """Test valid calorie calculator inputs."""
        self.app.stack.setCurrentIndex(1)
        self.app.calculator_widget.weight_input.setText("70")
        self.app.calculator_widget.height_input.setText("175")
        self.app.calculator_widget.age_input.setValue(25)
        self.app.calculator_widget.target_weight_input.setText("65")
        self.app.calculator_widget.weeks_input.setValue(10)
        self.app.calculator_widget.work_activity_combo.setCurrentIndex(2)
        self.app.calculator_widget.spare_activity_combo.setCurrentIndex(3)

        QTest.mouseClick(self.app.calculator_widget.calculate_button, Qt.LeftButton)
        QApplication.processEvents()

        self.assertIn("decrease", self.app.calculator_widget.result_label.text().lower())

if __name__ == "__main__":
    unittest.main()
