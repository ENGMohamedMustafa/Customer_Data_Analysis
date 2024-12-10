class GUI:
    def __init__(self, root):
        self.root = root
        self.backend = Backend()
        self.root.title("Message Application")
        self.root.geometry("400x500")
        self.create_widgets()
        
    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Message input
        self.message_var = tk.StringVar()
        message_entry = ttk.Entry(main_frame, textvariable=self.message_var)
        message_entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.EW)
        
        # Add message button
        add_button = ttk.Button(main_frame, text="Add Message", command=self.add_message)
        add_button.grid(row=0, column=1, padx=5, pady=5)
        
        # Messages display area
        self.messages_text = tk.Text(main_frame, height=20, width=40)
        self.messages_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        # Refresh button
        refresh_button = ttk.Button(main_frame, text="Refresh", command=self.refresh_messages)
        refresh_button.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        # Initial display of messages
        self.refresh_messages()
        
    def add_message(self):
        message = self.message_var.get()
        if self.backend.add_message(message):
            self.message_var.set("")  # Clear input
            self.refresh_messages()
        else:
            messagebox.showwarning("Warning", "Please enter a valid message!")
    
    def refresh_messages(self):
        self.messages_text.delete(1.0, tk.END)
        messages = self.backend.get_messages()
        for msg in messages:
            self.messages_text.insert(tk.END, f"{msg}\n")
