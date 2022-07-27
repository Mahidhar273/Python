class QuizBrain:
    score = 0

    def __init__(self, q_list):
        self.q_no = 0
        self.score = 0
        self.Qlist = q_list

    def still_has_questions(self):
        return self.q_no < len(self.Qlist)

    def next_question(self):
        current_question = self.Qlist[self.q_no]
        self.q_no += 1
        user_answer = input(f"Q.{self.q_no}: {current_question.text} (True/False): ")
        self.check_answers(user_answer, current_question.answer)

    def check_answers(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Yay")
            self.score += 1
        else:
            print("No Yay")
            print(f"The correct is {correct_answer}")
        print(f"Your score is {self.score}/{self.q_no}")
        print()
