#Ask user for age
age = input("Enter your age: ")
#string to integer
age = int(age)
#Check conditions
if age >= 18:
    print("You are eligible to vote")
elif age < 18 and age >= 13:
    print("You are a teenager")
# print
print("Thank you for using Age Checker!")