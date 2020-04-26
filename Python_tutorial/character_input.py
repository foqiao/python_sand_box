import datetime

def character(name, age):
    age_difference = 100 - int(age)
    this_yr = datetime.datetime.now()
    yr_diff = age_difference + this_yr.year
    print(f'{name} will turn 100 at the year {yr_diff}')

name1 = input("Please enter your full name: ")
age1 = input("Please enter your current age: ")
character(name1, age1)