# Function to calculate the length of a string
def string_length(input_string):
    return len(input_string)


# Main function
if __name__ == "__main__":
    # Taking input from the user
    user_input = input("Enter a string: ")

    # Calculating the length of the string
    length = string_length(user_input)

    # Printing the length of the string
    print(f"The length of the string is {length}.")
