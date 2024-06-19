#Write a program in python that converts a string into a list of its characters.
def string_to_list_using_comprehension(input_string):
    # Using list comprehension to convert string to list of characters
    char_list = [char for char in input_string]
    return char_list


if __name__ == "__main__":
    input_string = input("Enter a string: ")

    # Convert string to list of characters using list comprehension
    char_list = string_to_list_using_comprehension(input_string)

    # Print the list of characters
    print(f"The string '{input_string}' converted to a list of characters is:")
    print(char_list)

