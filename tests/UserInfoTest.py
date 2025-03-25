import unittest
from main import CaloricCalculator
from PyQt5.QtWidgets import QApplication
import sys

class TestUserInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.calculator = CaloricCalculator()

    def test_sex_selection(self):
        self.calculator.sex_combo.setCurrentText("Man")
        self.assertEqual(self.calculator.sex_combo.currentText(), "Man")

        self.calculator.sex_combo.setCurrentText("Woman")
        self.assertEqual(self.calculator.sex_combo.currentText(), "Woman")

    def test_age_input(self):
        self.calculator.age_input.setValue(25)
        self.assertEqual(self.calculator.age_input.value(), 25)

    def test_weight_input(self):
        self.calculator.weight_input.setText("70")
        self.assertEqual(self.calculator.weight_input.text(), "70")

    def test_target_weight_input(self):
        self.calculator.target_weight_input.setText("65")
        self.assertEqual(self.calculator.target_weight_input.text(), "65")

    def test_height_input(self):
        self.calculator.height_input.setText("175")
        self.assertEqual(self.calculator.height_input.text(), "175")

    def test_work_activity_selection(self):
        self.calculator.work_activity_combo.setCurrentIndex(2)
        self.assertEqual(self.calculator.work_activity_combo.currentText(), "3: Quite active (nurse or similar)")

    def test_spare_activity_selection(self):
        self.calculator.spare_activity_combo.setCurrentIndex(1)
        self.assertEqual(self.calculator.spare_activity_combo.currentText(), "2: Slightly active (light exercise 2 times a week)")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

if __name__ == "__main__":
    unittest.main()
