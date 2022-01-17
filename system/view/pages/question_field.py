from tkinter import *
# from tkinter.font import Font
import os

from control.next_button import load_new_question
from model.questions import Question, QuestionType
from view.inputs.single_option import RadioButtonField
from view.inputs.multiple_options import CheckButtonField
from view.inputs.text_input import TextFields
from view.theme import Theme
from model.disclaimer import Disclaimer


class QuestionField:

    def __init__(self, master, kb_class, main_app):
        self.master = master
        self.main_app = main_app

        self.button = None
        self.question_field = None
        self.input_field = None
        self.options = None

        self.disclaimer = Disclaimer()
        self.visited = ['start']
        self.kb_class = kb_class

        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.frame.pack()

        self.question_text = StringVar()
        self.question_class = Question()
        self.question = self.question_class.get_questions()[0]

        self.add_question_field(self.frame)
        self.add_text(self.question[0])
        self.add_input_field()
        self.add_save_button(self.frame)

    def add_question_field(self, scrollable_frame):
        self.question_field = Label(scrollable_frame,
                                    textvariable=self.question_text,
                                    width=140,
                                    wraplength=650,
                                    justify=CENTER,
                                    font=("Arial", 20),
                                    fg=Theme.TEXT_COLOUR,
                                    bg=Theme.BG_COLOUR,
                                    bd=0)
        self.question_field.pack(pady=20)

    def add_text(self, text):
        self.question_text.set(text)

    def add_save_button(self, frame):
        """
        Adds 'next' button to frame which loads new question
        :param frame: frame to place button in
        """
        self.button = Button(frame, text="NEXT",
                             font=('Arial', 15, 'bold'),
                             padx=7,
                             pady=7,
                             relief=RAISED,
                             bg=Theme.NEXT_BUTTON_COLOUR,
                             fg=Theme.TEXT_COLOUR,
                             activebackground=Theme.BUTTON_CLICK,
                             activeforeground='white',
                             command=lambda: load_new_question(self, self.kb_class, self.question_class, self.question,
                                                               self.input_field))
        self.button.pack(side="bottom", expand=True, pady=20)

    def add_input_field(self):
        """
        Adds an input field to the frame
        """
        # if 'diploma' in self.question:
        if self.question[1] == QuestionType.SELECT:
            self.input_field = RadioButtonField(self.frame, self.question[2])

        # elif 'subject' in self.question:
        elif self.question[1] == QuestionType.MULTI_SELECT:
            self.input_field = CheckButtonField(self.frame, self.question[2])

        else:  # if self.question[1] == QuestionType.TEXT_FIELD:
            self.input_field = TextFields(self.frame)

    def destroy(self):
        """
        Removes all frames and items in the frames
        :return:
        """
        self.question_field.destroy()
        self.question_field = None

        # if self.question[1] == QuestionType.SELECT or self.question[1] == QuestionType.MULTI_SELECT:
        #     self.input_field.destroy()
        # else:
        #     self.input_field.destroy()

        self.input_field.destroy()
        self.input_field = None
        self.button.destroy()
        self.button = None
        self.frame.destroy()
        self.frame = None

    def update(self, empty):
        """
        Updates the question and input fields + terminates test if necessary
        :param empty: contains whether questions are left
        """
        self.input_field.destroy()
        self.button.destroy()

        if not empty and len(self.kb_class.kb) > 0:
            self.question = self.question_class.get_questions()[0]
            self.add_text(self.question[0])
            self.add_input_field()
            self.add_save_button(self.frame)
        else:
            self.save_results()
            self.save_disclaimers()
            self.destroy()
            self.main_app.add_results_page_button()
            self.main_app.add_trace_page_button()
            self.main_app.initialise_results()

    # prints the studies for which the requirements are met.
    def give_results(self):
        results = "Requirements met for the following studies:\n"
        if len(self.kb_class.kb) > 0:
            for study in self.kb_class.kb:
                results += study['label'] + " at " + study['university'] + "\n"
            self.question_field.configure(height=5 + len(results), anchor=N)
        else:
            results = "No requirements are met. No appropriate study programmes available."
        self.add_text(results)

    @staticmethod
    def make_file(path):
        """
        Creates file to store test results in
        """
        if os.path.exists(path):
            os.remove(path)

        file = open(path, 'x')
        return file

    def save_results(self):
        file = self.make_file('./model/results.txt')
        if len(self.kb_class.kb) > 0:
            for study in self.kb_class.kb:
                file.write(study['label'] + ", " + study['university'] + ", " + study['link'] + "\n")
            file.close()

    def save_disclaimers(self):
        file = self.make_file('./model/disclaimers.txt')
        file.write(self.disclaimer.get_disclaimers())
        file.close()
