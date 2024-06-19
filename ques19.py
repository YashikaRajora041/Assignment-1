import string


# Function to remove punctuation using string.translate
def remove_punctuation(input_string):
    # Create translation table
    translator = str.maketrans('', '', string.punctuation)

    # Remove punctuation using translate method
    return input_string.translate(translator)


# Main function
if __name__ == "__main__":
    # Taking input from the user
    input_string = input("Enter a string with punctuation: ")

    # Removing punctuation
    cleaned_string = remove_punctuation(input_string)

    # Printing the cleaned string
    print(f"The string without punctuation is:\n{cleaned_string}")
