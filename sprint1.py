def main():
    sex = input("Enter your sex (man/woman): ")
    print()
    age = int(input("Enter your age: "))
    print()
    weight = float(input("Enter your weight (kg): "))
    print()
    target_weight = float(input("Enter your target weight (kg): "))
    print()
    weeks = int(input("How fast do you want to achieve your goal (weeks)?: "))
    print()
    height = float(input("Enter your height (cm): "))
    print()
    
    print("How active are you during work?")
    print("1: Not active (sitting all day)")
    print("2: Slightly active (office work or similar)")
    print("3: Quite active (nurse or similar)")
    print("4: Active (gym instructor or similar)")
    print("5: Very active (craftsman or similar)")
    print()
    work_activity = int(input("Select your work activity level (1-5): "))
    print()

    
    print("How active are you during your spare time?")
    print("1: Not active (no exercise)")
    print("2: Slightly active (light exercise 2 times a week)")
    print("3: Quite active (moderate exercise 2 times a week)")
    print("4: Active (moderate exercise 3-4 times a week)")
    print("5: Very active (hard exercise at least 4 times a week)")
    print()
    spare_time_activity = int(input("Select your spare time activity level (1-5): "))
    print()
    
    while True:
            change = input("Do you want to update any information? (yes/no): ").strip().lower()
            if change == 'yes':
                key = input("Which information do you want to update? (sex, age, weight, target_weight, weeks, height, work_activity, spare_time_activity): ")
                if key in user_data:
                    new_value = input(f"Enter new value for {key}: ")
                    if key in ['age', 'weeks', 'work_activity', 'spare_time_activity']:
                        user_data[key] = int(new_value)
                    elif key in ['weight', 'target_weight', 'height']:
                        user_data[key] = float(new_value)
                    else:
                        user_data[key] = new_value
                else:
                    print("Invalid field. Please enter a valid option.")
            else:
                break
    print(f"To reach your goal of {target_weight} kg in {weeks} weeks:")
    return user_data
        
        
    
if __name__ == "__main__":
    main()
