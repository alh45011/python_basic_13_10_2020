first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))


def my_division(first_arg, second_arg):
    try:
        return first_arg / second_arg
    except ZeroDivisionError:
        return "Division by zero impossible"


print(my_division(first_num, second_num))
