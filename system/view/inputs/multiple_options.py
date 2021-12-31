from tkinter import *
from tkinter.font import Font
from view.theme import Theme


class CheckButtonField:
    def __init__(self, master, options):
        self.master = master
        self.options = options
        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.frame.pack(pady=(0, 10))
        self.buttons = []
        self.check_var = []
        self.add_check_button(self.frame)

    def add_check_button(self, frame):
        for option in self.options:
            idx = self.options.index(option)
            self.check_var.append(IntVar(frame))
            self.buttons.append(Checkbutton(frame, text=option, variable=self.check_var[idx], onvalue=1, offvalue=0,
                                            font=Font(family="Arial"), fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=0,
                                            selectcolor=Theme.BUTTON_COLOUR, activebackground=Theme.BG_COLOUR,
                                            activeforeground=Theme.TEXT_COLOUR))
            self.buttons[idx].pack(anchor=W)

    def get_chosen_option(self):
        chosen_string = ""
        for idx in range(len(self.check_var)):
            if self.check_var[idx].get() == 1:
                chosen_string += self.options[idx] + ", "
        print(chosen_string)
        return chosen_string
