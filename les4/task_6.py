from itertools import count
from itertools import cycle

number = int(input("Enter first number: "))

for el in count(number):
    if el > 1000:
        break
    else:
        print(el)

с = 0
for el in cycle([1,5,212,21,55]):
    if с > 10:
        break
    print(el)
    с += 1