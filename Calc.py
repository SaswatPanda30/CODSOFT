def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def floor_divide(x, y):
    return x // y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("This doesn't seem to be a valid number. Please try again.")

def get_operation():
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Modulus (%)")
    print("7. Floor Division (//)")
    
    while True:
        operation = input("Enter the operation (1/2/3/4/5/6/7): ")
        if operation in ['1', '2', '3', '4', '5', '6', '7']:
            return operation
        else:
            print("Invalid ! Please select a valid operation from the list.")

def calculator():
    print("Welcome to the Simple Calculator!")
    
    num1 = get_number("Please enter the first number: ")
    num2 = get_number("Please enter the second number: ")
    operation = get_operation()

    if operation == '1':
        result = add(num1, num2)
        operation_symbol = '+'
    elif operation == '2':
        result = subtract(num1, num2)
        operation_symbol = '-'
    elif operation == '3':
        result = multiply(num1, num2)
        operation_symbol = '*'
    elif operation == '4':
        result = divide(num1, num2)
        operation_symbol = '/'
    elif operation == '5':
        result = exponentiate(num1, num2)
        operation_symbol = '^'
    elif operation == '6':
        result = modulus(num1, num2)
        operation_symbol = '%'
    elif operation == '7':
        result = floor_divide(num1, num2)
        operation_symbol = '//'

    print(f"\nThe result of {num1} {operation_symbol} {num2} is: {result}")

if __name__ == "__main__":
    calculator()