from tkinter import *
from tkinter import messagebox
import os
import re

from view.design.theme import Theme


class TracePage:
    def __init__(self, master):
        self.trace = None
        self.trace_field = None
        self.master = master

        self.frame = Frame(self.master, bg=Theme.BG_COLOUR, width=750, height=600)
        self.scrollbar = Scrollbar(self.frame, orient="vertical", bg=Theme.BG_COLOUR)
        self.scrollbar.pack(fill='y', side='right', pady=10)

        self.load_trace()
        self.display_trace()

        self.scrollbar.config(command=self.trace_field.yview)
        self.frame.pack(anchor='center', ipady=10, ipadx=10)

    def load_trace(self):
        """
        Loads the trace from a text file
        """
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
                            self.trace += ln[1][1:]
                        else:
                            if re.search('eliminated studies', ln[0]) or re.search('response', ln[0]):
                                if re.search('eliminated studies', ln[0]):
                                    if ln[1] == 'None':
                                        self.trace += 'No studies were eliminated:\n'
                                    else:
                                        self.trace += 'The following studies were eliminated:\n'
                                answers = ln[1][1:].split(';')
                                for item in answers:
                                    if item:
                                        self.trace += item + '\n'
        else:
            messagebox.showerror("Error", "Something went wrong, please restart the program.")

    def display_trace(self):
        """
        Shows trace in frame
        """
        self.trace_field = Text(self.frame, yscrollcommand=self.scrollbar.set,
                                wrap='word', font=('Arial', 15), relief=FLAT,
                                fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=0)
        self.trace_field.insert("1.0", self.trace, CENTER)
        self.trace_field.pack(side='top', fill=X)

    def destroy(self):
        """
        Removes frame + its items
        """
        self.trace_field.destroy()
        self.frame.destroy()
        self.scrollbar.destroy()
