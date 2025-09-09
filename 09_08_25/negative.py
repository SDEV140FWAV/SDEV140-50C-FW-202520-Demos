user_input = input("Enter numbers:")

tokens = user_input.split()

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()
for pos, val in enumerate(nums):  
    """ if val < 0:
        val = 0 """
    print(f"{pos}: {val}")

# Change negative values to 0
""" for num in nums:
    if num < 0:
        num = 0  # Logic error: temp variable num set to 0 """
""" for index in range(len(nums)):
    if nums[index] < 0:
        nums[index] = 0 """
nums_copy = nums[:]
for index, num in enumerate(nums_copy):
    if num < 0:
        nums.pop(index)
        # nums.remove(num)
        # del nums[index]

# Print new numbers
print("New numbers: ")
for num in nums:
    print(num, end=" ")