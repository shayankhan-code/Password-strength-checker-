Password Strength Checker 🔐

A beginner-friendly Python project that checks password strength using length requirements, character types, common password detection, and repeated-character detection.

📌 Project Overview

This project is a command-line password checker built with Python.

It evaluates passwords using several validation rules and provides feedback about potential weaknesses.

The main goal of this project is to practice Python programming, functions, regular expressions, string manipulation, and basic security concepts.

✨ Features

- Minimum length check: Requires at least 12 characters.
- Lowercase check: Requires at least one lowercase letter.
- Uppercase check: Requires at least one uppercase letter.
- Digit check: Requires at least one number.
- Special character check: Requires at least one special character.
- Common password detection: Detects words such as "password", "123456", "qwerty", and "pakistan".
- Character substitution detection: Detects some common substitutions, such as "@" instead of "a" and "0" instead of "o".
- Repeated character detection: Detects three or more identical consecutive characters.
- Hidden password input: Uses Python's "getpass" module to hide password input in supported terminals.

🛠️ Technologies Used

- Python 3
- Regular Expressions ("re")
- String Manipulation
- "str.maketrans()" and ".translate()"
- "getpass"
- Python Functions

📂 Project Structure

password-checker/
│
├── password_checker.py
├── test_password_checker.py
└── README.md

"test_password_checker.py" is reserved for automated tests currently being developed.

🚀 How to Run

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project directory

cd password-checker

3. Run the program

python password_checker.py

4. Enter a password

The program will ask for a password and display the results.

💻 Example Output

Enter your password:

Common word: False
Repeated characters: False
Strength: strong: password is strong

Example output is illustrative. Do not use a real personal password when testing or sharing screenshots.

🧠 What I Learned

While building this project, I practiced:

- Writing reusable Python functions.
- Using conditional statements and loops.
- Working with regular expressions.
- Manipulating and normalizing strings.
- Detecting common password patterns.
- Using Python's built-in modules.
- Organizing code into separate functions.
- Understanding basic password security concepts.

⚠️ Limitations

This project is an educational password checker, not a complete password security assessment tool.

- It uses a small predefined list of common words.
- Its character substitution detection covers only selected substitutions.
- Its strength rules do not measure true password entropy.
- It does not check whether passwords have appeared in data breaches.
- A password that passes all checks is not necessarily secure.

Do not rely on this project to protect sensitive accounts or production systems.

🔮 Future Improvements

- Add automated tests using Python's "unittest" module.
- Expand common password detection.
- Improve password analysis.
- Add a more user-friendly command-line interface.
- Improve error handling.
- Add more security-focused validation.

👨‍💻 Author

Built as a Python learning project to develop programming and cybersecurity fundamentals.

📜 License

This project is open source under the MIT License (if an MIT LICENSE file is added to the repository).
