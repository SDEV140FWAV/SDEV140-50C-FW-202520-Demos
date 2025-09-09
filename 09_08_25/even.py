user_input = input("Enter Numbers: ")
tokens = user_input.split()

nums = []
for token in tokens:
    num = int(token)
    if num % 2 == 0:
        nums.append(num)

print()
for index,value in enumerate(tokens):
    
    print(f"{index}: {value}")

print(f"Max even #: {max(nums)}")

""" max_num = None
for num in nums:
    if(max_num == None) and (num % 2 == 0):
        max_num = num
    elif (max_num != None) and (num > max_num) and (num % 2 == 0):
        max_num = num
print(f"Max even #: {max_num}") """

# Get a list of integers from the user
numbers = [int(i) for i in input("Enter numbers:").split()]

# Return a list of only even numbers
even_numbers = [i for i in numbers if (i % 2) == 0]
print(f"Even numbers only: {even_numbers}")