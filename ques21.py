#Write a python program that counts the occurrences of a specific element
#in a list
# Function to count occurrences of an element in a list
def count_occurrences(input_list, element):
    count = 0
    for item in input_list:
        if item == element:
            count += 1
    return count


# Main function
if __name__ == "__main__":
    try:
        # Taking input from the user
        input_list = input("Enter a list of elements separated by spaces: ").split()
        element = input("Enter the element to count: ")

        # Converting input elements to appropriate types (if needed)
        # Assuming input elements are already in desired type (string, int, etc.)

        # Counting occurrences of the element
        occurrences = count_occurrences(input_list, element)

        # Printing the count of occurrences
        print(f"The element '{element}' occurs {occurrences} times in the list.")
    except ValueError:
        print("Invalid input format.")
