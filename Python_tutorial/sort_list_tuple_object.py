#sort list
li = [1, 3, 4, 6, 9, 0, 3, 2]
s_li = sorted(li)
#or
s_li1 = li.sort()

#sort tuple
#tuple don't have .sort()
tu = (1, 3, 4, 6, 9, 0, 3, 2)
s_tu = sorted(tu)

#sort dict
#same as tuple
dictionary = {1, 3, 4, 6, 9, 0, 3, 2}
s_dictionary = sorted(dictionary)

#use lambda to sort list in a custom order
li1 = [1, -3, -4, 6, 9, 0, 3, -2]
s_li2 = sorted(li1, key=lambda e: abs(e))

#use lambda to sort an object through its keys
class staff:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{name},{age},{salary}"

staff1 = staff('Carl', 23, 90000)
staff2 = staff('Jenny', 19, 80000)
staff3 = staff('Coralla', 29, 100000)

salary_sort = sorted((staff1, staff2, staff3), key=lambda sta: sta.salary)
print(salary_sort)

#or
from operator import attrgetter

class staff:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{name},{age},{salary}"

staff1 = staff('Carl', 23, 90000)
staff2 = staff('Jenny', 19, 80000)
staff3 = staff('Coralla', 29, 100000)

salary_sort = sorted((staff1, staff2, staff3), key=attrgetter('age'), reverse=True)
print(salary_sort)