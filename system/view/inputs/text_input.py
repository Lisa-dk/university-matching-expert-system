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
        """
        Adds a text field to the frame
        :param frame: frame to add text field to
        """
        self.input_text = Text(frame, height=3, width=10, font=Font(family="Arial"), fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=1)
        self.input_text.pack(pady=10)

    def get_chosen_option(self):
        """
        Gets contents text field
        :return: contents text field (as str)
        """
        print(self.input_text.get("1.0", "end-1c"))
        return self.input_text.get("1.0", "end-1c")