Python Quiz Game
Video Demo: https://youtu.be/-OF5giw9pZo
Description:
The Python Quiz Game is a command-line application that tests the user's knowledge with a series of multiple-choice questions. The program presents each question one at a time, accepts a letter answer from the user (A, B, C, or D), checks whether the answer is correct, and keeps a running score. When all questions have been answered, the program displays the final score as both a raw number and a percentage, along with a short message that changes based on how well the user performed. After each round, the user is offered the chance to play again, which allows the game to be used repeatedly without restarting the program.

The project was built as the final assignment for a Python programming course. It was designed to bring together many of the core concepts covered during the term — functions, lists, dictionaries, loops, conditionals, user input, and string formatting — into a single working program.

File Descriptions

The project consists of three files. The first and most important file is TermProject.py, which contains all of the program's logic. This file defines a main function and four additional functions: load_questions, ask_question, show_score, and play_again. All five functions are defined at the same indentation level.

The load_questions function returns a list of dictionaries, where each dictionary holds one question, its four answer choices, and the letter of the correct answer. Storing the questions in this structure makes it very easy to add, remove, or edit questions without changing any other part of the program. The ask_question function is responsible for displaying a single question and its options, reading the user's answer, converting it to uppercase so that lowercase input still works, and returning True or False depending on whether the answer was correct. The show_score function calculates the percentage by dividing the number of correct answers by the total number of questions and multiplying by one hundred. It then prints a different message depending on whether the user scored 100 percent, at least 70 percent, or below 70 percent. Finally, the play_again function asks whether the user wants another round and returns True or False so the main loop knows whether to continue.

The main function ties everything together. It prints a welcome message, loads the questions, and enters a loop that runs one full round of the quiz. Inside the loop, it calls ask_question for each question, adds to the score when the answer is correct, and prints the correct answer when the user is wrong. After all questions are asked, it calls show_score and then play_again to decide whether to start a new round or end the program.

The second file is requirements.txt, which lists the external libraries required by the project. Because the quiz uses only Python's built-in functions, this file contains a single comment noting that no external libraries are required. The third file is this README.md, which documents the project.

Design Decisions

The most important design decision was to separate the program into small functions, each with a single responsibility. This makes the code easier to read, easier to test, and easier to extend. For example, adding a new question only requires editing the load_questions function, and changing the scoring messages only requires editing show_score. Another key decision was to store questions as dictionaries rather than as separate variables, which keeps all the information about one question together and makes the code more organized. Using a while loop for replay also avoids the need to restart the program, which makes the game more convenient to use. These choices keep the program simple while still demonstrating a clear understanding of good programming structure.

