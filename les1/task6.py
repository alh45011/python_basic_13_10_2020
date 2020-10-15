today = float(input("enter first number: "))
last_day = float(input("enter second number: "))
day_num = 1
while today < last_day:
    print(day_num, "-й день: ", "%.2f" % today, " км")
    day_num = day_num + 1
    today = today * 1.1
    if today >= last_day:
        print(day_num, "-й день: ", "%.2f" % today, " км")
        print(f"Ответ: На {day_num} день спортсмен достиг результата не менее {last_day}")
