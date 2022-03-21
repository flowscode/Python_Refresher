class Employee:
    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay
        self.email = first + "." + last + "@GMAIL.COM"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Joshua", "Dawkins", 27, 30000)
emp_2 = Employee("Liam", "May", 25, 78000)

print(emp_1.first)
print(emp_2.email)
print(emp_2.fullname())
