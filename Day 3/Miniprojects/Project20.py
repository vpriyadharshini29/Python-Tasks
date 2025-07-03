
# 🔥 20. E-commerce Mini Checkout System
price = float(input("Enter product price: "))
qty = int(input("Enter quantity: "))
code = input("Enter discount code: ")
if code == "SAVE10":
    discount = 0.1
else:
    discount = 0

total = price * qty
total -= total * discount
print(f"Total payable: ₹{total}")