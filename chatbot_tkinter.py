import tkinter as tk

# Define the chatbot's simple response logic
def get_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today? 😊"
    elif "order" in user_input:
        return "You can track your order by providing your Order ID."
    elif "shipping" in user_input:
        return "We offer free shipping on orders over $50!"
    elif "contact" in user_input:
        return "You can contact our support team at support@example.com 📧"
    elif "bye" in user_input:
        return "Goodbye! Have a great day! 👋"
    else:
        return "I'm sorry, I didn't understand that. Please try asking something else."

# Function to update chat window
def send_message():
    user_input = entry_box.get()
    chat_log.config(state=tk.NORMAL)
    
    if user_input.strip() != "":
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        bot_response = get_response(user_input)
        chat_log.insert(tk.END, "Bot: " + bot_response + "\n\n")
    
    entry_box.delete(0, tk.END)
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

# Set up the main window
root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("400x500")
root.resizable(False, False)

# Chat window
chat_log = tk.Text(root, bd=1, bg="white", font=("Arial", 12), wrap="word", state=tk.DISABLED)
chat_log.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Entry box for user input
entry_box = tk.Entry(root, bd=1, font=("Arial", 12))
entry_box.pack(pady=10, padx=10, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=send_message)
send_button.pack(pady=5)

# Allow pressing Enter to send
root.bind('<Return>', lambda event: send_message())

# Start the GUI loop
root.mainloop()
