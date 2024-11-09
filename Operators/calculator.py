print("Welcome to the Basic Calculator!")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter choice (1/2/3/4): ")

if operation in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        print("Result:", num1 + num2)
    elif operation == '2':
        print("Result:", num1 - num2)
    elif operation == '3':
        print("Result:", num1 * num2)
    elif operation == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero!")
else:
    print("Invalid input! Please select a valid operation.")
