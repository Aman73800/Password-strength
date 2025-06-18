import tkinter as tk
from tkinter import messagebox
import re


common_words = {
    "password", "admin", "123456", "qwerty", "abc123", "welcome", "login",
    "letmein", "pass", "user", "guest", "test"
}

def check_strength(password):
    suggestions = []
    
    length = len(password)
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[^A-Za-z0-9]', password)

    
    score = 0
    if length >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if has_upper: score += 1
    else: suggestions.append("Add at least one uppercase letter")

    if has_lower: score += 1
    else: suggestions.append("Add at least one lowercase letter")

    if has_digit: score += 1
    else: suggestions.append("Include a number")

    if has_special: score += 1
    else: suggestions.append("Add a special character (e.g. @, #, $)")

    if password.lower() in common_words:
        suggestions.append("Avoid using common dictionary words")

   
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions

def analyze_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password")
        return

    strength, suggestions = check_strength(password)
    result_label.config(text=f"Password Strength: {strength}")
    suggestions_text.delete("1.0", tk.END)
    for s in suggestions:
        suggestions_text.insert(tk.END, f"• {s}\n")

# GUI window setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Check Strength", command=analyze_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

tk.Label(root, text="Suggestions:", font=("Arial", 12)).pack()
suggestions_text = tk.Text(root, height=6, width=45)
suggestions_text.pack()

root.mainloop()
