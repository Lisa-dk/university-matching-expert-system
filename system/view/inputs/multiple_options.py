from tkinter import *
from tkinter.font import Font


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
        for option in self.options:
            idx = self.options.index(option)
            self.check_var.append(IntVar(frame))
            self.buttons.append(Checkbutton(frame, text=option, variable=self.check_var[idx], onvalue=1, offvalue=0,
                                            font=Font(family="Arial"), fg="#e5e5e5", bg="#1c4046", bd=0,
                                            selectcolor="#768c90"))
            self.buttons[idx].pack(anchor=W)

    def get_chosen_option(self):
        chosen_string = ""
        for idx in range(len(self.check_var)):
            if self.check_var[idx].get() == 1:
                chosen_string += self.options[idx] + ", "
        print(chosen_string)
        return chosen_string
