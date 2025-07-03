
# 🔥 13. Salary Tax Deduction Calculator
salary = float(input("Enter salary in LPA: "))
if salary < 5:
    tax = 0
elif salary <= 10:
    tax = 0.1 * salary
else:
    tax = 0.2 * salary

net = salary - tax
print(f"Net salary after tax: {net} LPA")