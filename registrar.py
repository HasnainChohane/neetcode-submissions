student_data = ("Humama", "Python programing", "A+")

# Wrap in a list so enumerate has a collection to loop over
for index, data in enumerate([student_data]):
    # Extract from the tuple 'data' using correct positions
    student = data[0]     
    course = data[1]      
    final_grade = data[2]  
    # Printing statement
    print(f"{student} scored {final_grade} in {course} courses")
