user_input = ""
while user_input != "q":
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))
        bmi = (float(weight) / float(height * height)) * 703
        print(f"BMI: {bmi}")
    except (ValueError, TypeError):
        print("Could not calculate health info.\n")
    except ZeroDivisionError:
        print("invalid height entered. Must be > 0.")

    user_input = input('Enter any key ("q" to quit): ')