#use break+else at time to stop loop when found
numbers = [4, 8, 15, 16, 23, 42]
target = 8

for num in numbers:
    if num == target:
        print("Target found!")
        break
else:
    print("Target not found")
