
# 🔥 8. Simple Calculator App
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose (+, -, *, /, %, **): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
elif operation == "%":
    result = a % b
elif operation == "**":
    result = a ** b
else:
    result = "Invalid operation"

print("Result:", result)