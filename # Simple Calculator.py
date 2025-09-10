# Simple Calculator

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
            # Get user input
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
            # Perform calculation
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operator!"
                # Display result
    print("Result:", result)


# Run calculator
calculator()
