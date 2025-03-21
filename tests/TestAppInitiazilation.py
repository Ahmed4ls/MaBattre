import unittest
from PyQt5.QtWidgets import QApplication
from main import MainApp

class TestAppSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.app = MainApp()

if name == "main":
    unittest.main()
