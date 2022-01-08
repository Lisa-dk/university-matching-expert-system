from tkinter import *


# class from https://blog.teclado.com/tkinter-scrollable-frames/
from view.theme import Theme


class ScrollFrame(Frame):
    def __init__(self, container):
        super().__init__(container)

        canvas = Canvas(container, bg=Theme.BG_COLOUR)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)

        self.scrollable_frame = Frame(canvas, bg=Theme.BG_COLOUR)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
