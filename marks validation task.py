while True:
    # Take input from the user
    user_input = input("Enter marks (0-100) or -1 to stop: ")
    marks = int(user_input)

    # Concept: break (Stop the program when user enters -1)
    if marks == -1:
        print("Program stopped.")
        break

    # Skip and ask again if marks are invalid
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter a value between 0 and 100.")
        continue

    # Determine the grade
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
