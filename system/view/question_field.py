from tkinter import *
from control.next_button import load_new_question
from model.questions import Question


class QuestionField():
    def __init__(self, master, kb_class):
        self.button = None
        self.text_field = None
        self.master = master
        self.question_class = Question()
        self.question = self.question_class.get_questions()[0]
        self.kb_class = kb_class

        self.add_text_field(self.master)
        self.add_text(self.question)

        self.input_field = InputFields(self.master)

        self.add_save_button(self.master)

    def add_text_field(self, frame):
        self.text_field = Text(frame, height=5, width=100)
        self.text_field.pack()

    def add_text(self, text):
        self.text_field.insert(END, text)

    def add_save_button(self, frame):
        self.button = Button(frame, height=1, width=10, text="Next",
                             command=lambda: load_new_question(self, self.kb_class, self.question_class, self.question,
                                                               self.input_field))
        self.button.pack()

    # updates the question and input text fields
    def update(self, empty):
        self.text_field.delete("1.0", "end-1c")
        self.input_field.input_text.delete("1.0", "end-1c")

        if len(self.kb_class.kb) == 0:
            self.add_text("No requirements are met. No appropriate study programmes available.")

        if not empty and len(self.kb_class.kb) > 0:
            self.question = self.question_class.get_questions()[0]
            self.add_text(self.question)
        else:
            self.input_field.input_text.destroy()
            self.button.destroy()
            self.give_results()

    # prints the studies for which the requirements are met.
    def give_results(self):
        results = "Requirements met for the following studies:\n"
        if len(self.kb_class.kb) > 0:
            for study in self.kb_class.kb:
                results += study['label'] + " at " + study['university'] + "\n"
        self.add_text(results)


class InputFields():
    def __init__(self, master):
        self.input_text = None
        self.master = master
        self.add_input_text_field(self.master)

    def add_input_text_field(self, frame):
        self.input_text = Text(frame, height=3, width=10)
        self.input_text.pack()
