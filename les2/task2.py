list = [];
while True:
    list.append(input("Enter something\n"))
    quit = input("Should we stop? Y/N  ");
    if quit == "Y" or quit == "y":
        break
print("Before:", list)

i = 0
while i < len(list) - 1:
    list[i], list[i+1] = list[i+1], list[i]
    i += 2

print("After", list)
