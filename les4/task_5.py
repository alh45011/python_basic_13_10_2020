from functools import reduce

even_list = [element for element in range(100, 10001) if not element & 1]

print(even_list)

def mul(prev_el, el):
    return prev_el * el

print(reduce(mul, even_list))
