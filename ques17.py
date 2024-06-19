#Write a program in python that converts a given string to title case (first
#letter of each word capitalized).
# Function to convert a string to title case
def title_case(input_string):
    # Split the input string into words
    words = input_string.split()

    # Initialize an empty list to store capitalized words
    title_case_words = []

    # Capitalize the first letter of each word and concatenate them
    for word in words:
        capitalized_word = word.capitalize()
        title_case_words.append(capitalized_word)

    # Join the capitalized words into a title case string
    title_case_string = ' '.join(title_case_words)

    return title_case_string


# Main function
if __name__ == "__main__":
    # Taking input from the user
    input_string = input("Enter a string to convert to title case: ")

    # Converting the string to title case
    title_case_string = title_case(input_string)

    # Printing the title case string
    print(f"The string in title case is: {title_case_string}")
