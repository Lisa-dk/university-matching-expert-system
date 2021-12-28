from tkinter import *
from tkinter.font import Font


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
        i = 0
        for option in self.options:
            radio_button = Radiobutton(frame, text=option, variable=self.chosen, value=option, fg="#e5e5e5",
                                       bg="#1c4046", bd=0, selectcolor="#768c90").pack(anchor=W)

    def get_chosen_option(self):
        print(self.chosen.get())
        return self.chosen.get()
