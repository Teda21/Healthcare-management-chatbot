import tkinter as tk
from tkinter import messagebox
import csv
import os
import subprocess

# Define the CSV file path
CSV_FILE = 'users.csv'

# Function to show the registration window
def show_register_window():
    # Create a new window for the registration form
    register_window = tk.Toplevel(root)
    register_window.title("Registration")
    register_window.geometry("400x300")

    # Create labels and entry fields for username and password
    username_label = tk.Label(register_window, text="Username:")
    username_label.pack(pady=10)
    username_entry = tk.Entry(register_window)
    username_entry.pack(pady=10)

    password_label = tk.Label(register_window, text="Password:")
    password_label.pack(pady=10)
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack(pady=10)

    # Create a register button
    register_button = tk.Button(register_window, text="Register",
                               command=lambda: register(username_entry.get(), password_entry.get()))
    register_button.pack(pady=10)

# Function to register a new user
def register(username, password):
    # Check if the user already exists
    if user_exists(username):
        messagebox.showerror("Error", "Username already exists.")
        return

    # Save the new user to the CSV file
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    messagebox.showinfo("Success", "Registration successful!")

# Function to check if a user exists
def user_exists(username):
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    return True
    except FileNotFoundError:
        pass
    return False

# Function to log in an existing user
def login():
    username = username_entry.get()
    password = password_entry.get()

    if authenticate(username, password):
        messagebox.showinfo("Success", "Login successful!")
        # Navigate to the conversation page
        show_conversation_page()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Function to authenticate user credentials
def authenticate(username, password):
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
    except FileNotFoundError:
        pass
    return False

# Function to show the conversation page
def show_conversation_page():
    # Close the current window
    root.withdraw()

    # Open the "conversation_board.py" file
    subprocess.Popen(['python', 'conversation.py'])

# Create the main window
root = tk.Tk()
root.title("Registration and Login System")
root.geometry("500x400")  # Set the size of the main window

# Create labels and entry fields for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=10)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

# Create login and register buttons
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

register_button = tk.Button(root, text="Register", command=show_register_window)
register_button.pack(pady=10)

root.mainloop()