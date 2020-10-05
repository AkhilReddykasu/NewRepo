"""45. Factorial using recursion """

num = int(input("Enter a num to find the factorial:"))


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


print("Factorial of a number is:", fact(num))
