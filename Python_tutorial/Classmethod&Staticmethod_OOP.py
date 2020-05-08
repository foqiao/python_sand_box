class Employee:

    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "%s.%s@company.com".format(first, last)

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    #class annotation replaces self instance for the below function
    def set_raise_amt(cls, amount):
        self.raise_amount = amount

emp1 = Employee('Ted', 'Yuan', 50000)
emp2 = Employee('Jason', 'Yuan', 40000)