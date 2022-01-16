from tkinter import *
# from tkinter.font import Font
from view.theme import Theme


class TextFields:
    def __init__(self, master):
        self.input_text = StringVar()  # the text in  your entry
        self.input_widget = None
        self.master = master
        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.frame.pack()
        self.add_text_field(self.frame)

    def add_text_field(self, frame):
        """
        Adds a text field to the frame
        :param frame: frame to add text field to
        """
        # self.input_text = Text(frame, height=1, width=5, font=('Arial', 16), fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=1, wrap='word')

        self.input_widget = Entry(frame, width=5, font=('Arial', 16), fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=1, textvariable=self.input_text)
        self.input_widget.focus_set()
        self.input_widget.pack(padx=10, pady=5)

        def character_limit(entry_text):
            if len(entry_text.get()) > 0:
                entry_text.set(entry_text.get()[-1])

        self.input_text.trace("w", lambda *args: character_limit(self.input_text))

    def get_chosen_option(self):
        """
        Gets contents text field
        :return: contents text field (as str)
        """
        print(self.input_widget.get()[-1])
        return self.input_widget.get()[-1]
    
    def destroy(self):
        self.input_widget.destroy()
        self.frame.destroy()
