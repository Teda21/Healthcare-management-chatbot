import json
import openai
import random
import tkinter as tk
import subprocess
from tkinter import messagebox

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        # Load responses from the JSON file
        self.intents = self.load_intents_from_json('data1.json')

        # Create the chat display
        self.chat_display = tk.Text(master, height=20, width=50)
        self.chat_display.grid(row=0, column=0, padx=10, pady=10)

        # Create the input field
        self.input_field = tk.Entry(master, width=50)
        self.input_field.grid(row=1, column=0, padx=10, pady=10)

        # Create the send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=0, padx=10, pady=10)

        # Create the symptom button
        self.symptom_button = tk.Button(master, text="Symptom", command=self.open_symptom_checker)
        self.symptom_button.grid(row=3, column=0, padx=10, pady=10)

    def load_intents_from_json(self, file_path):
        """Load intents from a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            print("JSON data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: The file contains invalid JSON.")
            return {}

    def send_message(self):
        """Handle sending a message and getting a response."""
        user_input = self.input_field.get()
        if user_input.strip():  # Check if input is not empty
            self.chat_display.insert(tk.END, "You: " + user_input + "\n")
            self.input_field.delete(0, tk.END)

            # Get the chatbot's response based on user input
            chatbot_response = self.get_response(user_input)
            self.chat_display.insert(tk.END, "Chatbot: " + chatbot_response + "\n")

    def get_response(self, user_input):
        """Get a response from the loaded intents or OpenAI API based on user input."""
        # Check if the user input matches any patterns in the intents
        for intent in self.intents.get('intents', []):
            if user_input in intent['patterns']:
                return random.choice(intent['responses'])

        # If no match is found, use OpenAI API to generate a response
        return self.get_openai_response(user_input)

    def get_openai_response(self, user_input):
        """Get a response from OpenAI API."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return "I'm sorry, I couldn't get a response from the AI."

    def open_symptom_checker(self):
        """Open the symptom checking script."""
        try:
            subprocess.Popen(['python', 'sympthom cheking.py'])  # Change this to the correct path if necessary
            self.master.withdraw()  # Hide the chatbot window
        except Exception as e:
            messagebox.showerror("Error", f"Could not open symptom checker: {e}")

# Create the main application window
root = tk.Tk()
chatbot_gui = ChatbotGUI(root)
root.mainloop()