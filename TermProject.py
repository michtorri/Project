"""
TermProject.py
A simple multiple-choice quiz game.
"""


def load_questions():
    """Return a list of quiz questions.
    Each question is a dictionary with:
    - question: the text
    - options: the four choices
    - answer: the letter of the correct choice
    """
    return [
        {
            "question": "What does CPU stand for?",
            "options": ["A. Central Processing Unit",
                        "B. Computer Personal Unit",
                        "C. Central Program Utility",
                        "D. Control Processing Unit"],
            "answer": "A"
        },
        {
            "question": "Which data structure stores items in key-value pairs?",
            "options": ["A. List",
                        "B. Tuple",
                        "C. Dictionary",
                        "D. Set"],
            "answer": "C"
        },
        {
            "question": "What keyword defines a function in Python?",
            "options": ["A. function",
                        "B. def",
                        "C. func",
                        "D. define"],
            "answer": "B"
        },
        {
            "question": "Which of these is a valid Python comment?",
            "options": ["A. // comment",
                        "B. <!-- comment -->",
                        "C. # comment",
                        "D. /* comment */"],
            "answer": "C"
        },
        {
            "question": "What does the len() function do?",
            "options": ["A. Sorts a list",
                        "B. Returns the length of an object",
                        "C. Converts to lowercase",
                        "D. Opens a file"],
            "answer": "B"
        }
    ]


def ask_question(question_data):
    """Display one question, get the user's answer,
    and return True if correct, False otherwise.
    """
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print("  " + option)

    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    return answer == question_data["answer"]


def show_score(score, total):
    """Print the final score and a message based on performance."""
    print("\n" + "=" * 40)
    print(f"Your score: {score} out of {total}")
    percentage = (score / total) * 100
    print(f"That's {percentage:.1f}%")

    if percentage == 100:
        print("Perfect score! Excellent work!")
    elif percentage >= 70:
        print("Good job! Keep practicing.")
    else:
        print("Nice try — review and try again.")


def play_again():
    """Ask the user if they want another round.
    Return True for yes, False for no.
    """
    choice = input("\nPlay again? (y/n): ").strip().lower()
    return choice == "y"


def main():
    """Run the quiz game."""
    print("Welcome to the Python Quiz!")
    print("Answer each question with A, B, C, or D.")

    questions = load_questions()
    playing = True

    while playing:
        score = 0
        for question in questions:
            if ask_question(question):
                score += 1
                print("Correct!")
            else:
                print(f"Incorrect. The answer was {question['answer']}.")

        show_score(score, len(questions))
        playing = play_again()

    print("\nThanks for playing. Goodbye!")


if __name__ == "__main__":
    main()
