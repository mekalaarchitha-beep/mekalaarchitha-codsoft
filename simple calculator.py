print("Simple Calculator")
print("Operations: +, -, *, /")
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
op = input("Enter operation (+ - * /):")
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error (division by zero)"
else:
    result = "Invalid operation"
print("Result:", result)
