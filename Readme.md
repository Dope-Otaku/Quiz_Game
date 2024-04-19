# DSA PROJECT-1 EASY MODE

class QuizGame:
"""
A class representing a quiz game app based on data structures and algorithms.
"""

    def __init__(self):
        """
        Initializes a new instance of the QuizGame class.
        """
        self.questions = []
        self.score = 0

    def add_question(self, question, answer):
        """
        Adds a new question to the quiz game.

        Args:
            question (str): The question to be added.
            answer (str): The correct answer to the question.
        """
        self.questions.append((question, answer))

    def play_game(self):
        """
        Starts the quiz game and allows the user to play.

        Returns:
            int: The final score of the player.
        """
        for question, answer in self.questions:
            user_answer = input(question)
            if user_answer == answer:
                self.score += 1

        return self.score
