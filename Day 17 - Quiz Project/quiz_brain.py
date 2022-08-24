class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number} : {q.text} (True/False) ")
        self.check_answer(choice, q.answer)
        print(f"You got {self.score} / {self.question_number} correct")
        print()
        print()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, choice, answer):
        if choice.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"Sorry, that was wrong. The correct answer was {answer}")
