def reverse_list(lst):
    low_pointer = 0
    high_pointer = len(lst) - 1


    while low_pointer < high_pointer:
        temp = lst[low_pointer]

        lst[low_pointer] = lst[high_pointer]
        lst[high_pointer] = temp
        low_pointer += 1
        high_pointer -= 1

    return lst

lst = ["pooh", "christopher robin", "piglet", "eeyore"]
print(reverse_list(lst))