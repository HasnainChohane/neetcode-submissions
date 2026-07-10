class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no, department):
        # Rule 1: Use super() to call the Parent constructor
        super().__init__(name, age)
        self.roll_no = roll_no
        self.department = department

    def show_student(self):
        # Rule 2: Use super() to reuse the display method
        super().display()
        print(f"Roll No: {self.roll_no}, Department: {self.department}")
student1 = Student("Ali", 20, 101, "CS")
student1.show_student()
