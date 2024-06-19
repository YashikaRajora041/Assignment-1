def add_numbers(num1, num2):
    return num1 + num2


# Main function
if __name__ == "__main__":
    # Taking input from the user
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        # Calculating the sum
        result = add_numbers(number1, number2)

        # Printing the result
        print(f"The sum of {number1} and {number2} is {result}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")