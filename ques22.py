#Write a python program that returns the minimum and maximum values
#in a list of numbers.
# Function to find minimum and maximum values in a list of numbers
def find_min_max(numbers):
    if not numbers:
        return None, None

    # Initialize min and max with the first element of the list
    min_value = max_value = numbers[0]

    # Iterate through the list to find min and max values
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num

    return min_value, max_value


# Main function
if __name__ == "__main__":
    try:
        # Taking input from the user
        input_list = input("Enter a list of numbers separated by spaces: ").split()

        # Converting input elements to integers
        numbers = list(map(float, input_list))  # Assuming input could be floating point numbers

        # Finding minimum and maximum values
        min_val, max_val = find_min_max(numbers)

        # Printing the results
        print(f"The minimum value in the list is: {min_val}")
        print(f"The maximum value in the list is: {max_val}")
    except ValueError:
        print("Invalid input format. Please enter numbers separated by spaces.")
