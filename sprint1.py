def main():

    user_data = {}


    user_data['sex'] = input("Enter your sex (man/woman): ").strip().lower()
    print()
    user_data['age'] = int(input("Enter your age: ").strip())
    print()
    user_data['weight'] = float(input("Enter your weight (kg): ").strip())
    print()
    user_data['target_weight'] = float(input("Enter your target weight (kg): ").strip())
    print()
    user_data['weeks'] = int(input("How fast do you want to achieve your goal (weeks)?: ").strip())
    print()
    user_data['height'] = float(input("Enter your height (cm): ").strip())
    print()


    print("How active are you during work?")
    print("1: Not active (sitting all day)")
    print("2: Slightly active (office work or similar)")
    print("3: Quite active (nurse or similar)")
    print("4: Active (gym instructor or similar)")
    print("5: Very active (craftsman or similar)")
    print()
    user_data['work_activity'] = int(input("Select your work activity level (1-5): ").strip())
    print()


    print("How active are you during your spare time?")
    print("1: Not active (no exercise)")
    print("2: Slightly active (light exercise 2 times a week)")
    print("3: Quite active (moderate exercise 2 times a week)")
    print("4: Active (moderate exercise 3-4 times a week)")
    print("5: Very active (hard exercise at least 4 times a week)")
    print()
    user_data['spare_time_activity'] = int(input("Select your spare time activity level (1-5): ").strip())
    print()
