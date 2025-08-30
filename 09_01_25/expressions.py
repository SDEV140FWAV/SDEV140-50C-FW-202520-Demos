import math
import random

decimal_num = int(input("Enter a decimal number: "))
binary_digit8 = decimal_num % 2
decimal_num = int(decimal_num / 2)
binary_digit7 = decimal_num % 2
decimal_num = int(decimal_num / 2)
binary_digit6 = decimal_num % 2
decimal_num = int(decimal_num / 2)
binary_digit5 = decimal_num % 2
decimal_num = int(decimal_num / 2)
binary_digit4 = decimal_num % 2
decimal_num = int(decimal_num / 2)
binary_digit3 = decimal_num % 2
decimal_num = int(decimal_num / 2)
binary_digit2 = decimal_num % 2
decimal_num = int(decimal_num / 2)
binary_digit1 = decimal_num % 2
decimal_num = int(decimal_num / 2)
print(binary_digit1,binary_digit2, binary_digit3, binary_digit4, binary_digit5, binary_digit6, binary_digit7, binary_digit8)

num = 49
num_sqrt = math.sqrt(num)
random.seed(15)
print(random.random())
print(random.randrange(1,20))
print(ord("강"))
print(chr(44022))