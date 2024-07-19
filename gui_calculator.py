import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_letters, use_digits, use_special):
    """
    Generate a random password based on specified criteria.
    
    Parameters:
    length (int): Desired length of the password
    use_letters (bool): Include letters in the password
    use_digits (bool): Include digits in the password
    use_special (bool): Include special characters in the password
    
    Returns:
    str: Generated password
    """
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length should be a positive integer.")
        use_letters = var_letters.get()
        use_digits = var_digits.get()
        use_special = var_special.get()
        
        password = generate_password(length, use_letters, use_digits, use_special)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")

# Length label and entry
label_length = tk.Label(root, text="Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Checkbuttons for character sets
var_letters = tk.BooleanVar(value=True)
check_letters = tk.Checkbutton(root, text="Include Letters", variable=var_letters)
check_letters.grid(row=1, column=0, columnspan=2)

var_digits = tk.BooleanVar(value=True)
check_digits = tk.Checkbutton(root, text="Include Digits", variable=var_digits)
check_digits.grid(row=2, column=0, columnspan=2)

var_special = tk.BooleanVar(value=True)
check_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special)
check_special.grid(row=3, column=0, columnspan=2)

# Generate button
button_generate = tk.Button(root, text="Generate Password", command=on_generate)
button_generate.grid(row=4, column=0, columnspan=2, pady=10)

# Entry to display the generated password
entry_password = tk.Entry(root, width=50)
entry_password.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
