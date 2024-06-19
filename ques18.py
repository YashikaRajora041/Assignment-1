#. Write a python program that checks if two strings are anagrams of each
#other
# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case insensitivity
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False

    # Count frequency of characters in both strings
    frequency_dict1 = {}
    frequency_dict2 = {}

    for char in str1:
        if char in frequency_dict1:
            frequency_dict1[char] += 1
        else:
            frequency_dict1[char] = 1

    for char in str2:
        if char in frequency_dict2:
            frequency_dict2[char] += 1
        else:
            frequency_dict2[char] = 1

    # Compare the two frequency dictionaries
    return frequency_dict1 == frequency_dict2


# Main function
if __name__ == "__main__":
    # Taking input from the user
    input_str1 = input("Enter the first string: ")
    input_str2 = input("Enter the second string: ")

    # Checking if the strings are anagrams
    if are_anagrams(input_str1, input_str2):
        print(f"'{input_str1}' and '{input_str2}' are anagrams.")
    else:
        print(f"'{input_str1}' and '{input_str2}' are not anagrams.")
