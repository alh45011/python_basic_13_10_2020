revenue = int(input("Enter revenue: "))
costs = int(input("Enter costs: "))

if revenue >= costs:
    print("Your company has profit!")
else:
    print("Your company is unprofitable :(")

number_of_employee = int(input("Enter number of employee: "))

if revenue <= costs:
    print("Sorry. There is no profit. 0/employee")
else:
    print("Profit per employee is: ", (revenue - costs) / number_of_employee)
