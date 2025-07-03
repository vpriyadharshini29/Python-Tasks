# 🔥 19. Mobile Recharge Validator
number = input("Enter mobile number: ")
amount = int(input("Enter recharge amount: "))
if len(number) == 10 and amount > 10:
    print("Recharge successful")
else:
    print("Invalid details")