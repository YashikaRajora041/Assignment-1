#Write a program in python that counts the frequency of each character in
#a string.
# Function to count the frequency of each character in a string
def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    frequency_dict = {}

    # Count frequency of each character
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict


# Main function
if __name__ == "__main__":
    # Taking input from the user
    input_string = input("Enter a string: ")

    # Calculating character frequencies
    frequency_dict = count_character_frequency(input_string)

    # Printing the frequency of each character
    print("Character frequencies:")
    for char, freq in frequency_dict.items():
        print(f"{char}: {freq}")
