sec = int(input("Enter time in seconds: "))
print(f'{sec//3600}:{(sec%3600)//60}:{sec%60}')
