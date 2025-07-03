
# 🔥 15. Bitwise Access Rights Checker
READ = 1
WRITE = 2
EXECUTE = 4
permission = READ | WRITE
print("Has Write?", permission & WRITE != 0)