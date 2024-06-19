# Function to calculate the sum of the digits of a given number
def sum_of_digits(number):
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    return sum_digits


# Main function
if __name__ == "__main__":
    try:
        # Taking input from the user
        number = int(input("Enter a number: "))

        # Handling negative numbers
        if number < 0:
            print("Please enter a non-negative number.")
        else:
            # Calculating the sum of the digits
            result = sum_of_digits(number)

            # Printing the result
            print(f"The sum of the digits of {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
