
first = [10, 20, 30]
second = first[:]
print(first == second and first is not second)
print(first)
print(second)
if first is second:
    print("Don't change the alias")
else:
    first[1] = 99
    print(first == second)
    print(first)
    print(second)


my_list = [[10, 20], [30, 40]]
print(f"First nested list: {my_list[0]}")
print(f"Second nested list: {my_list[1]}")
print(f"Element 0 of first nested list: {my_list[0][0]}")

for row in my_list:
    for col in row:
        print(col)
    