#Age Checker

#input
age = input("Enter your age: ")

#Convert age
age = int(age)

#if condition
if age >= 18:
    print("You are eligible to vote")
elif age < 18 and age >= 13:  # Teenager range 13-17
    print("You are a teenager")

#prints after if-block
print("Thank you for using Age Checker!")