#Write a python program that takes a list of numbers and returns their sum
# Function to calculate the sum of numbers in a list
def calculate_sum(numbers):
    return sum(numbers)


# Main function
if __name__ == "__main__":
    try:
        # Taking input from the user
        numbers = input("Enter numbers separated by spaces: ").split()

        # Converting input strings to integers
        numbers = list(map(int, numbers))

        # Calculating the sum
        total_sum = calculate_sum(numbers)

        # Printing the sum
        print(f"The sum of the numbers is: {total_sum}")
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
