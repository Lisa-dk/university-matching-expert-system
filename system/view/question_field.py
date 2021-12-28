from tkinter import *
from tkinter.font import Font
from control.next_button import load_new_question
from model.questions import Question


class QuestionField:
    def __init__(self, master, kb_class):
        self.master = master
        self.button = None
        # self.question_frame = None
        self.question_field = None
        self.question_text = StringVar()
        # self.master = master
        # self.master = Frame(self.master, bg="#1c4046")
        # self.master.pack()
        self.question_class = Question()
        self.question = self.question_class.get_questions()[0]
        self.kb_class = kb_class

        self.add_question_field(self.master)
        self.add_text(self.question)

        self.input_field = None
        self.options = None
        self.add_input_field()

        self.add_save_button(self.master)

    def add_question_field(self, frame):
        # self.question_frame = Frame(frame, bg="#1c4046")
        # self.question_frame.pack()
        # self.question_field = Text(self.frame, height=3, width=100, font=Font(family="Arial"), fg="white", bg="#1c4046", bd=0)
        self.question_field = Label(frame, textvariable=self.question_text, height=3, width=100, wraplength=500, justify=LEFT, font=Font(family="Arial"), fg="white", bg="#1c4046", bd=0)
        # self.question_field.grid(column=0, row=0)
        self.question_field.pack()

    def add_text(self, text):
        # self.question_field.insert(END, "\n" + text)
        # self.question_field.config(state=DISABLED)
        self.question_text.set(text)

    def add_save_button(self, frame):
        self.button = Button(frame, height=1, width=10, text="Next",
                             command=lambda: load_new_question(self, self.kb_class, self.question_class, self.question,
                                                               self.input_field), bg="#768c90", bd=1)
        # self.button.grid(column=0, row=2)
        self.button.pack()

    def add_input_field(self):
        # TODO: change with questiontypes
        if 'diploma' in self.question:
            self.options = ['Lise Diploma', 'AP', 'IB', 'Label France Education', 'British GCE A Levels']
            self.input_field = RadioButtonField(self.master, self.options)

        elif 'subject' in self.question:
            self.options = ['Analytics & Approaches SL', 'Analytics & Approaches HL', 'Mathematics SL', 'Mathematics HL',
                            'Calculus', 'Physics SL', 'Physics HL', 'Chemistry SL', 'Chemistry HL']
            self.input_field = CheckButtonField(self.master, self.options)

        else:
            self.input_field = TextFields(self.master)

    def destroy(self):
        self.question_field.destroy()
        # self.question_frame = None
        self.question_field = None
        if 'diploma' in self.question:
            self.input_field.frame.destroy()
            self.options = None
        elif 'subject' in self.question:
            self.input_field.frame.destroy()
            self.options = None
        else:
            self.input_field.input_text.destroy()
        self.input_field = None
        self.button.destroy()
        self.button = None

    # updates the question and input text fields
    def update(self, empty):
        # self.question_field.config(state=NORMAL)
        # self.question_field.delete("1.0", "end-1c")

        if 'diploma' in self.question:
            self.input_field.frame.destroy()

        elif 'subject' in self.question:
            self.input_field.frame.destroy()
        else:
            self.input_field.input_text.destroy()
            # self.input_field.input_text.delete("1.0", "end-1c")

        self.button.destroy()

        if not empty and len(self.kb_class.kb) > 0:
            self.question = self.question_class.get_questions()[0]
            self.add_text(self.question)
            self.add_input_field()
            self.add_save_button(self.master)
        else:
            # self.button.destroy()
            # if 'diploma' not in self.question and 'subject' not in self.question:
            #     self.input_field.input_text.destroy()
            self.give_results()

    # prints the studies for which the requirements are met.
    def give_results(self):
        results = "Requirements met for the following studies:\n"
        if len(self.kb_class.kb) > 0:
            for study in self.kb_class.kb:
                results += study['label'] + " at " + study['university'] + "\n"
            self.question_field.configure(height=5 + len(results))
        else:
            results = "No requirements are met. No appropriate study programmes available."
        self.add_text(results)


class TextFields:
    def __init__(self, master):
        self.input_text = None
        self.master = master
        self.frame = Frame(self.master, bg="#1c4046")
        # self.frame.grid(column=0, row=1)
        self.frame.pack()
        self.add_text_field(self.frame)

    def add_text_field(self, frame):
        self.input_text = Text(frame, height=3, width=10, font=Font(family="Arial"), fg="white", bg="#1c4046", bd=0)
        self.input_text.pack()

    def get_chosen_option(self):
        print(self.input_text.get("1.0", "end-1c"))
        return self.input_text.get("1.0", "end-1c")


class RadioButtonField:
    def __init__(self, master, options):
        self.master = master
        self.options = options
        self.frame = Frame(self.master, bg="#1c4046")
        # self.frame.grid(column=0, row=1)
        self.frame.pack()
        # self.buttons = [None] * len(options)
        self.chosen = StringVar(self.frame, options[0])
        self.add_radio_button(self.frame)

    def add_radio_button(self, frame):
        for option in self.options:
            # self.buttons[self.options.index(option)] = \
            # TODO: align check buttons
            Radiobutton(frame, text=option, variable=self.chosen, value=option, fg="#e5e5e5", bg="#1c4046", bd=0, selectcolor="#768c90").pack()

    def get_chosen_option(self):
        print(self.chosen.get())
        return self.chosen.get()


class CheckButtonField:
    def __init__(self, master, options):
        self.master = master
        self.options = options
        self.frame = Frame(self.master, bg="#1c4046")
        # self.frame.grid(column=0, row=1)
        self.frame.pack()
        # self.buttons = [None] * len(options)
        self.buttons = []
        # self.chosen = [IntVar(self.frame)] * len(options)
        self.check_var = []
        self.add_check_button(self.frame)

    def add_check_button(self, frame):
        # TODO: align check buttons
        for option in self.options:
            idx = self.options.index(option)
            self.check_var.append(IntVar(frame))
            # self.buttons[self.options.index(option)] = \
            self.buttons.append(Checkbutton(frame, text=option, variable=self.check_var[idx], onvalue=1, offvalue=0, font=Font(family="Arial"), fg="#e5e5e5", bg="#1c4046", bd=0, selectcolor="#768c90"))
            self.buttons[idx].pack()

    def get_chosen_option(self):
        chosen_string = ""
        for idx in range(len(self.check_var)):
            if self.check_var[idx].get() == 1:
                chosen_string += self.options[idx] + ", "
        if chosen_string == "":
            chosen_string = "nothing"
        print(chosen_string)
        return chosen_string
