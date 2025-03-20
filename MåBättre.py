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