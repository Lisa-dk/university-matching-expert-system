from tkinter import *
# from tkinter.font import Font
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
        """
        Adds single-check buttons for all options to a question
        :param frame: frame to place buttons in
        """
        for option in self.options:
            Radiobutton(frame, text=option, variable=self.chosen, value=option, font=("Arial", 17),
                        fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=0, selectcolor=Theme.BUTTON_COLOUR,
                        activebackground=Theme.BG_COLOUR, activeforeground=Theme.TEXT_COLOUR).pack(fill=X, anchor=W, pady=5)

    def get_chosen_option(self):
        """
        Gets checked button
        :return: checked button contents (as str)
        """
        print(self.chosen.get())
        return self.chosen.get()
    
    def destroy(self):
        self.frame.destroy()
