def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


# Main function
if __name__ == "__main__":
    # Taking input from the user
    try:
        number = int(input("Enter a number: "))

        # Checking if the number is even or odd
        result = check_even_odd(number)

        # Printing the result
        print(f"The number {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")