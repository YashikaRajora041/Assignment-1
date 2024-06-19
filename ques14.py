# Main function

#. Write a program that reads multiple lines of input from the user until they
#  enter an empty line, then prints all the lines.


if __name__ == "__main__":
    lines = []

    print("Enter multiple lines of text. Press Enter on an empty line to finish.")

    # Reading input lines until an empty line is entered
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    # Printing all the entered lines
    print("\nEntered lines:")
    for line in lines:
        print(line)
