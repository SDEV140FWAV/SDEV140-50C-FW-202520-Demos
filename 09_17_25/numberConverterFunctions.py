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

def convert_decimal_hex(decimal_num):
    binary_number = convert_decimal_bin(decimal_num)
    hex_number = convert_bin_hex(binary_number)
    return hex_number

def do_conversion(prompt,valid_func,convert_func):
    valid_input = False
    while not valid_input:
        user_input = input(prompt)
        valid_input = valid_func(user_input)
    
    return (user_input,convert_func(user_input))

# To-do finish function
def convert_to_float_safe(string):
    if string.count('.') > 1:
        return None
    if string.count('-') > 1:
        return None
    if string.count('-') == 1 and string[0] != '-':
        return None
    if string.count('+') > 1:
        return None
    if string.count('+') == 1 and string[0] != '+':
        return None
    string_cpy = string[:]
    string_cpy = string_cpy.replace('+', "")
    string_cpy = string_cpy.replace('-', "")
    string_cpy = string_cpy.replace('.', "")
    if not string_cpy.isdigit():
        return None
    return float(string)

def test_float():
    print(convert_to_float_safe("13.278"))
    print(convert_to_float_safe("192.168.1.1"))
    print(convert_to_float_safe("-12.22"))
    print(convert_to_float_safe("12-25-2025"))
    print(convert_to_float_safe("12 2321 jkljl"))




def main():
    prompt = "What operation do you want to do?\n" \
        + "1. Convert Binary to Hexadecimal\n" \
        + "2. Convert Hexadecimal to Binary\n" \
        + "3. Convert Decimal to Binary\n" \
        + "4. Convert Binary to Decimal\n"\
        + "5. Convert Decimal to Hexadecimal\n"
    valid_operation = False
    while not valid_operation:
        operation = input(prompt)
        if operation != "1" and operation != "2" and operation != "3" and operation != "4" and operation != "5":
            continue
        else:
            valid_operation = True
    if operation == "1": 
        binary_number, hex_number = do_conversion(prompt="Enter a binary number to convert to hexadecimal: ",valid_func=valid_binary_number, convert_func=convert_bin_hex)
        print(f"{binary_number} is {hex_number} in hexadecimal")

    elif operation == "2":    
        hex_number, binary_number = do_conversion(prompt="Enter a hexadecimal number: ", convert_func=convert_hex_bin, valid_func=valid_hexadecimal_number)
        print(f"{hex_number} in binary is {binary_number}")

    elif operation == "3":
        decimal_num_str, binary_number = do_conversion("Enter a decimal number: ", valid_decimal_number, convert_decimal_bin)   
        print(f"{decimal_num_str} is {binary_number} in binary")

    elif operation == "4":
        binary_number, decimal_num = do_conversion("Enter a binary number to convert to decimal: ", valid_binary_number, convert_bin_decimal)
        print(f"{binary_number} is {decimal_num} in decimal")
    elif operation == "5":
        decimal_num, hex_number = do_conversion("Enter a decimal number: ", valid_decimal_number, convert_decimal_hex)
        print(f"{decimal_num} is {hex_number} in hexadecimal")

if __name__ == "__main__":
    main()

