#Class variables are variables that shared among each instances of a class
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "%s.%s@company.com".format(first, last)

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)

#to access each variables within a class, you need either access class itself or use the class instance

emp1 = Employee('Ted', 'Yuan', 50000)

#pay before the raise
print(emp1.pay)

#pay raise for emp1
emp1.pay_raise()

print(emp1.pay)

#when calling an attribute of a class, the python will look for the instance whether have this matching attribute.
#If nothing found, they will look at the ancestor of this class for the same matching attribute
print(Employee.raise_amount)
print(emp1.raise_amount)

#If we change the raise_amount, the raise amount of the class will change to the updated value
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)

#If we change only the attribute for emp1, the raise amount for emp1 will update alone
emp1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)

#If we output dictionary for emp1, only the attributes within the emp1's constructor will show up
print(emp1.__dict__)

#If we output dictionary for Employee, all the attributes within the class will show up
print(Employee.__dict__)