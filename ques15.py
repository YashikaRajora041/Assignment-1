#Write a program that reads data from a CSV file and prints it to the
#console.
import csv

# Function to read and print data from a CSV file
def read_csv_file(file_name):
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")

# Main function
if __name__ == "__main__":
    file_name = "data.csv"
    read_csv_file(file_name)