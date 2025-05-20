class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # public
        self._salary = salary      # protected
        self.__ssn = ssn           # private

e = Employee("Saima", 9000000, "123-45-6789")
print(e.name)         # Accessible
print(e._salary)      # Technically accessible, but discouraged
# print(e.__ssn)      # Error: Not directly accessible
print(e._Employee__ssn)  # Name mangling can access it
