import json
import tkinter as tk
from tkinter import messagebox

# Sample data: symptoms and their associated conditions
symptom_data = {
    "headache": ["migraine", "tension headache", "cluster headache"],
    "fever": ["flu", "COVID-19", "common cold"],
    "cough": ["flu", "common cold", "COVID-19"],
    "sore throat": ["common cold", "strep throat", "allergies"],
    "fatigue": ["anemia", "depression", "chronic fatigue syndrome"]
}

def load_symptom_data(file_path):
    """Load symptom data from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return symptom_data  # Return default data if file not found
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON.")
        return symptom_data  # Return default data if JSON is invalid

def check_symptoms(symptoms):
    """Check the provided symptoms and return potential conditions."""
    conditions = []
    for symptom in symptoms:
        if symptom in symptom_data:
            conditions.extend(symptom_data[symptom])
        else:
            conditions.append(f"No conditions found for symptom: {symptom}")
    return conditions

class SymptomCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Symptom Checker")

        # Create labels and entry fields
        self.label = tk.Label(master, text="Enter your symptoms (comma separated):")
        self.label.pack(pady=10)

        self.symptoms_entry = tk.Entry(master, width=50)
        self.symptoms_entry.pack(pady=10)

        self.check_button = tk.Button(master, text="Check Symptoms", command=self.check_symptoms)
        self.check_button.pack(pady=10)

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack(pady=10)

    def check_symptoms(self):
        """Handle the symptom checking logic."""
        user_input = self.symptoms_entry.get().lower()
        user_symptoms = [symptom.strip() for symptom in user_input.split(',') if symptom.strip()]

        if not user_symptoms:
            messagebox.showerror("Input Error", "Please enter at least one symptom.")
            return

        conditions = check_symptoms(user_symptoms)

        # Clear the previous results
        self.result_text.delete(1.0, tk.END)

        # Display the results
        self.result_text.insert(tk.END, "Potential conditions based on your symptoms:\n")
        for condition in conditions:
            self.result_text.insert(tk.END, f"- {condition}\n")

# Create the main application window
root = tk.Tk()
app = SymptomCheckerApp(root)
root.mainloop()