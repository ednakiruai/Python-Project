import tkinter as tk  # Import the tkinter module for GUI

# Global variable to store the calculation
calculation = ""

# Initialize the main application window
root = tk.Tk()
root.geometry("350x300")  # Set window size
root.title("Group 9 Simple Calculator")  # Set window title

# Create the display field
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)  # Span across multiple columns