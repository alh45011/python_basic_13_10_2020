def summator():
    sum = 0

    while True:
        values = input("Enter list of numbers or 'z' to exit: ").split()
        for value in values:
            if value == 'z':
                return sum
            sum += int(value)
        print("Current Sum: ", sum)

print(summator())
