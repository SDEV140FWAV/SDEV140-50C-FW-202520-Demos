the_sum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    the_sum = the_sum + number
    data = input("Enter a number or just enter to quit: ")
print(f"The sum is {the_sum:.2f}")

