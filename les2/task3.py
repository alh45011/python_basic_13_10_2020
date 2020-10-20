month = int(input("Enter month`s number: "))

dict_months = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn", 12: "Winter" }

#First option from dictionary
print(dict_months[month])
#Second option from list (I made it from the sorce dictionary
print(list(dict_months.values())[month])
