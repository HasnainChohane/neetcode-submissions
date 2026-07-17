class Employee:
    def work(self):
        print("Employee is working in general tasks")

class Teacher(Employee):
    def work(self):  
        print("Teacher is teaching students")

class Developer(Teacher):  # Inherits from Teacher
    def work(self):  
        print("Developer is writing and debugging code")

class Doctor(Developer):  # Inherits from Developer
    def work(self):  
        print("Doctor is treating patients")

# --- Testing ---
Employee().work()
Teacher().work()
Developer().work()
Doctor().work()