numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def greater_than_prev(our_list):
    i = 1
    while i < len(our_list):
        if our_list[i-1] < our_list[i]:
            yield our_list[i]
        i += 1


print(list(greater_than_prev(numbers)))

new_list = [numbers[idx] for idx in range(1, len(numbers)) if numbers[idx - 1] < numbers[idx]]
print(new_list)

