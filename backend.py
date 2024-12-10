import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

class Backend:
    def __init__(self):
        self.data_file = "messages.json"
        self.messages = []
        self.load_data()
    
    def load_data(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    self.messages = json.load(file)
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def save_data(self):
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.messages, file)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_message(self, message):
        if message.strip():
            self.messages.append(message)
            self.save_data()
            return True
        return False
    
    def get_messages(self):
        return self.messages
