def add (a,b):
    return a + b

def sub (a,b):
    return a - b

def mul (a,b):
    return a * b

def div (a,b):
    return a / b

def average (a,b):
    return (a + b) / 2

operation = input("Enter operation you want to perform \n" \
    "1. Addition\n" \
    "2. Subtraction\n" \
    "3. Multiplication\n" \
    "4. Division\n" \
    "5. Average\n")

print("Select a operation from 1,2,3,4,5")
if operation not in ("1", "2", "3", "4", "5"):
    print("Invalid operation")
    exit()
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


if operation == "1":
    print("Sum of", a, "and", b, "is", add(a, b))
elif operation == "2":
    print("Difference of", a, "and", b, "is", sub(a, b))
elif operation == "3":
    print("Product of", a, "and", b, "is", mul(a, b))
elif operation == "4":
    print("Quotient of", a, "and", b, "is", div(a, b))
elif operation == "5":
    print("Average of", a, "and", b, "is", average(a, b))
