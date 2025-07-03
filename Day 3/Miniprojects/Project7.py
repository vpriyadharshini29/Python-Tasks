
# 🔥 7. Product Discount System
product = input("Enter product name: ")
price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

final_price = price - (price * discount / 100)
print(f"{product} after {discount}% discount is ₹{final_price}")