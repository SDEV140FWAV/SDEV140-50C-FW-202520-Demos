import random

magic_num = random.randint(100,1000)
valid_num = False
while not valid_num:
    user_num = input("Enter a number between 1 and 100: ")
    
    if user_num.isnumeric():
        if 1 <= int(user_num) <= 100:
           valid_num = True
        else:
            print(f"Error: {user_num} is not a number between 1 and 100.")
    else:
        print(f"Error: The input, {user_num}, contains non-numeric digits.")
        valid_num = False
if int(user_num) <= magic_num:
    print("My number is higher!!! I win!")
else:
    print("Good Guess!")

print("Thanks for playing!")
    
        
