from tkinter.font import Font
from tkinter import *
from view.theme import Theme

import os


class InformationPage:
    def __init__(self, main_app, master):
        self.button = None
        self.main_app = main_app
        self.master = master
        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.text_field = Text(self.frame, font=Font(family="Arial"), fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=0)
        info = "\nWelcome to the study programme test!\n" \
               "This test aims to recommend/match Turkish students with engineering study programmes at Dutch " \
               "universities. Be aware, however, that not all requirements are included and you should check the " \
               "requirements of the recommended universities as well."
        self.text_field.insert(END, info)
        self.text_field.configure(state='disabled', width=53, height=8)

        self.path = './model/results.txt'
        if os.path.exists(self.path):
            self.make_retake_button()
        else:
            self.make_start_button()
            
        self.text_field.pack()
        self.button.pack()
        self.frame.pack()

    def make_start_button(self):
        self.button = Button(self.frame, text="Start Test", bg=Theme.BUTTON_COLOUR, bd=1, command=self.start_test)

    def make_retake_button(self,):
        self.button = Button(self.frame, text="Retake Test", bg=Theme.BUTTON_COLOUR, bd=1, command=self.retake_test)

    def retake_test(self):
        os.remove(self.path)
        self.main_app.initialise_kb()
        self.start_test()

    def start_test(self):
        self.destroy()
        self.main_app.start_test()

    def destroy(self):
        self.button.destroy()
        self.text_field.destroy()
        self.frame.destroy()