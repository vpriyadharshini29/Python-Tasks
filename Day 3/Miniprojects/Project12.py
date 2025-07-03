
# 🔥 12. Driving License Eligibility System
age = int(input("Enter age: "))
has_aadhar = input("Do you have Aadhar? (yes/no): ")
if age >= 18:
    if has_aadhar == "yes":
        print("Eligible for license")
    else:
        print("Aadhar required")
else:
    print("Not eligible")
