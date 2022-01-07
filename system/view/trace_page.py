from tkinter import messagebox
from view.theme import Theme
from tkinter import *
from tkinter.font import Font
import os
import re


class TracePage:
    def __init__(self, master):
        self.trace = None
        self.trace_field = None
        self.master = master
        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.frame.pack()
        self.load_trace()
        self.display_trace()

    def load_trace(self):
        path = './model/trace.txt'
        if os.path.exists(path):
            if os.stat(path).st_size == 0:
                messagebox.showerror("Error", "Something went wrong, please restart the program.")
            else:
                with open('./model/trace.txt', 'r') as file:
                    self.trace = ''
                    for line in file:
                        ln = line.split(':')
                        if re.search('question', ln[0]):
                            self.trace += ln[0] + ln[1]
                        else:
                            if re.search('response', ln[0]):
                                self.trace += 'Your response:\n'
                            elif re.search('eliminated studies', ln[0]):
                                if ln[1] == 'None':
                                    self.trace += 'No studies were eliminated:\n'
                                else:
                                    self.trace += 'The following studies were eliminated:\n'

                            answers = ln[1].split(',')
                            for item in answers:
                                if item != []:
                                    self.trace += item + '\n'
        else:
            messagebox.showerror("Error", "Something went wrong, please restart the program.")

    def display_trace(self):
        self.trace_field = Label(self.frame, text=self.trace, width=100,
                                   wraplength=500, justify=LEFT, font=Font(family="Arial"), fg=Theme.TEXT_COLOUR,
                                   bg=Theme.BG_COLOUR, bd=0)
        self.trace_field.pack(side=TOP, ipady=10)

    def destroy(self):
        self.trace_field.destroy()
        self.frame.destroy()
