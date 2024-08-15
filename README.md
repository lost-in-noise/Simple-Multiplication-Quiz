# Multiplication Quiz in Python

This project is a simple Python script that runs a multiplication quiz directly in your code editor's terminal. It generates random multiplication problems, checks user answers, and tracks the score.

## Features

- Generates random multiplication problems using numbers between 1 and 10.
- Ensures only integer inputs are accepted from the user.
- Provides instant feedback (correct/incorrect) after each answer.
- Displays the final score after all questions are answered.

## How It Works

1. The quiz asks a series of multiplication questions (e.g., "What is 3 \* 4?").
2. The user inputs their answer.
3. The program checks if the answer is correct and provides feedback.
4. After all questions are answered, the user’s final score is displayed.

## Getting Started

### Prerequisites

- Python 3.12.5 should be installed on your system.
- A code editor like [Visual Studio Code (VS Code)](https://code.visualstudio.com/) or any IDE that supports Python.

## How to Run the Quiz in VS Code

1. **Open the Project in VS Code:**

   - Clone or download the project files and open the folder in VS Code.

2. **Create a Python File:**

   - Ensure you have a file named `multiplication_quiz.py` (or any `.py` file name you prefer).
   - Paste the script into the file.

3. **Open the Terminal:**

   - In VS Code, press ` Ctrl + \`` (backtick) or go to  `View > Terminal` to open the integrated terminal.

4. **Run the Script:**

   - In the terminal, run the script using the following command:
     ```bash
     python multiplication_quiz.py
     ```
   - If you're using Python 3 and it’s configured as `python3`, use:
     ```bash
     python3 multiplication_quiz.py
     ```

5. **Interact with the Quiz:**
   - Answer each multiplication question in the terminal as prompted.

## Customizing the Number of Questions

You can easily change the number of questions asked by modifying this line in the script:

```python
num_questions = 5
```

Set the value to your desired number of questions.

### Example Output
```bash
Welcome to the Multiplication Quiz!
Question 1:
What is 4 * 5?
Enter your answer: 20
Correct!

Question 2:
What is 7 * 8?
Enter your answer: 56
Correct!

Question 3:
What is 9 * 3?
Enter your answer: 28
Incorrect. The correct answer is 27.

Your score: 2 out of 3
```
### Built With
Python 3.x

Visual Studio Code 

### Author
Nancy Kikvadze
