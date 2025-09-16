valid_num = False
while not valid_num:
    number = input("Enter the numeric grade: ")
    if number.isdecimal():
        if 0 <= int(number) <= 100:
            valid_num = True
        else:
            print(f"Error: {number} is not a number between 0 and 100.")
            valid_num = False
    else:
        print(f"Error: The input, {number}, contains non-numeric digits.")
        valid_num = False
number = int(number)
if number >= 90:
    letter = 'A'
elif number >= 80:
    letter = 'B'
elif number >= 70:
    letter = 'C'
elif number >= 60:
    letter = 'D'
else:
    letter = 'F'
print(f"The letter grade is {letter}.")
