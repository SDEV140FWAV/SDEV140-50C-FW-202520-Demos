hex_digits = {"0":"0000", "1":"0001","2":"0010","3":"0011","4":"0100", 
             "5":"0101","6":"0110","7":"0111","8":"1000","9":"1001",
             "A":"1010","B":"1011","C":"1100","D":"1101",
             "E":"1110","F":"1111"}
binary_hex = {}
hex_letters = ["A", "B","C","D","E","F"]

for index, hex in enumerate(hex_digits.keys()):
    binary_hex[hex_digits[hex]] = hex

def get_binary_number(prompt):
    valid_binary_num = False
    while not valid_binary_num:
        binary_number = input(prompt)
        binary_number = binary_number.replace(" ","")
        valid_binary_num = True
        for digit in binary_number:
            if digit != "1" and digit != "0":
                print(f"The input contains non-binary digits: {digit}")
                valid_binary_num = False
                break
    return binary_number

def valid_binary_number(binary_number):
    valid_binary_num = True
    for digit in binary_number:
            if digit != "1" and digit != "0":
                print(f"The input contains non-binary digits: {digit}")
                valid_binary_num = False
                break
    return valid_binary_num

def valid_hexadecimal_number(hex_number):
    valid_num = True
    for digit in hex_number:
            if digit.upper() not in hex_digits:
                print(f"The input contains non hex digits: {digit}")
                valid_num = False
                break
    return valid_num

def valid_decimal_number(decimal_number):
    valid_decimal = True
    for digit in decimal_number:
        if not digit.isdigit():
            valid_decimal = False
            print(f"There are non decimal digits: {digit}")
    return valid_decimal

def convert_bin_decimal(binary_number):
    decimal_num = 0
    for exponent in range(0, len(binary_number)):
        decimal_num = decimal_num + int(binary_number[-1 - exponent]) * 2**exponent
    return decimal_num

def convert_bin_hex(binary_number):
   
    if len(binary_number) % 4 != 0:
            for i in range(4 - len(binary_number)%4):
                binary_number = "0"+ binary_number
    segements = []
    for group in range(0,len(binary_number),4):
        segements.append(binary_number[group:group+4])
    
    hex_number = ""
    for segment in segements:
        hex_number = hex_number + binary_hex[segment]  
    return hex_number

def convert_hex_bin(hex_number):
    binary_number = ""
    for digit in hex_number:
        binary_number = binary_number + hex_digits[digit.upper()]
    return binary_number

def convert_decimal_bin(decimal_num):
    decimal_num = int(decimal_num)
    binary_number = ""
    while decimal_num != 0:
        binary_number = str(decimal_num % 2) + binary_number
        decimal_num = decimal_num // 2
    return binary_number

def do_conversion(prompt,valid_func,convert_func):
    valid_input = False
    while not valid_input:
        user_input = input(prompt)
        valid_input = valid_func(user_input)
    
    return convert_func(user_input)

# To-do finish function
def get_decimal_number(prompt):
    return 17






prompt = "What operation do you want to do?\n" \
       + "1. Convert Binary to Hexadecimal\n" \
       + "2. Convert Hexadecimal to Binary\n" \
       + "3. Convert Decimal to Binary\n" \
       + "4. Convert Binary to Decimal\n"
valid_operation = False
while not valid_operation:
    operation = input(prompt)
    if operation != "1" and operation != "2" and operation != "3" and operation != "4":
        continue
    else:
        valid_operation = True
if operation == "1":
    binary_number = ""
    hex_number = do_conversion(prompt="Enter a binary number to convert to hexadecimal: ",valid_func=valid_binary_number, convert_func=convert_bin_hex)
    
    print(f"{binary_number} is {hex_number} in hexadecimal")

elif operation == "2":    
    valid_num = False
    while not valid_num:
        hex_number = input("Enter a hexadecimal number: ")
        valid_num = True
        for digit in hex_number:
            if digit.upper() not in hex_digits:
                print(f"The input contains non hex digits: {digit}")
                valid_num = False
                break

    binary_number = ""
    for digit in hex_number:
        binary_number = binary_number + hex_digits[digit.upper()]

    print(f"{hex_number} in binary is {binary_number}")
elif operation == "3":
    valid_decimal = False
    while not valid_decimal:
        decimal_num = input("Enter a decimal number: ")
        decimal_num = decimal_num.replace("-", "")
        decimal_num = decimal_num.replace("+", "")
        valid_decimal = True
        for digit in decimal_num:
            if not digit.isdigit():
                valid_decimal = False
                print(f"There are non decimal digits: {digit}")
        decimal_num_str = decimal_num[:]
        decimal_num = int(decimal_num)
        binary_number = ""
        while decimal_num != 0:
            binary_number = str(decimal_num % 2) + binary_number
            decimal_num = int(decimal_num / 2)
        print(f"{decimal_num_str} is {binary_number} in binary")
elif operation == "4":
    binary_number = get_binary_number("Enter a binary number to convert to decimal: ")
    decimal_num = 0
    for exponent in range(0, len(binary_number)):
        decimal_num = decimal_num + int(binary_number[-1 - exponent]) * 2**exponent
    print(f"{binary_number} is {decimal_num} in decimal")
