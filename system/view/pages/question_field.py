from tkinter import *
from tkinter.font import Font
from control.next_button import load_new_question
from model.questions import Question, QuestionType
from view.inputs.single_option import RadioButtonField
from view.inputs.multiple_options import CheckButtonField
from view.inputs.text_input import TextFields
from view.theme import Theme
from model.disclaimer import Disclaimer

import os


class QuestionField:

    def __init__(self, master, kb_class, main_app):
        self.master = master
        self.main_app = main_app
        self.button = None
        self.question_field = None
        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.frame.pack()

        # TODO: Scrollbar needs canvas apparently...
        # self.canvas = Canvas(self.frame)
        # self.scrollbar = Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        # self.scrollable_frame = Frame(self.canvas)
        # self.scrollable_frame.bind(
        #    "<Configure>",
        #    lambda e: self.canvas.configure(
        #        scrollregion=self.canvas.bbox("all")
        #    )
        # )
        # self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        # self.canvas.configure(yscrollcommand=self.scrollbar.set)
        # self.frame.pack(fill="both", expand=True)
        # self.canvas.pack(side="left", fill="both", expand=True)
        # self.scrollbar.pack(side="right", fill="y")

        self.question_text = StringVar()
        self.question_class = Question()
        self.disclaimer = Disclaimer()
        self.visited = ['start']
        self.question = self.question_class.get_questions()[0]
        self.kb_class = kb_class

        self.add_question_field(self.frame)
        self.add_text(self.question[0])

        self.input_field = None
        self.options = None
        self.add_input_field()

        self.add_save_button(self.frame)

    def add_question_field(self, scrollable_frame):
        self.question_field = Label(scrollable_frame, textvariable=self.question_text, height=3, width=100,
                                    wraplength=500,
                                    justify=LEFT, font=Font(family="Arial"), fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR,
                                    bd=0)
        self.question_field.pack()

    def add_text(self, text):
        self.question_text.set(text)

    def add_save_button(self, scrollable_frame):
        self.button = Button(scrollable_frame, height=1, width=10, text="Next",
                             command=lambda: load_new_question(self, self.kb_class, self.question_class, self.question,
                                                               self.input_field), bg=Theme.BUTTON_COLOUR, bd=1,
                             activebackground=Theme.BUTTON_CLICK)

        self.button.pack(side="bottom")

    def add_input_field(self):
        # DONE: change with question types
        # if 'diploma' in self.question:
        if self.question[1] == QuestionType.SELECT:
            # self.options = ['Lise Diploma', 'AP', 'IB', 'Label France Education', 'British GCE A Levels']
            # self.input_field = RadioButtonField(self.frame, self.options)
            self.input_field = RadioButtonField(self.frame, self.question[2])

        # elif 'subject' in self.question:
        elif self.question[1] == QuestionType.MULTI_SELECT:
            # self.options = ['Analytics & Approaches SL', 'Analytics & Approaches HL', 'Mathematics SL', 'Mathematics HL', 'Calculus', 'Physics SL', 'Physics HL', 'Chemistry SL', 'Chemistry HL']
            # self.input_field = CheckButtonField(self.frame, self.options)
            self.input_field = CheckButtonField(self.frame, self.question[2])

        else:  # if self.question[1] == QuestionType.TEXT_FIELD:
            self.input_field = TextFields(self.frame)

    def destroy(self):
        self.question_field.destroy()
        # self.question_frame = None
        self.question_field = None
        # if 'diploma' or 'subject' in self.question:
        if self.question[1] == QuestionType.SELECT or self.question[1] == QuestionType.MULTI_SELECT:
            self.input_field.frame.destroy()
            # self.options = None
        else:
            self.input_field.input_text.destroy()
        self.input_field = None
        self.button.destroy()
        self.button = None
        self.frame.destroy()
        self.frame = None

    # updates the question and input fields
    def update(self, empty):
        self.input_field.frame.destroy()
        self.button.destroy()

        if not empty and len(self.kb_class.kb) > 0:
            self.question = self.question_class.get_questions()[0]
            self.add_text(self.question[0])
            self.add_input_field()
            self.add_save_button(self.frame)
        else:
            self.save_results()
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
    def make_file():
        path = './model/results.txt'
        if os.path.exists(path):
            os.remove(path)

        file = open(path, 'x')
        return file

    def save_results(self):
        file = self.make_file()
        if len(self.kb_class.kb) > 0:
            for study in self.kb_class.kb:
                file.write(study['label'] + ", " + study['university'] + "\n")
        print('saved')