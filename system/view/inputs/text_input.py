from tkinter import *
from tkinter.font import Font
from view.theme import Theme


class TextFields:
    def __init__(self, master):
        self.input_text = None
        self.master = master
        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.frame.pack()
        self.add_text_field(self.frame)

    def add_text_field(self, frame):
        self.input_text = Text(frame, height=3, width=10, font=Font(family="Arial"), fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=0)
        self.input_text.pack()

    def get_chosen_option(self):
        print(self.input_text.get("1.0", "end-1c"))
        return self.input_text.get("1.0", "end-1c")