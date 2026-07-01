#short introduction by using Function
def intro(name, roll_no, depart, cgpa):
    return f"\nName: {name}, \nRoll No: {roll_no}, \nDepartment: {depart}, \nCGPA: {cgpa}"

# Prompting user for inputs
user_name = input("Enter your name: ")
user_roll = input("Enter your Roll no: ")
user_dept = input("Enter your Department: ")
user_cgpa = input("Enter your CGPA: ")

print(intro(user_name, user_roll, user_dept, user_cgpa))

