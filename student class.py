class Student:
    school = "Beacon Light School & Uni , Fateh Pur"
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    # Instance method
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
    # Class method
    @classmethod
    def show_school(cls):
        print(f"School Name: {cls.school}")
    # Static method
    @staticmethod
    def welcome_message():
        print("Welcome to the Student Management System!")
Student.welcome_message()
Student.show_school()
student1 = Student("Hasnain", 20)
student1.display_info()
