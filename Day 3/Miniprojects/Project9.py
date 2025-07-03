
# 🔥 9. User Age Classification System
name = input("Enter name: ")
age = int(input("Enter age: "))
if age < 13:
    group = "Child"
elif age <= 19:
    group = "Teenager"
elif age <= 59:
    group = "Adult"
else:
    group = "Senior"

print(f"{name} is classified as {group}")