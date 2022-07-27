from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    new_quest = Question(i["text"], i["answer"])
    question_bank.append(new_quest)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
print("congrats, You completed all the questions")
print(f"Your final score is {quiz.score}")
