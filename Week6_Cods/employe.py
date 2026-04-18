class Employee:
    def __init__(self, salary):
        self.__salary = salary   # private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary


emp = Employee(50000)

# Access using getter
print("Salary:", emp.get_salary())

# Update using setter
emp.set_salary(60000)
print("Updated Salary:", emp.get_salary())


print(emp._Employee__salary) 