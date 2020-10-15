num = int(input("Enter positive integer number "))
max_digit = 0
while num != 0:
    digit = num%10
    if digit > max_digit:
        max_digit = digit
    num = num//10

print("The biggest digit: ", max_digit)
