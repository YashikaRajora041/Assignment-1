# Function to calculate age based on birth year
def calculate_age(birth_year):
    current_year = 2024  # Replace with the current year or use datetime.datetime.now().year for dynamic current year
    age = current_year - birth_year
    return age


# Main function
if __name__ == "__main__":
    try:
        # Taking input from the user
        birth_year = int(input("Enter your birth year: "))

        # Calculating the age
        age = calculate_age(birth_year)

        # Printing the age
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")
