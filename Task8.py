student_name = input("Enter student name: ")
python_score = float(input("Enter Python score: "))
english_score = float(input("Enter English score: "))
mathematics_score = float(input("Enter Mathematics score: "))

average = (python_score + english_score + mathematics_score) / 3

print("\n========================================")
print("          STUDENT RESULT")
print("========================================")

print(f"\nStudent: {student_name}")

print(f"\nPython:        {python_score:.0f}")
print(f"English:       {english_score:.0f}")
print(f"Mathematics:   {mathematics_score:.0f}")

print("----------------------------------------")
print(f"Average:       {average:.2f}")
print("========================================")