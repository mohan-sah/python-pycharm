from question_model import Question
from data import question_data
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

new_question = QuizBrain(question_bank)
asking_question = True
while asking_question:
    i = 1
    new_question.next_question(new_question)

    i += 1
    if i == len(question_bank) -1:
        asking_question = False

