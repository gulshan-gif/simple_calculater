
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid operator"

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

print("Result:", calculator(x, y, operator))
	