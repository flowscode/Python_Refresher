class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay
        self.email = first + "." + last + "@GMAIL.COM"

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

print(Employee.num_of_employees)

emp_1 = Employee("Joshua", "Dawkins", 27, 30000)
emp_2 = Employee("Liam", "May", 25, 78000)

print(emp_1.first)
print(emp_2.email)
print(emp_1.fullname())
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.num_of_employees)

print(emp_1.raise_amount)
Employee.set_raise_amount(1.07)
print(emp_1.raise_amount)
