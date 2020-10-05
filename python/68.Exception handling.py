"""Exception handling"""

a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

try:
    print("resource open")
    print("Value after division:", a/b)
    n = int(input("Enter a number:"))
    print("value of n -", n)
except ValueError:
    print("Input invalid...")
except ZeroDivisionError:
    print("divided by zero")
except Exception as e:
    print('divided by zero : ', e)
finally:
    print('resource close')

