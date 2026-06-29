student={
 "Name":"Hasnain",
 "Roll_ No":"SOFTF24BSS12",
 "Age":"21",
 "Department":"Engineering Technology",
 "CGPA":"3.77",
}
print("1.Complete Dictionary")
print(student)
print("="*40)

print("2.Student Name")
print(student["Name"])
print("="*40)

student["CGPA"] =3.88
print("3.Update CGPA")
print(f"New CGPA = {student["CGPA"]}")
print("="*40)

student["city"] = "Lahore"
print("4. Dictionary after adding 'city':")
print(student)
print("-" * 40)


student.pop("Age", None) 
print("5. Dictionary after removing 'Age':")
print(student)
print("-" * 40)

print("6. All Keys:")
print(student.keys())
print("-" * 40)

print("7. All Values:")
print(student.values())
print("-" * 40)

print("8. Key-Value Pairs using items():")
for key, value in student.items():
    print(f"{key}: {value}")