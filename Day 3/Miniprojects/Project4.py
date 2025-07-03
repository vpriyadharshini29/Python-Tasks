
# 🔥 4. Simple ATM Simulation
balance = float(input("Enter initial balance: "))
action = input("Do you want to deposit or withdraw? ")

if action == "deposit":
    amount = float(input("Enter deposit amount: "))
    balance += amount
elif action == "withdraw":
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient balance")

print(f"Current balance: ₹{balance}")
