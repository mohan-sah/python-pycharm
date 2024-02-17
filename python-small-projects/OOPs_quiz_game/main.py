from question_model import Question
from data2 import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    question_no = Question(question_text, question_answer)
    question_bank.append(question_no)
# for i in question_bank:
#     print(i.text,i.answer)
# print(question_bank)
#
# print(question_bank[0].text)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f" Your final score was : {quiz.score}/{quiz.question_number}")