my_list = []

while True:
    new_value = int(input("Enter something\n"))
    my_list.append(new_value)
    my_list.sort(reverse = True)
    print(my_list)
    quit = input("Should we stop? Y/N  ");
    if quit == "Y" or quit == "y":
        break