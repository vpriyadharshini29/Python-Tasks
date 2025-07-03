# Arithmetic Operators Tasks (1–8)

# Task 1: Take two numbers as input and print their addition, subtraction, multiplication, and division.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Task 2: Perform floor division and modulus of two numbers and display with f-string.
print(f"Floor Division: {a // b}, Modulus: {a % b}")

# Task 3: Use exponentiation ** to calculate power of a number.
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Power:", base ** exp)

# Task 4: Create a calculator that takes 2 inputs and prints all arithmetic results (+, -, *, /, //, %, **).
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"+: {x+y}, -: {x-y}, *: {x*y}, /: {x/y}, //: {x//y}, %: {x%y}, **: {x**y}")

# Task 5: Create a shopping app that adds the prices of 3 items.
item1 = float(input("Price of item 1: "))
item2 = float(input("Price of item 2: "))
item3 = float(input("Price of item 3: "))
print("Total cost:", item1 + item2 + item3)

# Task 6: Ask user for marks in 5 subjects and calculate average using arithmetic operators.
marks = [int(input(f"Enter mark {i+1}: ")) for i in range(5)]
print("Average:", sum(marks) / 5)

# Task 7: Convert Celsius to Fahrenheit using arithmetic formula.
celsius = float(input("Enter Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

# Task 8: Use print(f"") to show result of each arithmetic operation with two variables.
x, y = 10, 3
print(f"Sum: {x+y}, Diff: {x-y}, Mul: {x*y}, Div: {x/y}")


#  Comparison Operators Tasks (9–14)
# Task 9: Compare two user-input numbers using all 6 comparison operators and print results.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

# Task 10: Write a program to check if a person is older than 18.
age = int(input("Enter your age: "))
print("Adult" if age > 18 else "Minor")

# Task 11: Take two strings and check if they are equal or not using ==, !=.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Equal" if s1 == s2 else "Not Equal")

# Task 12: Ask for two exam scores and compare which one is higher using >, <.
m1 = int(input("Score 1: "))
m2 = int(input("Score 2: "))
print("Higher:", "m1" if m1 > m2 else "m2")

# Task 13: Use >= and <= to check if the number lies in a particular range.
num = int(input("Enter number: "))
print("In range" if 10 <= num <= 100 else "Out of range")

# Task 14: Create a simple program to check if a user entered score is a passing mark (above 50).
score = int(input("Enter score: "))
print("Pass" if score > 50 else "Fail")


# Logical Operators Tasks (15–20)
# Task 15: Use and to check if age is above 18 and the person has an ID.
age = int(input("Age: "))
has_id = input("Do you have ID (yes/no)? ")
print("Allowed" if age > 18 and has_id == "yes" else "Denied")

# Task 16: Use or to check if a user entered "yes" or "y" as confirmation.
confirm = input("Confirm (yes/y)? ")
print("Confirmed" if confirm == "yes" or confirm == "y" else "Not confirmed")

# Task 17: Use not to reverse a comparison result.
x = 5
print("x is not 10:", not x == 10)

# Task 18: Create a program to allow club entry only if age ≥ 21 and dress code is “formal”.
age = int(input("Age: "))
dress = input("Dress code: ")
if age >= 21 and dress.lower() == "formal":
    print("Allowed in club")
else:
    print("Not allowed")

# Task 19: Ask user two boolean inputs and evaluate them using all logical operators.
a = input("First (True/False): ") == "True"
b = input("Second (True/False): ") == "True"
print("AND:", a and b)
print("OR:", a or b)
print("NOT A:", not a)

# Task 20: Combine multiple conditions using and/or and print pass/fail logic.
score = int(input("Marks: "))
attendance = int(input("Attendance %: "))
print("Pass" if score >= 40 and attendance >= 75 else "Fail")


# Assignment Operators Tasks (21–26)

# Task 21: Initialize a variable with 10 and use +=, -=, *=, /=, //=, %= to update its value.
x = 10
x += 5
x -= 2
x *= 3
x /= 2
x //= 2
x %= 4
print("Final value:", x)

# Task 22: Take a number and increment it by 5 using +=.
n = int(input("Enter number: "))
n += 5
print("Incremented by 5:", n)

# Task 23: Calculate area of a square and double it using *=.
side = int(input("Enter side of square: "))
area = side ** 2
area *= 2
print("Doubled area:", area)

# Task 24: Take a salary amount and apply tax deduction using -=.
salary = float(input("Enter salary: "))
tax = float(input("Enter tax: "))
salary -= tax
print("Salary after tax:", salary)

# Task 25: Build a step-by-step program that modifies a variable using every assignment operator.
v = 10
v += 2
v -= 1
v *= 3
v /= 2
v //= 2
v %= 3
print("Final result:", v)

# Task 26: Create a mini bank balance simulator using assignment operators to update deposits/withdrawals.
balance = 1000
deposit = int(input("Deposit amount: "))
balance += deposit
withdraw = int(input("Withdraw amount: "))
balance -= withdraw
print("Remaining balance:", balance)

# Identity Operators Tasks (27–30)
# Task 27: Compare two identical lists using is and print if they refer to the same memory.
a = [1, 2]
b = a
print("Same memory:", a is b)

# Task 28: Compare two different but equal lists using is not.
x = [1, 2]
y = [1, 2]
print("Different memory:", x is not y)

# Task 29: Show that a = b means both a is b is True (same memory) only for non-mutable objects.
a = 10
b = a
print("Integers memory same:", a is b)

# Task 30: Create three variables, two referencing the same list and one different, compare using is, is not.
l1 = [3, 4]
l2 = l1
l3 = [3, 4]
print("l1 is l2:", l1 is l2)
print("l1 is not l3:", l1 is not l3)


# Membership Operators Tasks (31–35)

# Task 31: Check if a letter is present in a string using in.
letter = input("Enter a letter: ")
print("In string?", letter in "membership")

# Task 32: Ask user for a fruit name and check if it is in your predefined fruit list.
fruits = ['apple', 'banana', 'mango']
choice = input("Enter fruit: ").lower()
print("Available" if choice in fruits else "Not available")

# Task 33: Use not in to check if a number is not in a list.
nums = [1, 2, 3]
n = int(input("Enter number: "))
print("Not in list:", n not in nums)

# Task 34: Search for a word in a sentence using in and display if it’s found.
sentence = "This is a Python learning course."
word = input("Search word: ")
print("Found!" if word in sentence else "Not found!")

# Task 35: Check if a key exists in a dictionary using in.
student = {"name": "Priya", "age": 21}
key = input("Enter key: ")
print("Exists" if key in student else "Does not exist")


# Bitwise Operators Tasks (36–40)

# Task 36: Take two integers and perform bitwise AND (&), OR (|), XOR (^).
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)

# Task 37: Demonstrate NOT (~) on a positive number.
x = int(input("Enter number: "))
print("Bitwise NOT:", ~x)

# Task 38: Perform left shift << and right shift >> on a number and display binary.
num = int(input("Enter number: "))
print("Left shift (x2):", num << 1)
print("Right shift (/2):", num >> 1)

# Task 39: Show binary representation using bin() and apply bitwise operations.
x = 4
y = 3
print("x:", bin(x), "y:", bin(y))
print("x & y:", bin(x & y))

# Task 40: Create a bit mask simulation using bitwise operations for toggling bits.
mask = 0b0101
toggle = 0b0010
result = mask ^ toggle
print("Toggled mask:", bin(result))

#  Conditional Statements – Basic (41–45)
# Task 41: Ask user for age and print if eligible to vote using if.
age = int(input("Age: "))
if age >= 18:
    print("Eligible to vote")

# Task 42: Ask for age, print "Minor" if less than 18, else "Adult" using if-else.
age = int(input("Age: "))
print("Minor" if age < 18 else "Adult")

# Task 43: Ask for marks and print grades.
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")

# Task 44: Ask for temperature and print Hot, Warm, or Cool.
temp = float(input("Temperature: "))
if temp > 35:
    print("Hot")
elif 25 <= temp <= 35:
    print("Warm")
else:
    print("Cool")

# Task 45: Ask for a number and print if it is even or odd using if-else.
num = int(input("Enter number: "))
print("Even" if num % 2 == 0 else "Odd")


# Conditional Statements – Intermediate (46–50)
# Task 46: Ask for username and password using if-else to simulate login check.
username = input("Username: ")
password = input("Password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")

# Task 47: Ask if it's raining, and if user has an umbrella. Use nested if.
raining = input("Is it raining (yes/no)? ")
if raining == "yes":
    umbrella = input("Do you have an umbrella? ")
    if umbrella == "yes":
        print("Go out")
    else:
        print("Stay in")
else:
    print("Go out")

# Task 48: Ask user for age and nationality. Allow voting if age ≥ 18 and nationality is "Indian".
age = int(input("Enter age: "))
nation = input("Nationality: ")
if age >= 18 and nation.lower() == "indian":
    print("Can vote")
else:
    print("Cannot vote")

# Task 49: Build a calculator with add, sub, mul, div.
op = input("Choose operation (add/sub/mul/div): ")
a = int(input("a: "))
b = int(input("b: "))
if op == "add":
    print("Result:", a + b)
elif op == "sub":
    print("Result:", a - b)
elif op == "mul":
    print("Result:", a * b)
elif op == "div":
    print("Result:", a / b)
else:
    print("Invalid operation")

# Task 50: Ask for exam result (marks, attendance). Pass if marks ≥ 40 and attendance ≥ 75%.
marks = int(input("Marks: "))
attendance = int(input("Attendance %: "))
if marks >= 40 and attendance >= 75:
    print("Passed")
else:
    print("Failed")




