import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from main import MainApp

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.app = MainApp()

    def test_login_valid(self):
        """Test valid login switches to the calculator page."""
        self.app.auth_widget.username_input.setText("validuser")
        self.app.auth_widget.password_input.setText("password")
        QTest.mouseClick(self.app.auth_widget.signup_button, Qt.LeftButton)

        self.app.auth_widget.username_input.setText("validuser")
        self.app.auth_widget.password_input.setText("password")
        QTest.mouseClick(self.app.auth_widget.login_button, Qt.LeftButton)

        QApplication.processEvents()

        self.assertEqual(self.app.stack.currentIndex(), 1)

    def test_login_invalid(self):
        """Test invalid login stays on the auth page."""
        self.app.auth_widget.username_input.setText("invaliduser")
        self.app.auth_widget.password_input.setText("wrongpass")
        QTest.mouseClick(self.app.auth_widget.login_button, Qt.LeftButton)
        QApplication.processEvents()

        self.assertEqual(self.app.stack.currentIndex(), 0)

if name == "main":
    unittest.main()
