# concepts: conditionals, math

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose (+, -, *, /, **, %)")

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by 0")

elif operation == "**":
    result = num1 ** num2

elif operation == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        print("Cannot mod by 0")

else:
    print("Invalid operation")

print(f"Result: {result}")