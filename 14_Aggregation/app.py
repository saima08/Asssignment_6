class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, emp):
        self.emp = emp

e = Employee("Saima")
d = Department(e)
print(d.emp.name)
