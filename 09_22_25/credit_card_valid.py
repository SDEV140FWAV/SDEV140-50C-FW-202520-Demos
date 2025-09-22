def get_valid_credit_card_number():
    cc_num = input("Enter a 16 digit credit card number: ")
    cc_num = cc_num.strip()
    cc_num = cc_num.replace(" ","")
    if len(cc_num) != 16 or not cc_num.isdigit():
        print("Credit card numbers must be 16 numeric digits.")
        return None
    else:
        return cc_num

def double_odd_positions(cc_num):
    doubled_odd_digits = [] #[int(digit) * 2 for digit in cc_num[::2]]
    for digit in cc_num[::2]:
        doubled_odd_digits.append(int(digit) * 2)
    return doubled_odd_digits

def get_even_positions(cc_num):
    even_digits =[int(digit) for digit in cc_num[1::2]]
    return even_digits

def add_two_digit_positions(odd_digits):
    for i in range(0,len(odd_digits)):
        odd_digits[i] = odd_digits[i] % 10 + odd_digits[i]//10


def main():
    credit_card = None
    while credit_card == None:
        credit_card = get_valid_credit_card_number()
    even_digits = get_even_positions(credit_card)
    odd_digits = double_odd_positions(credit_card)
    #print(odd_digits)
    add_two_digit_positions(odd_digits)
    #print(odd_digits)
    total_sum = sum(even_digits) + sum(odd_digits)
    if total_sum % 10 == 0:
        print(f"{credit_card} is a valid credit card number.")
    else:
        print(f"{credit_card} is not valid!")

if __name__ == "__main__":
    main()
            