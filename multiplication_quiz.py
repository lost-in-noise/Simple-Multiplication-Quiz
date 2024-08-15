import random

def multiplication_quiz(num_questions):
    score = 0

    for i in range(1, num_questions + 1):
        # Generate two random integers between 1 and 10
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        
        # Present the question to the user
        print(f"Question {i}:")
        print(f"What is {num1} * {num2}?")
        
        # Get the user's answer and validate input
        while True:
            try:
                user_answer = int(input("Enter your answer: "))
                break
            except ValueError:
                print("Please enter a valid integer.")

        # Check if the user's answer is correct
        correct_answer = num1 * num2
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.\n")

    # Display the final score
    print(f"Your score: {score} out of {num_questions}")

# Run the quiz with a specified number of questions
if __name__ == "__main__":
    print("Welcome to the Multiplication Quiz!")
    num_questions = 5  # You can change this value to present more or fewer questions
    multiplication_quiz(num_questions)
