Multiplication Quiz in Python
This project is a simple Python script that runs a multiplication quiz directly in your code editor's terminal. It generates random multiplication problems, checks user answers, and tracks the score.

Features
Generates random multiplication problems using numbers between 1 and 10.
Ensures only integer inputs are accepted from the user.
Provides instant feedback (correct/incorrect) after each answer.
Displays the final score after all questions are answered.
Prerequisites
Python 3.x should be installed on your system.
A code editor like Visual Studio Code (VS Code) or any IDE that supports Python.
How to Run the Quiz in VS Code
Open the Project in VS Code:

Clone or download the project files and open the folder in VS Code.
Create a Python File:

Ensure you have a file named multiplication_quiz.py (or any .py file name you prefer).
Paste the script into the file.
Open the Terminal:

In VS Code, press Ctrl + (backtick) or go to View > Terminal to open the integrated terminal.
Run the Script:

In the terminal, run the script using the following command:
bash
Copy code
python multiplication_quiz.py
If you're using Python 3 and it’s configured as python3, use:
bash
Copy code
python3 multiplication_quiz.py
Interact with the Quiz:

Answer each multiplication question in the terminal as prompted.
Customizing the Number of Questions
You can easily change the number of questions asked by modifying this line in the script:

python
Copy code
num_questions = 5
Set it to your preferred number.

Example Output
plaintext
Copy code
Welcome to the Multiplication Quiz!
Question 1:
What is 3 * 6?
Enter your answer: 18
Correct!

Question 2:
What is 7 * 4?
Enter your answer: 28
Correct!

Question 3:
What is 5 * 9?
Enter your answer: 45
Correct!

Your score: 3 out of 3
Additional Notes
Ensure the Python extension is installed in VS Code for syntax highlighting, linting, and easier debugging.
You can set breakpoints and use VS Code’s debugger if you want to step through the code.
Built With
Python 3.12.5
Visual Studio Code
Author
Nancy Kikvadze