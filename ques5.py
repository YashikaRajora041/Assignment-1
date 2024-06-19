# Main function
if __name__ == "__main__":
    # Taking input from the user
    user_input = input("Enter a string to write to the file: ")

    # Specifying the file name
    file_name = "output.txt"

    # Writing the input to the file
    with open(file_name, "w") as file:
        file.write(user_input)

    # Informing the user that the input has been written to the file
    print(f"Your input has been written to {file_name}.")