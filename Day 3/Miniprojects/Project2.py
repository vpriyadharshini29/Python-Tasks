
# 🔥 2. Electricity Bill Calculator
name = input("Enter your name: ")
units = int(input("Enter units consumed: "))

if units <= 100:
    rate = 2
elif units <= 300:
    rate = 3
else:
    rate = 5

bill = units * rate
print(f"Hello {name}, your bill is ₹{bill}")