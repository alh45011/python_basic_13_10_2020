def fact(n):
    number = 1
    for el in range(1, n + 1):
        number *= el
        yield number

for el in fact(6):
    print(el)