import csv
import os

# Define the CSV file path
CSV_FILE = 'users.csv'


# Function to register a new user
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Check if the user already exists
    if user_exists(username):
        print("Username already exists. Please choose a different username.")
        return

    # Save the new user to the CSV file
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print("Registration successful!")


# Function to check if a user exists
def user_exists(username):
    if not os.path.exists(CSV_FILE):
        return False

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return True
    return False


# Function to log in an existing user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if authenticate(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")


# Function to authenticate user credentials
def authenticate(username, password):
    if not os.path.exists(CSV_FILE):
        return False

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False


# Main function to run the program
def main():
    while True:
        print("\nWelcome to the Registration and Login System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()