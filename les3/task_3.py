def my_func(first, second, third):
    if first + second > second + third:
        temp = first + second
    else:
        temp = second + third

    if first + third > temp:
        temp = first + third

    return temp


print(my_func(1, 2, 3))
