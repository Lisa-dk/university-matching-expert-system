from tkinter import *

from view.theme import Theme


class CheckButtonField:
    def __init__(self, master, options):
        self.master = master
        self.options = options
        self.buttons = []
        self.check_var = []

        # Creating a scrollable frame 
        if len(options) > 8:
            self.container = Frame(master, bg=Theme.BG_COLOUR)
            self.container.pack(side=TOP, expand=YES)

            self.canvas = Canvas(self.container, bg=Theme.BG_COLOUR, height=360, width=300, highlightthickness=0)

            self.scrollbar = Scrollbar(self.container, orient="vertical", command=self.canvas.yview, bg=Theme.BG_COLOUR)

            self.frame = Frame(self.canvas, bg=Theme.BG_COLOUR)

            self.add_check_button(self.frame)

            self.canvas.create_window(0, 0, anchor='nw', window=self.frame)

            self.canvas.update_idletasks()

            self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scrollbar.set)

            self.canvas.pack(fill='y', expand=YES, side=LEFT, pady=10)
            self.scrollbar.pack(fill='y', side='left', pady=10)
            self.scrollbar.config(command=self.canvas.yview)

        else:
            self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
            self.frame.pack(side="top")

            self.add_check_button(self.frame)

    def add_check_button(self, frame):
        """
        Adds check buttons for all options to a question
        :param frame: frame to place buttons in
        """
        for option in self.options:
            idx = self.options.index(option)
            self.check_var.append(IntVar(frame))
            self.buttons.append(Checkbutton(frame, text=option, variable=self.check_var[idx], onvalue=1, offvalue=0,
                                            fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=0, font=('Arial', 16),
                                            selectcolor=Theme.BUTTON_COLOUR, activebackground=Theme.BG_COLOUR,
                                            activeforeground=Theme.TEXT_COLOUR, pady=5))
            self.buttons[idx].pack(anchor=W)

    def get_chosen_option(self):
        """
        Gets the checked buttons
        :return: list containing all checked options
        """
        chosen = []
        for idx in range(len(self.check_var)):
            if self.check_var[idx].get() == 1:
                chosen.append(self.options[idx])
        return chosen

    def destroy(self):
        if len(self.options) > 8:
            self.container.destroy()
            self.canvas.destroy()
            self.scrollbar.destroy()
        else:
            self.frame.destroy()
