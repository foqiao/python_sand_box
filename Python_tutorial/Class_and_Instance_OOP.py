#simple example of python OOP
class Employee:
    pass

#object constructor that constructs two employees' directories
emp_1 = Employee()
emp_2 = Employee()

#print the emp_1 and emp_2
print(emp_1)
print(emp_2)

#add in components for the first employee
emp_1.first = 'Ted'
emp_1.last = 'Yuan'
emp_1.email = 'foqiao89@hotmail.com'
emp_1.pay = 6000

#add in components for the second employee
emp_2.first = 'Lily'
emp_2.last = 'Lee'
emp_2.email = 'lily.lee@hotmail.com'
emp_2.pay = 15000

#print out the email of both employees
print(emp_1.email)
print(emp_2.email)

#a step further from the above example
class employee1:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "%s.%s@company.com".format(first, last)

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

#object constructors of two employees
emp_1 = employee1('Ted', 'Yuan', 50000)
emp_2 = employee1('Lily', 'Lee', 40000)

#output fullname
print(emp_1.fullName())