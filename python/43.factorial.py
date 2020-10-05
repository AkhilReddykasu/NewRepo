"""43. factorial"""

num = int(input("Enter a number to find the factorial:"))
r = 1
for i in range(1, num + 1):
    r *= i

print("Factorial of a number is:", r)
