# Function to check if a substring is present in a given string
def is_substring_present(main_string, substring):
    return substring in main_string


# Main function
if __name__ == "__main__":
    # Taking input from the user
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to check: ")

    # Checking if the substring is present
    if is_substring_present(main_string, substring):
        print(f"The substring '{substring}' is present in the main string.")
    else:
        print(f"The substring '{substring}' is not present in the main string.")