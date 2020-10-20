print("Hello ranger!\n")
goods_list = []
i = 1
names = []
prices = []
numbers = []
units = []
rates = []
while True:
    name = input("Enter the name of the cool stuff: ")
    names.append(name)
    price = input("Enter its price: ")
    prices.append(price)
    number = input("Enter its number: ")
    numbers.append(number)
    unit = input("What's the unit of measure? ")
    units.append(unit)
    rate = input("Rate its coolness from 1 to infinity: ")
    rates.append(rate)
    goods_list.append((i, {"название": name, "цена": price, "количество": number, "eд.": unit, "рейтинг": rate}))
    i += 1
    quit = input("Should we stop? Y/N  ");
    if quit == "Y" or quit == "y":
        break
print("The list: ", goods_list)
analytics = {
    "название": names,
    "цена": prices,
    "количество": numbers,
    "eд.": units,
    "рейтинг": rates
}
print("The analytics: ", analytics)


