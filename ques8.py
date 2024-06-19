# Function to concatenate two strings
def concatenate_strings(string1, string2):
    return string1 + string2


# Main function
if __name__ == "__main__":
    # Taking input from the user
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    # Concatenating the strings
    result = concatenate_strings(string1, string2)

    # Printing the concatenated result
    print(f"The concatenated string is: {result}")