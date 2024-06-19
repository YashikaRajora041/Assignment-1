def greet_user(name):
    return f"Hello, {name}! Welcome!"


# Main function
if __name__ == "__main__":
    # Taking input from the user
    name = input("Enter your name: ")

    # Generating the greeting message
    greeting_message = greet_user(name)

    # Printing the greeting message
    print(greeting_message)