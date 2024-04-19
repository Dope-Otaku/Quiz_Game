#quiz_game

class Quiz:
    def __init__(self):
        self.questions = []     #initiated a questions list where questions and their answers will be stored
        self.score = 0          #initiated a score variable where total score will be stored

    def add_question(self, question, answer):  #calling this function will store a question and answer pair to code    
        self.questions.append((question, answer))
        # return f"{question}: {answer}"    #just to check the functionality

    def play_game(self):    #you can start the game by invoking this
        for question, answer in self.questions:
            user_answer = input(question)
            if user_answer == answer:
                self.score += 1
        return f"Your total score is {self.score}"
    
    def quit(self):
        self.questions = []
        self.score = 0
        return f"Thank you for playing this game!"


new = Quiz()

print("Welcome to a quiz game")
playing = input("Do you want to play the game? (yes/no) ")
if playing != "yes":
    quit()

print("Okay! Let's play: ")
print(new.add_question("what is my name? ", "example"))
print(new.add_question("what is my gfname? ", "example"))
print(new.add_question("what is my father's name? ", "example"))
print(new.add_question("what is my mother's name? ", "example"))
print(new.add_question("what is my dog's name? ", "example"))
print(new.play_game())






