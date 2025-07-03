# 🔥 3. Student Grade Evaluator
name = input("Enter your name: ")
marks = [int(input(f"Enter mark {i+1}: ")) for i in range(5)]
average = sum(marks) / 5

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
else:
    grade = 'D'

print(f"{name}, your average is {average}, and grade is {grade}")