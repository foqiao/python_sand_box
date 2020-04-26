def leap_years(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_in_month(month, year):
    if not 1 <= month <= 12:
        return "invalid month"
    else:
        if month % 2 != 0:
            return 31
        elif month == 8:
            return 31
        elif month == 2 and not leap_years(year):
            return 28
        elif month == 2 and leap_years(year):
            return 29
        else:
            return 30

print(day_in_month(8, 2020))
print(day_in_month(2, 2020))
print(day_in_month(2, 2019))
print(day_in_month(4, 2020))