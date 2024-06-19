def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result


# Main function
if __name__ == "__main__":
    # Taking input from the user
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            # Calculating the factorial
            result = factorial(number)

            # Printing the result
            print(f"The factorial of {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")