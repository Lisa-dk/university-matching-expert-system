from tkinter import messagebox
from view.theme import Theme
from tkinter import *
# from tkinter.font import Font
import os
import re


class TracePage:
    def __init__(self, master):
        self.trace = None
        self.trace_field = None
        self.master = master

        # self.container = Frame(master, bg=Theme.BG_COLOUR)
        # self.container.pack()
        self.frame = Frame(self.master, bg=Theme.BG_COLOUR, width=750, height=600)
        # self.frame.pack(anchor='center', ipady=10, ipadx=10)

        # self.canvas = Canvas(self.container, bg=Theme.BG_COLOUR, width=750, height=600)
        # self.scrollbar = Scrollbar(self.container, orient="vertical", command=self.canvas.yview, bg=Theme.BG_COLOUR)
        self.scrollbar = Scrollbar(self.frame, orient="vertical", bg=Theme.BG_COLOUR)
        self.scrollbar.pack(fill='y', side='right', pady=10)

        # self.frame = Frame(self.canvas, bg=Theme.BG_COLOUR)
        # self.frame.pack()

        self.load_trace()
        self.display_trace()

        # self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        #
        # self.canvas.update_idletasks()
        #
        # self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scrollbar.set)
        #
        # self.canvas.pack(fill='y', expand='yes', side='left')
        # self.scrollbar.pack(fill='y', side='right', pady=5)

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
                                print(ln)
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
        # self.container.destroy()
        self.frame.destroy()
        # self.canvas.destroy()
        self.scrollbar.destroy()
