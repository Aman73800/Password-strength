# 🔐 Password Strength Checker (Python GUI)

A beginner-friendly desktop application built using **Python** and **Tkinter** to evaluate and display the strength of user-entered passwords. It also provides real-time suggestions to help users create stronger and more secure passwords.

---

## 📌 Features

* GUI built with `tkinter`
* Checks password strength based on:

  * Length
  * Uppercase and lowercase letters
  * Numbers
  * Special characters
  * Common password patterns (e.g., "password", "123456")
* Displays strength: **Weak**, **Moderate**, or **Strong**
* Suggests improvements for weak or moderate passwords

---

## 🛠️ Tech Stack

* **Python 3**
* **Tkinter** (for GUI)
* **re** module (for regex-based pattern checks)

---

## 🖥️ How It Works

* The user enters a password in the input field
* On clicking "Check Strength":

  * The password is analyzed for character types and length
  * It’s scored and categorized into Weak / Moderate / Strong
  * Suggestions are displayed to guide improvement

### Sample Output:

```
Password Strength: Moderate
Suggestions:
• Add at least one uppercase letter
• Add a special character (e.g. @, #, $)
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed

### Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Aman73800/Password-strength.git

   ```

2. Run the script:

   ```bash
   python pass.py
   ```

---

## 📁 File Structure

```
pass.py        # Main GUI script with logic and suggestions
```

---

## 📚 Learning Outcome

* GUI development with `tkinter`
* String pattern validation using `re`
* Building user-friendly feedback systems

---

## 🙌 Acknowledgments

This project was built as **Internship Task 2** at \[YourCompanyName].
Thanks to the team for guidance and support.

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

📬 Feel free to connect or contribute!
