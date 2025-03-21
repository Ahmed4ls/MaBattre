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

    def start(self):
        self.stack.setCurrentIndex(1)

class CaloricCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        title = QLabel("MaBattre - How many calories do I need?")
        title.setFont(QFont("Arial", 22, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        layout.addWidget(QLabel("Select Sex:"))
        self.sex_combo = QComboBox()
        self.sex_combo.addItems(["Man", "Woman"])
        layout.addWidget(self.sex_combo)
        
        layout.addWidget(QLabel("Enter Age:"))
        self.age_input = QSpinBox()
        layout.addWidget(self.age_input)
        
        layout.addWidget(QLabel("Enter your weight (kg):"))
        self.weight_input = QLineEdit()
        layout.addWidget(self.weight_input)
        
        layout.addWidget(QLabel("Enter your target weight (kg):"))
        self.target_weight_input = QLineEdit()
        layout.addWidget(self.target_weight_input)
        
        layout.addWidget(QLabel("How fast do you want to achieve your goal (weeks)?:"))
        self.weeks_input = QSpinBox()
        layout.addWidget(self.weeks_input)
        
        layout.addWidget(QLabel("Enter your height (cm):"))
        self.height_input = QLineEdit()
        layout.addWidget(self.height_input)
        
        layout.addWidget(QLabel("How active are you during work?"))
        self.work_activity_combo = QComboBox()
        self.work_activity_combo.addItems(["1: Not active (sitting all day)", "2: Slightly active (office work or similar)", "3: Quite active (nurse or similar)", "4: Active (gym instructor or similar)", "5: Very active (craftsman or similar)"])
        layout.addWidget(self.work_activity_combo)
        
        layout.addWidget(QLabel("How active are you during your spare time?"))
        self.spare_activity_combo = QComboBox()
        self.spare_activity_combo.addItems(["1: Not active (no exercise)", "2: Slightly active (light exercise 2 times a week)", "3: Quite active (moderate exercise 2 times a week)", "4: Active (moderate exercise 3-4 times a week)", "5: Very active (hard exercise at least 4 times a week)"])
        layout.addWidget(self.spare_activity_combo)
        
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)
        
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)

    def calculate(self):
        pass  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())