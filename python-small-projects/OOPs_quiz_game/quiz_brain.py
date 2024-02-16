# TODO: 1 . asking the question
# TODO: 2.  checking if the answer was correct
# TODO: 3. checking if we're the end of the quiz


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    # def next_question(self, current_question):
    #     current_question.question_number += 1
    #     current_question.question_list = current_question.question_list[current_question.question_number]
    #     answer_for_cur_question = input(f"Q {current_question.question_number}: {current_question.question_list} : (True/False) : ")
    #     print(answer_for_cur_question)
