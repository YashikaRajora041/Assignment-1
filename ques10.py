# Function to convert a string to uppercase
def convert_to_uppercase(input_string):
    return input_string.upper()


# Main function
if __name__ == "__main__":
    # Taking input from the user
    user_input = input("Enter a string: ")

    # Converting the string to uppercase
    uppercase_string = convert_to_uppercase(user_input)

    # Printing the uppercase string
    print(f"The uppercase string is: {uppercase_string}")
