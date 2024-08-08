import csv
import json
import os
import tkinter as tk
from tkinter import messagebox

# Define the CSV file path
CSV_FILE = 'appointments.csv'

# Function to load existing appointments from a CSV file
def load_appointments(file_path):
    appointments = []
    if os.path.exists(file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                appointments.append(row)
    return appointments

# Function to save appointments to a CSV file
def save_appointments(file_path, appointments):
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['name', 'appointment_time', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Write the header
        for appointment in appointments:
            writer.writerow(appointment)

# Function to create an appointment
def create_appointment(name, date, time, description):
    appointment_time = f"{date} {time}"
    appointment = {
        'name': name,
        'appointment_time': appointment_time,
        'description': description
    }
    return appointment

# Function to handle user input and create an appointment
def handle_user_input():
    name = name_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    description = description_entry.get()

    # Validate inputs
    if not name or not date or not time or not description:
        messagebox.showerror("Error", "All fields must be filled out.")
        return

    # Create the appointment
    appointment = create_appointment(name, date, time, description)

    # Load existing appointments and add the new one
    appointments = load_appointments(CSV_FILE)
    appointments.append(appointment)

    # Save the updated list of appointments
    save_appointments(CSV_FILE, appointments)

    # Show success message
    messagebox.showinfo("Success", "Your appointment has been created!")
    print("Your appointment has been created:")
    print(json.dumps(appointment, indent=4))

# Create the main window
root = tk.Tk()
root.title("Appointment Scheduler")
root.geometry("400x300")

# Create labels and entry fields for appointment details
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Date (YYYY-MM-DD):").pack(pady=5)
date_entry = tk.Entry(root)
date_entry.pack(pady=5)

tk.Label(root, text="Time (HH:MM):").pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack(pady=5)

tk.Label(root, text="Description:").pack(pady=5)
description_entry = tk.Entry(root)
description_entry.pack(pady=5)

# Create a button to submit the appointment
submit_button = tk.Button(root, text="Create Appointment", command=handle_user_input)
submit_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()