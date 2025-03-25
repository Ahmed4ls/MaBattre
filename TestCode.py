import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox,
QSpinBox, QStackedWidget, QMessageBox, QFrame)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import pyrebase

config = {  
    "apiKey": "AIzaSyDqU6_e-NbtXRoaHf1WOsiWcFFC91tNODs",
    "authDomain": "mabattre.firebaseapp.com",
    "databaseURL": "https://mabattre-default-rtdb.firebaseio.com",
    "projectId": "mabattre",
    "storageBucket": "mabattre.appspot.com",
    "messagingSenderId": "451993272033",
    "appId": "1:451993272033:web:6f1c64d042f77e608601a0",
    "measurementId": "G-6YVF3T2E4W"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

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

def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return user
    except Exception as e:
        return {"error": str(e)}

def sign_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except Exception as e:
        return {"error": str(e)}

class DailyChallengePage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.challenges = [
            "Drink 8 glasses of water today.",
            "Take a 10-minute walk.",
            "Eat at least one serving of vegetables.",
            "Do 10 minutes of stretching.",
            "Avoid sugary snacks for the day.",
            "Take the stairs instead of the elevator.",
            "Practice deep breathing for 5 minutes."
        ]
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        title = QLabel("Daily Health Challenge")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.challenge_label = QLabel()
        self.challenge_label.setFont(QFont("Arial", 14))
        self.challenge_label.setAlignment(Qt.AlignCenter)
        self.challenge_label.setWordWrap(True)
        layout.addWidget(self.challenge_label)

        self.complete_button = QPushButton("Mark as Completed")
        self.complete_button.clicked.connect(self.mark_completed)
        layout.addWidget(self.complete_button)

        self.back_button = QPushButton("Back to Tips")
        self.back_button.clicked.connect(self.go_back)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
        self.set_daily_challenge()

    def set_daily_challenge(self):
        self.current_challenge = random.choice(self.challenges)
        self.challenge_label.setText(self.current_challenge)

    def mark_completed(self):
        QMessageBox.information(self, "Success", "Great job! Challenge marked as completed.")
        self.set_daily_challenge() 

    def go_back(self):
        self.stack.setCurrentIndex(2) 

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.stack = QStackedWidget()
        self.auth_widget = AuthPage(self.stack)
        self.calculator_widget = CaloricCalculator(self.stack)
        self.tips_widget = TipsPage(self.stack)
        self.daily_challenge_widget = DailyChallengePage(self.stack)

        self.stack.addWidget(self.auth_widget)
        self.stack.addWidget(self.calculator_widget)
        self.stack.addWidget(self.tips_widget)
        self.stack.addWidget(self.daily_challenge_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        self.setWindowTitle("MaBattre - Health & Wellness")
        self.current_user_id = None
        self.show()

class AuthPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        title = QLabel("Welcome to MaBattre")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.signup)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        if not email or not password:
            QMessageBox.warning(self, "Error", "Please enter both email and password.")
            return
        result = sign_in(email, password)
        if 'error' in result:
            QMessageBox.warning(self, "Error", result['error'])
        else:
            QMessageBox.information(self, "Success", "Login successful!")
            self.stack.setCurrentIndex(1)

    def signup(self):
        email = self.email_input.text()
        password = self.password_input.text()
        if not email or not password:
            QMessageBox.warning(self, "Error", "Please enter an email and password to register.")
            return
        result = sign_up(email, password)
        if 'error' in result:
            QMessageBox.warning(self, "Error", result['error'])
        else:
            QMessageBox.information(self, "Success", "Registration successful! You can now log in.")
            self.email_input.clear()
            self.password_input.clear()

class CaloricCalculator(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        title = QLabel("MaBattre - How many calories do I need?")
        title.setFont(QFont("Arial", 20, QFont.Bold))
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
        self.work_activity_combo.addItems(["1: Not active", "2: Slightly active", "3: Quite active", "4: Active", "5: Very active"])
        layout.addWidget(self.work_activity_combo)

        layout.addWidget(QLabel("How active are you during your spare time?"))
        self.spare_activity_combo = QComboBox()
        self.spare_activity_combo.addItems(["1: Not active", "2: Slightly active", "3: Quite active", "4: Active", "5: Very active"])
        layout.addWidget(self.spare_activity_combo)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate(self):
        try:
            sex = self.sex_combo.currentText()
            age = self.age_input.value()
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            target_weight = float(self.target_weight_input.text())
            weeks = self.weeks_input.value()
            work_activity = self.work_activity_combo.currentIndex() + 1
            spare_activity = self.spare_activity_combo.currentIndex() + 1

            tdee = calculate_caloric_needs(sex, weight, height, age, work_activity, spare_activity)
            daily_caloric_intake = calculate_daily_caloric_intake(weight, target_weight, weeks, tdee)

            if daily_caloric_intake > tdee:
                goal = "gain"
            else:
                goal = "lose"

            self.stack.widget(2).set_results(daily_caloric_intake, target_weight, weeks, goal)
            self.stack.setCurrentIndex(2)
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numbers.")


class TipsPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.title = QLabel("")
        self.title.setFont(QFont("Arial", 18, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)

        self.tip_boxes = []
        for _ in range(4):
            box = QFrame()
            box.setFrameShape(QFrame.Box)
            box.setLineWidth(2)
            box_layout = QVBoxLayout()
            label = QLabel("")
            label.setWordWrap(True)
            label.setFont(QFont("Arial", 11))
            box_layout.addWidget(label)
            box.setLayout(box_layout)
            self.layout.addWidget(box)
            self.tip_boxes.append(label)


        self.daily_challenge_button = QPushButton("Daily Challenge")
        self.daily_challenge_button.clicked.connect(lambda: self.stack.setCurrentIndex(3))
        self.layout.addWidget(self.daily_challenge_button)

        self.back_button = QPushButton("Calculate Again")
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def set_results(self, daily_calories, target_weight, weeks, goal):
        self.title.setText(
            f"Your goal: {target_weight} kg in {weeks} weeks\nRecommended daily intake: {daily_calories:.0f} kcal"
        )
        if goal == "lose":
            tips = [
                "Eat more protein to stay full longer and preserve muscle mass.",
                "Drink plenty of water before meals to reduce calorie intake.",
                "Increase fiber intake to improve satiety and digestion.",
                "Prioritize whole foods and avoid high-calorie processed snacks."
            ]
        else:
            tips = [
                "Consume calorie-dense foods like nuts, seeds, and healthy oils.",
                "Increase meal frequency to add extra calories throughout the day.",
                "Focus on strength training to ensure weight gain is muscle, not fat.",
                "Drink smoothies or shakes with added protein and carbs."
            ]

        for i, tip in enumerate(tips):
            self.tip_boxes[i].setText(tip)

    def go_back(self):
        self.stack.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())