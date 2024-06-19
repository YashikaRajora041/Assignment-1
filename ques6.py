# Main function
if __name__ == "__main__":
    # Specifying the file name
    file_name = "output.txt"

    try:
        # Reading the content of the file
        with open(file_name, "r") as file:
            content = file.read()

        # Printing the content to the console
        print("Content of the file:")
        print(content)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")