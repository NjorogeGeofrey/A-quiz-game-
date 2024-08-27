from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

Question_bank = []

for question in question_data:
    Quiz = Question(question["text"], question["answer"])
    Question_bank.append(Quiz)

quiz = QuizBrain(Question_bank)
while quiz.still_has_questions():
    quiz.next_question()
quiz.final_score()
