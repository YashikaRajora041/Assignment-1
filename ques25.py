# Write a program that copies the contents of one text file to another.
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as dest:
                dest.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("One of the files does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        source_file = input("Enter the source file name: ")
        destination_file = input("Enter the destination file name: ")

        copy_file(source_file, destination_file)
    except KeyboardInterrupt:
        print("\nProcess interrupted.")
