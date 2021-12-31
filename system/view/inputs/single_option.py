from tkinter import *
from view.theme import Theme


class RadioButtonField:
    def __init__(self, master, options):
        self.master = master
        self.options = options
        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.frame.pack()
        self.chosen = StringVar(self.frame, options[0])
        self.add_radio_button(self.frame)

    def add_radio_button(self, frame):
        for option in self.options:
            Radiobutton(frame, text=option, variable=self.chosen, value=option, fg=Theme.TEXT_COLOUR,
                                       bg=Theme.BG_COLOUR, bd=0, selectcolor=Theme.BUTTON_COLOUR).pack(anchor=W)

    def get_chosen_option(self):
        print(self.chosen.get())
        return self.chosen.get()
