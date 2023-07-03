from source import MathOperations
try:
    ops = MathOperations()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    add = ops.add(num1, num2)
    print("Addition:", add)

    sub = ops.subtract(num1, num2)
    print("Subtraction:", sub)

    mul = ops.multiply(num1, num2)
    print("Multiplication:", mul)

    div = ops.divide(num1, num2)
    print("Division:", div)

    sqr = ops.square_root(num1)
    sqr2 = ops.square_root(num2)
    print("Square root of the first number:", sqr)
    print("Square root of the second number:", sqr2)

except ValueError as e:
    print("Invalid input:", e)
except ZeroDivisionError:
    print("Cannot divide by zero")
