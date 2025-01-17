def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x % y

def main():
    print("Welcome to the Basic Calculator program!")
    print("Operations supported: +, -, *, /, %")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /, %): ")

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    elif operator == '%':
        result = modulus(num1, num2)
    else:
        print("Invalid operator. Please enter one of '+', '-', '*', '/', '%'")
        return

    print(f"Result: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
