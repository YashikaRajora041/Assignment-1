#. Write a program that acts as a simple calculator. It should take two
#numbers and an operator (+, -, *, /) as input and print the result.
# Function to perform arithmetic operations
# Function to perform arithmetic operations
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero is undefined."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator."


# Main function
if __name__ == "__main__":
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        # Performing calculation
        result = calculator(num1, num2, operator)

        # Printing the result
        print(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

