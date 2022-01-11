from tkinter import *
# from view.scroll_frame import ScrollFrame
from view.theme import Theme


class CheckButtonField:
    def __init__(self, master, options):
        self.master = master
        self.options = options
        self.buttons = []
        self.check_var = []
        if len(options) > 15:
            # self.frame = ScrollFrame(self.master)

            container = Frame(master, bg=Theme.BG_COLOUR)
            container.pack(side=TOP, expand=YES)

            canvas = Canvas(container, bg=Theme.BG_COLOUR, height=300, width=200, highlightthickness=0)
            scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview, bg=Theme.BG_COLOUR)

            self.frame = Frame(canvas, bg=Theme.BG_COLOUR)

            self.add_check_button(self.frame)

            canvas.create_window(0, 0, anchor='nw', window=self.frame)

            canvas.update_idletasks()

            canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)

            canvas.pack(fill='y', expand=YES, side=LEFT)
            scrollbar.pack(fill='y', side='left', pady=5)

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
                                            fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=0, font=('Arial', 17),
                                            selectcolor=Theme.BUTTON_COLOUR, activebackground=Theme.BG_COLOUR,
                                            activeforeground=Theme.TEXT_COLOUR))
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
