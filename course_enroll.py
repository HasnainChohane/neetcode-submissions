python_students = {"ali", "sara", "hamza"}
web_students = {"hamza", "noor", "fatima"}

# Perform set operations and sort the results for predictable output
both_courses = (set(sorted(python_students.intersection(web_students))))
all_students =(set( sorted(python_students.union(web_students))))
python_only = (set(sorted(python_students.difference(web_students))))

# Print the clean, sorted lists
print(f"Both courses: {both_courses}")
print(f"All students: {all_students}")
print(f"Python only: {python_only}")
