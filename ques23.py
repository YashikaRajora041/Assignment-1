#. Write a program that converts temperature from Celsius to Fahrenheit
#and vice versa based on user input.
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Main function
if __name__ == "__main__":
    try:
        # Taking input from the user
        choice = input(
            "Enter '1' to convert from Celsius to Fahrenheit, or '2' to convert from Fahrenheit to Celsius: ")

        if choice == '1':
            # Convert from Celsius to Fahrenheit
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")

        elif choice == '2':
            # Convert from Fahrenheit to Celsius
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")

        else:
            print("Invalid choice. Please enter '1' or '2'.")

    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")


