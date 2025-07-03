# 🔥 10. Access Control Based on Role
role = input("Enter role (admin/user): ")
has_id = input("Do you have ID (yes/no): ")
if role == "admin":
    if has_id == "yes":
        print("Access granted")
    else:
        print("ID required")
else:
    print("User access limited")