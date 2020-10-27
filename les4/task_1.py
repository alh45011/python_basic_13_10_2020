from sys import argv

script_name, hours, rate, award = argv


def calc_salary(hours, rate, award):
    return hours * rate + award


print(calc_salary(int(hours), int(rate), int(award)))