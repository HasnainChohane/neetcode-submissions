class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def employee_info(self):
        return f"Name: {self.name}, Designation: {self.designation}, Salary: ${self.salary}"
emp1 = Employee("Alice Smith", "Software Engineer", 85000)
emp2 = Employee("Bob Jones", "Data Scientist", 95000)
emp3 = Employee("Charlie Brown", "Project Manager", 110000)

# Displaying info
print(emp1.employee_info())
print(emp2.employee_info())
print(emp3.employee_info())
