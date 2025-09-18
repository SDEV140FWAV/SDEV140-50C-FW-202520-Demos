def append_to_list(value=99, my_list=None):
    if my_list == None:
        my_list = []
    my_list.append(value)
    return my_list

numbers = append_to_list(50)  # default list appended with 50
print(numbers)
numbers = append_to_list(100)  # default list appended with 100
print(numbers)