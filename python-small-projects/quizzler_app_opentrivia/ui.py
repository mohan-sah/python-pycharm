from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        # ("Ariel",20,"italic")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=250,
                                                     text="text goes here",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score : 0", font=("Ariel", 20, "bold"), background=THEME_COLOR,
                                 foreground="white")
        self.score_label.grid(row=0, column=1)
        self.score_label.config(padx=20, pady=20)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.action_true, pady=20, padx=20)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.action_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text =f"Score : {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of Question")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def action_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def action_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config( background="green")
        else:
            self.canvas.config( background="red")

        self.window.after(200, func=self.get_next_question)

