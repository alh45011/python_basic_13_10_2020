splitted_string = input("Enter your string, hero!\n").split()
i = 1
for word in splitted_string:
    print(i, ": ", word[0:10])
    i += 1