# Function to generate the first n numbers in the Fibonacci sequence
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


# Main function
if __name__ == "__main__":
    try:
        # Taking input from the user
        n = int(input("Enter the number of Fibonacci numbers to generate: "))

        if n <= 0:
            print("Please enter a positive integer.")
        else:
            # Generating the Fibonacci sequence
            fibonacci_sequence = generate_fibonacci(n)

            # Printing the Fibonacci sequence
            print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_sequence}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
