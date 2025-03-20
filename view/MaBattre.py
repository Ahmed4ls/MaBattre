import sys
import math
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
                             QComboBox, QSpinBox, QStackedWidget)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

def calculate_bmr(sex, weight, height, age):
    if sex.lower() == "man":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def activity_multiplier(work_activity, spare_time_activity):
    work_factors = [1.2, 1.375, 1.55, 1.725, 1.9]
    spare_factors = [1.2, 1.375, 1.55, 1.725, 1.9]
    return (work_factors[work_activity - 1] + spare_factors[spare_time_activity - 1]) / 2

def calculate_caloric_needs(sex, weight, height, age, work_activity, spare_time_activity):
    bmr = calculate_bmr(sex, weight, height, age)
    activity_level = activity_multiplier(work_activity, spare_time_activity)
    return bmr * activity_level

def calculate_daily_caloric_intake(current_weight, target_weight, weeks, tdee):
    weight_difference = target_weight - current_weight
    total_calories_needed = weight_difference * 7700
    daily_caloric_adjustment = total_calories_needed / (weeks * 7)
    return tdee + daily_caloric_adjustment

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.stack = QStackedWidget()
        
        self.auth_widget = AuthPage(self.stack)
        self.calculator_widget = CaloricCalculator()
        
        self.stack.addWidget(self.auth_widget)
        self.stack.addWidget(self.calculator_widget)
        
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        
        self.setLayout(layout)
        self.setWindowTitle("MaBattre - Health & Wellness")
        self.show()

class AuthPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        title = QLabel("Welcome to MaBattre")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)
        
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.start)
        layout.addWidget(self.login_button)
        
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.start)
        layout.addWidget(self.signup_button)
        
        self.setLayout(layout)