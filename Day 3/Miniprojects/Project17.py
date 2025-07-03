# 🔥 17. Basic Chat Filter App
banned = ["bad", "spam"]
message = input("Enter your message: ")
if any(word in message for word in banned):
    print("Message blocked")
else:
    print("Message sent")